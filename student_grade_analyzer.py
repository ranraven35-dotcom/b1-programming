student_records = []
stats = {}

print("=== GRADE ANALYZER ===\n")

for i in range(1, 7):
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))
    print()

scores = [score for name, score in student_records]

stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores) / len(scores)

unique_scores = set(scores)

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

print("\n" + "="*40)
print("=== STUDENT RECORDS ===")
print("="*40)
for i, (name, score) in enumerate(student_records, 1):
    print(f"{i}. {name}: {score}")

print("\n" + "="*40)
print("=== CLASS STATISTICS ===")
print("="*40)
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n" + "="*40)
print("=== UNIQUE SCORES ===")
print("="*40)
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")

print("\n" + "="*40)
print("=== GRADE DISTRIBUTION ===")
print("="*40)
for score in sorted(grade_distribution.keys(), reverse=True):
    count = grade_distribution[score]
    plural = "students" if count != 1 else "student"
    print(f"Score {score}: {count} {plural}")
