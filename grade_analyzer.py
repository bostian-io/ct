scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
grade_distribution = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0 
} # using a dictionary to store the count of each grade
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
    grade_distribution[grade] += 1 #adding the count of each grade to the dictionary

print("=== Grade Analyzer ===")
print(f"Total scores: {len(scores)}")
print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
passing = len(scores) - grade_distribution["F"]
passing_percentage = (passing / len(scores)) * 100
print(f"Passing: {passing} ({passing_percentage:.1f}%)")
failing = len(scores) - passing # we already have the number of passing students, so we can calculate the number of failing students by subtracting passing from the total number of scores
failing_percentage = (failing / len(scores)) * 100
print(f"Failing: {failing} ({failing_percentage:.1f}%)")

print("\nGrade Distribution:")
for grade, count in grade_distribution.items():
    print(f"{grade}: {count} students")

print("\n--- Add More Scores ---")
while True:
    try:
        user_entry = (input("Enter a new score (or type 'done' to finish): "))
        if user_entry.lower() == 'done':
            print(f"\nFinal average: {sum(scores) / len(scores):.1f}")
            break
        new_score = int(user_entry)
        if new_score >= 0 and new_score <= 100: # assumes aren't accepting scores over 100
            scores.append(new_score)
            print(f"Updated average: {sum(scores) / len(scores):.1f}")
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")