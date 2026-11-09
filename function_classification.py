## Part 1 - Function Classification

# Function A
# Classification: O(1) [Constant Time] - it's pulling the first value in the data index no matter how large that index is, so the number of operations stays the same.
def get_first(data):
    return data[0]

# Function B
# Classification: O(n) [Linear Time] - it's going through all of the data one time and adding a count where the data item is a target. So this would scale linearly with additional inputs. If you have 10x as many data inputs, it takes roughly 10x as long. 
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count

# Function C
# Classification: O(n^2) [Quadratic Time] - this is a case of nested loops, where for each i in data, it's compared to every other value and appended as pairs. If you go from 100 to 1000 inputs, you go from roughly 10,000 comparisons to 1,000,000 comparisons. The operations roughly quadruple with additional inputs.
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs

# Function D
# Classification: O(log n) [Logarithmic Time] - it takes n and counts how many times it halves n before getting down to 1. Because each step halves n, doubling the input only increases the number of while loop iterations and count increases by one each.
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# Function E
# Classification: O(n log n) [Linearithmic Time] - When adding the costs of the three lines (O(n) + O(n log n) + O(1)), the sort grows fastest as the input gets large, so it dominates and the other terms are dropped.
## From my research, it seems that Big O prioritizes telling you the shape of the growth as it gets large, which is why we would give this a coarse grain classification. 
def process(data):
    total = sum(data)           # Classification: O(n) [Linear Time] - it goes through each data input and adds them together, scaling linearly.
    sorted_data = sorted(data)  # Classification: O(n log n) [Linearithmic Time] - the sorting function will split the list in half repeatedly, which can only happen log n times. When merging those back together, each of n is handled at each merging level until the entire list is merged and sorted. So, the operations are n by log n. 
    first = data[0]             # Classification: O(1) [Constant Time] - it's pulling the first value in the data index no matter how large that index is, so the number of operations stays the same.
    return total, sorted_data, first

## Part 2 - Benchmarked Functions

import time
import random

def count_pairs(data): # Quadratic
    pair_count = 0
    target = 22
    for i in range(len(data)):
        for j in range(i + 1, len(data)): # loops through and compares all remaining j to each i in the dataadding to the pair count if any i and j are equal to the target
            if data[i] + data[j] == target: # adds to the pair count if any i and j are equal to the target
                pair_count += 1
    return pair_count


def count_dict_pairs(data): # Linear
    seen = {} # capture kv pair (seen:frequency) in dictionary
    pair_count = 0
    target = 22

    for i in data:
        complement = target - i # isolate complementary numbers for creation of target sum pairs

        if complement in seen:
            pair_count += seen[complement] # count the occurances of complement in seen dict and add those to pair count

        seen[i] = seen.get(i, 0) +1 # retrieve value for key from seen dict with default value of 0. Add 1 to that number and store any new values in the seen dict.
    return pair_count


def benchmark(func, data):
    """Time how long a function takes to run."""
    start = time.time()
    result = func(data)
    end = time.time()
    return end - start

# Generate test data with no duplicates (worst case — must check everything)
sizes = [1000, 5000, 10000]

for size in sizes:
    data = list(range(size))        # No duplicates — forces full scan
    random.shuffle(data)            # Randomize order

    t1 = benchmark(count_pairs, data)
    t2 = benchmark(count_dict_pairs, data)

    print(f"n={size:>6}  |  Quadratic: {t1:.4f}s  |  Linear: {t2:.4f}s")

# Benchmark Output:
# n=  1000  |  Quadratic: 0.0431s  |  Linear: 0.0002s
# n=  5000  |  Quadratic: 1.1765s  |  Linear: 0.0010s
# n= 10000  |  Quadratic: 4.0015s  |  Linear: 0.0017s