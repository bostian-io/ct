# AI Evaluation notes
> Apply to grade_analyzer.py

1. Pythonic
python
from collections import Counter

def get_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

grade_distribution = Counter(get_grade(s) for s in scores)

Counter returns 0 for missing keys, so grade_distribution["F"] is safe even if nobody failed.

✅ The review suggested a grading function and `Counter` from `collections`. It seems more Pythonic and like it would be an improvement. It says it's more common. 
❌ I want to keep the code at a level I understand and can maintain, so I won't implement it. The review said my code was already clean and readable, so leaving it as is is a reasonable choice. I'll revisit this when I'm closer to covering things like `Counter`.

2. Edge cases

Empty list crashes. sum / len, max, and min all raise errors on an empty list. Guard it, or wrap the average in a helper:

python
def average(scores):
    return sum(scores) / len(scores) if scores else 0.0

if not scores:
    print("No scores to analyze.")
else:
    # existing report code here

✅ 'def average' seems like it would make it more testable and clean up code as a function
✅ 'if scores else 0.0' seems like reasoable way to handle empty list
✅ 'if not scores' reasonable improvement to handle empty score list
✅ I do understand what both solutions do and why I should implement them
✅ implemented both and full functionaly preserved

3. Security / reliability

Nothing serious. You’re using int() rather than eval(), which was the one real risk. The only change worth making is narrowing your try so it wraps only int():

python
try:
    new_score = int(user_entry)
except ValueError:
    print("Invalid input.")
    continue

Right now, any ValueError raised inside the block would be misreported as bad user input.

✅ It's reasonable to only apply the Except and ValueError to that interaction, especially if we know surrounding code can be negatively impacted.
✅ I understand the change and it's value.
✅ Implemented and full functionality preserved.