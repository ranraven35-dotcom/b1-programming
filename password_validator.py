import string
import random

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)

def has_digit(password):
    return any(char in string.digits for char in password)

def has_special_char(password):
    return any(char in string.punctuation for char in password)

def validate_password(password):
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special': has_special_char(password)
    }
    results['is_valid'] = all(results.values())
    return results

def main():
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)
    print("\nPassword Requirements:")
    print("  • Minimum 8 characters")
    print("  • At least one uppercase letter")
    print("  • At least one lowercase letter")
    print("  • At least one digit")
    print("  • At least one special character (!@#$%^&* etc.)")
    print()
    
    password = input("Enter password to validate: ")
    results = validate_password(password)
    
    print("\n" + "=" * 50)
    print("VALIDATION RESULTS")
    print("=" * 50)
    
    check_symbol = "✓" if results['min_length'] else "✗"
    print(f"{check_symbol} Minimum length (8+ chars): {results['min_length']}")
    
    check_symbol = "✓" if results['has_uppercase'] else "✗"
    print(f"{check_symbol} Contains uppercase: {results['has_uppercase']}")
    
    check_symbol = "✓" if results['has_lowercase'] else "✗"
    print(f"{check_symbol} Contains lowercase: {results['has_lowercase']}")
    
    check_symbol = "✓" if results['has_digit'] else "✗"
    print(f"{check_symbol} Contains digit: {results['has_digit']}")
    
    check_symbol = "✓" if results['has_special'] else "✗"
    print(f"{check_symbol} Contains special char: {results['has_special']}")
    
    print("\n" + "=" * 50)
    if results['is_valid']:
        print("✓ PASSWORD IS STRONG!")
    else:
        print("✗ PASSWORD IS WEAK - Please address failed requirements")
    print("=" * 50)

if __name__ == "__main__":
    main()
