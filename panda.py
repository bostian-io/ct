import pandas as pd

data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)

# commented for more clear printing of requested QA's

# print(df.shape)
# print(df.dtypes)
# print(df.head())
# print(df.describe())
# print(df.info())

students_per_course = df.groupby("course")["student"].count()
print("How many students are in each course?:")
print(students_per_course)

average_score_per_course = df.groupby("course")["score"].mean()
print("\nWhat is the average score per course?:")
print(average_score_per_course)

top_3 = df.sort_values("score", ascending=False).head(3)
print("\nWho are the top 3 students by score?:")
print(top_3)

avg_hours_studied = df.groupby("passed")["hours_studied"].mean() # stores the two bool groups for us to use below
passed_avg_hours = avg_hours_studied[True]
failed_avg_hours = avg_hours_studied[False]
print("\nWhat is the average hours studied for students who passed vs. failed?")
print(f"Passed: {passed_avg_hours:.2f} hours")
print(f"Failed: {failed_avg_hours:.2f} hours")

df["grade"] = pd.cut(df["score"], bins=[0, 70, 80, 90, 101], labels=["F", "C", "B", "A"], right=False) 

# print(df.head()) # confirm our new column works

grade_distribution = df.groupby(["course", "grade"], observed=False)["grade"].count()
print("\nWhat’s the distribution of grades per course?")
print(grade_distribution)