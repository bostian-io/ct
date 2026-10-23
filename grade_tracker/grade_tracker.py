# takes csv
# has 5 functions
# 1. load_students(filepath)
# 2. calculate_average(grades)
# 3. get_letter_grade(average)
# 4. generate_report(students)
# 5. write_report(report,filepath)

import csv

def load_students(filepath):
    """Read the CSV and return a list of dictionaries (one per student)."""
    try:
        with open(filepath, newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error could not find '{filepath}'. Check that the file exists in the correct location.")
        return []

def calculate_average(grades):
    """Average the students grades. Skip empty strings and return None if none."""
    student_grades = []
    for g in grades:
        g = str(g).strip() # make sure it's string, then strip all whitespaces
        if g == "": # make sure we're skipping empty ones
            continue
        try: 
            student_grades.append(float(g)) # we want to make it a float before appending it
        except ValueError:
            print(f"Warning, invalid grade '{g}'.")
    if not student_grades:
        return None
    return round(sum(student_grades) / len(student_grades), 1)

def get_letter_grade(average):
    """Get letter grades for student grade averages."""
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

def generate_report(students):
    """Generate a summay dictionary from student records of student performance."""
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    results = []

    for student in students:
        name = student["student_name"]
        reported_grades = [value for key, value in student.items() if key != "student_name"] # list comprehension that loops through and builds a list of grades, keeps the value only if the key isn't "student_name", so you're only left with grades (which are the rest the columns of the csv)
        average = calculate_average(reported_grades)
        letter = get_letter_grade(average)
        grade_distribution[letter] += 1
        results.append({"name": name, "average": average, "letter_grade": letter})

    # averages pulls those values from results so that we can use them in what we return in this report
    averages = [r["average"] for r in results if r["average"] is not None] # 'is not None' filtered out to avoid crashes when we pull comparisons for reporting

    # uses averages to compute those statistics and others from the previos for loop
    return {
            "total_students": len(students),
            "class_average": round(sum(averages) / len(averages), 1) if averages else None,
            "highest_average": max(averages) if averages else None,
            "lowest_average": min(averages) if averages else None,
            "grade_distribution": grade_distribution,
            "students": results,
    }

def write_report(report, filepath): # takes report from above and filepath for writing
    """Write a formatted report to a text file."""
    with open(filepath, "w") as f:
        f.write("STUDENT GRADE REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total students:   {report['total_students']}\n")
        f.write(f"Class average:    {report['class_average']}\n")
        f.write(f"Highest average:  {report['highest_average']}\n")
        f.write(f"Lowest average:   {report['lowest_average']}\n\n")

        # loop through the KV pairs of grade distribution and writes formatted output
        f.write("Grade Distribution:\n")
        for grade, count in report["grade_distribution"].items():
            f.write(f"  {grade}: {count}\n")

        # loops through results from above and writes formatted output
        f.write("\nIndividual Results:\n")
        for s in report["students"]:
            avg = s["average"] if s["average"] is not None else "N/A"
            f.write(f"  {s['name']:<20} {str(avg):>6}  ({s['letter_grade']})\n")


def main(): # runs the program and uses the functions
    """Run the program: load, report, print, save."""
    print("Loading student data...")
    students = load_students("data/students.csv") # uses load_students function with error handling
    if not students:
        print("No students to report on. Please check data/students.csv.")
        return
    print(f"  Loaded {len(students)} students.\n")

    print("Generating report...\n")
    report = generate_report(students) # runs the generate report function and prints a summary

    print("--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}\n")

    print("Grade Distribution:")
    for grade, count in report["grade_distribution"].items():
        print(f"  {grade}: {count}")

    print("\nTop 5 students:") 
    ranked = [s for s in report["students"] if s["average"] is not None] # list comprehension that loops through our generated report and adds students who have an average
    get_average = lambda s: s["average"] # in-line function to get the average from the dictionaries
    ranked.sort(key=get_average, reverse=True) # .sort is a method of lists, sorts ranked from least to most
    for s in ranked[:5]:
        print(f"  {s['name']:<20} {s['average']:>5}  ({s['letter_grade']})")

    write_report(report, "grade_report.txt") # runs the write_report function to a new text file
    print("\nReport written to grade_report.txt")


if __name__ == "__main__": # python automatically sets a variable called __name__. If I run the program from the file name, is equals main, so the if is true and main() runs.
    main()