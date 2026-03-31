""" 
Write a function named has_duplicates that
returns True if a list contains any duplicate
values, otherwise False.
"""
# M1
def has_duplicates(nums):
    if not nums:
        return False
    unique = []

    for w in nums:
        if w not in unique:
            unique.append(w)
    
    return nums != unique

# M2
def has_duplicates(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

print(has_duplicates([1, 2, 3, 4])) # False
print(has_duplicates([1, 2, 3, 2])) # True
print(has_duplicates([])) # False
print(has_duplicates([5])) # False
