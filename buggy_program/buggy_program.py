# buggy_program.py — Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers): 
    # error1: SyntaxError, missing ":"
    # found myself with traceback
    numbers = [int(i) for i in numbers] 
    # error4
    # fix for TypeError found in the definition variables and in attempting to use the function to calculate stats on the scores
    # fix: converts all items to proper type
    # AI found this error.

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    above_average = []
    for num in numbers:
        if num > average: 
            # error2: SyntaxError, missing ":"
            # found myself with traceback
            above_average.append(num)
    
    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [85, 92, 78, 95, 88, "70", 93]
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']:.2f}") 
# error3: NameError, missing quotations around 'average'
# found myself - commented out above lines and used traceback to confirm error type and resolution
print(f"Above average: {result['above_count']} scores")
