import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_discount(category, tier):
    category_discounts = {
        'Electronics': 10,
        'Clothing': 15,
        'Books': 5,
        'Home': 12
    }
    
    tier_discounts = {
        'Premium': 5,
        'Standard': 0,
        'Budget': 2
    }
    
    category_discount = category_discounts.get(category, 0)
    tier_discount = tier_discounts.get(tier, 0)
    
    return category_discount + tier_discount

def process_products(input_file, output_file):
    try:
        products = []
        total_discount = 0
        
        with open(input_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(',')
                    if len(parts) != 4:
                        logging.warning(f"Line {line_num}: Invalid format, skipping")
                        continue
                    
                    name, price_str, category, tier = parts
                    base_price = float(price_str)
                    discount_pct = calculate_discount(category, tier)
                    discount_amt = base_price * (discount_pct / 100)
                    final_price = base_price - discount_amt
                    
                    products.append({
                        'name': name,
                        'base_price': base_price,
                        'discount_pct': discount_pct,
                        'discount_amt': discount_amt,
                        'final_price': final_price
                    })
                    
                    total_discount += discount_pct
                    
                except ValueError as e:
                    logging.error(f"Line {line_num}: Invalid price format - {e}")
                    continue
        
        with open(output_file, 'w') as f:
            f.write("=" * 90 + "\n")
            f.write("PRICING REPORT\n")
            f.write("=" * 90 + "\n")
            f.write(f"{'Product Name':<30} {'Base Price':>12} {'Discount %':>12} "
                    f"{'Discount $':>12} {'Final Price':>12}\n")
            f.write("-" * 90 + "\n")
            
            for product in products:
                f.write(f"{product['name']:<30} "
                        f"${product['base_price']:>11.2f} "
                        f"{product['discount_pct']:>11.1f}% "
                        f"${product['discount_amt']:>11.2f} "
                        f"${product['final_price']:>11.2f}\n")
            
            f.write("=" * 90 + "\n")
        
        avg_discount = total_discount / len(products) if products else 0
        print("\nProcessing Complete!")
        print(f"Total products processed: {len(products)}")
        print(f"Average discount applied: {avg_discount:.2f}%")
        print(f"Report saved to: {output_file}")
        
        logging.info(f"Successfully processed {len(products)} products")
        
    except FileNotFoundError:
        logging.error(f"Input file '{input_file}' not found")
        print(f"Error: Could not find {input_file}")
    except PermissionError:
        logging.error(f"Permission denied writing to '{output_file}'")
        print(f"Error: Cannot write to {output_file}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    process_products('products.txt', 'pricing_report.txt')
