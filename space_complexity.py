## Part 1 - Classify Space Complexity

# Function A - O(n) Linear space complexity because it creates a new string that is the reverse of the input string, which requires additional space proportional to the length of the input string.
def reverse_string(s):
    return s[::-1]

# Function B - O(n) Linear space complexity because it creates a dictionary that counts the presence of each char in text, which requires additional space proportional to the size of the input text.
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Function C - O(n^2) Quadratic space complexity because for each j of each i in range(n) the data structure grows, meaning it grows roughly with the square of the input. 
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Function D - O(1) Constant space complexity because it is only creating the variables total and num which only access one value at a time.
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


## Part 2 - Tradeoff Decision

# Time complexity - O(n) Linear time complexity
# Space complexity - O(n) Linear space complexity
def emails_set(emails):
    seen_emails = set()
    duplicate_emails = set()
    
    for email in emails:
        if email in seen_emails:
            duplicate_emails.add(email)
        else:
            seen_emails.add(email)
    return duplicate_emails


# Time complexity - O(n log n) Linearithmic time complexity
# Space complexity - O(n) Linear space complexity
def emails_list(emails):
    emails.sort() # O(n log n) time comlexity
    duplicate_emails = []
    for email in range(1, len(emails)):
        if emails[email] == emails[email -1]:
            duplicate_emails.append(emails[email])
    return duplicate_emails


# Tradeoff Questions:

# 4GB RAM? - emails_list, because emails_set is a bit more memory intensive because it stores the additional set. Because in this case we are low on memory, that needs to be the priority over speed.

# 64GB RAM? - emails_set, because we have much more memory to manage the additional set, and we are defaulting to prioritizing speed when memory isn't a constraint.

# test_set = ["test1@example.com", "test2@example.com", "test3@example.com", "test1@example.com"]
# print(emails_list(test_set))