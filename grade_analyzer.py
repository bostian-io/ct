scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
grade_distribution = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}  # using a dictionary to store the count of each grade


def average(scores):
    return sum(scores) / len(scores) if scores else 0.0


for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    grade_distribution[grade] += 1

if not scores:
    print("No scores to analyze.")
else:
    print("=== Grade Analyzer ===")
    print(f"Total scores: {len(scores)}")
    print(f"Average: {average(scores):.1f}")
    print(f"Highest: {max(scores)}")
    print(f"Lowest: {min(scores)}")
    passing = len(scores) - grade_distribution["F"]
    passing_percentage = (passing / len(scores)) * 100
    print(f"Passing: {passing} ({passing_percentage:.1f}%)")
    failing = len(scores) - passing
    failing_percentage = (failing / len(scores)) * 100
    print(f"Failing: {failing} ({failing_percentage:.1f}%)")

    print("\nGrade Distribution:")
    for grade, count in grade_distribution.items():
        print(f"{grade}: {count} students")

print("\n--- Add More Scores ---")
while True:
    try:
        user_entry = input("Enter a new score (or type 'done' to finish): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        break

    if user_entry == "done":
        break

    try:
        new_score = int(user_entry)
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")
        continue

    if 0 <= new_score <= 100:  # assumes that we aren't accepting scores over 100
        scores.append(new_score)
        print(f"Updated average: {average(scores):.1f}")
    else:
        print("Please enter a valid score between 0 and 100.")

print(f"\nFinal average: {average(scores):.1f}")