""" 
Write a Python function named remove_duplicates
that takes a list and returns a new list with
duplicates removed while keeping the original order.
"""

# M1
def remove_duplicates(nums):
    unique_list = []
    for n in nums:
        if n not in unique_list:
            unique_list.append(n)
    return unique_list

# M2
def remove_duplicates(nums):
    seen = set()
    results = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            results.append(n)
    return results


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# Expected output: [1, 2, 3, 4]

print(remove_duplicates([5, 5, 5]))
# Expected output: [5]

print(remove_duplicates([]))
# Expected output: []
