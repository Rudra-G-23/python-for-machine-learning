""" 
Write a function named is_sorted_ascending 
that takes a list of numbers and returns
True if the list is sorted in ascending order,
otherwise False.
"""

def is_sorted_ascending(nums):
    if not nums:
        return True
    
    sort_nums = sorted(nums)
    return nums == sort_nums

print(is_sorted_ascending([1, 2, 3, 4])) # True
print(is_sorted_ascending([1, 3, 2])) # False
print(is_sorted_ascending([])) # True
print(is_sorted_ascending([5])) # True
