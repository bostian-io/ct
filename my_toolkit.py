def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0 # covers the case of an empty list
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
    """Find the maximum and minimum values in a list of numbers."""
    if not numbers: # covers the case of an empty list
        return None, None

    max_value = numbers[0]
    min_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

def count_occurrences(items, target):
    """Count the occurrences of a target item in a list."""
    count = 0
    for i in items:
        if i == target:
            count += 1
    return count

def is_palindrome(text):
    """Check if a word is a palindrome."""
    cleaned = text.lower().replace(" ", "") # converts to lowercase and then removes spaces to account for phrases, mixed case, and spacing.
    if len(cleaned) < 2:
        print(f"\nSingle character or empty string: '{text}' is not considered a palindrome.")
        return False # This is not considered a word.
    return cleaned == cleaned[::-1] # Uses slicing to reverse the string and compare it to the original.

def create_report(title, scores):
    """Takes a report title and a list of scores, and returns a formatted string report."""
    average_score = calculate_average(scores)
    max_score, min_score = find_max_and_min(scores)
    return f"Report: {title}\nAverage Score: {average_score:.2f}\nMax Score: {max_score}\nMin Score: {min_score}"

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93, 85, 100, 67, 85, 90, 82, 76, 89, 91, 84, 77, 95, 88, 92, 85, 79, 81, 94, 85] # added more scores to test the count_occurrences function
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print(f"'Racecar a Racecar' palindrome: {is_palindrome('Racecar a Racecar')}") # caps, spacing, and phrase edge case test
    print(f"'a' palindrome: {is_palindrome('a')}") # single character edge case test
    print(f"'' palindrome: {is_palindrome('')}") # empty string edge case test
    print()
    print(create_report("Class Scores", test_scores))

