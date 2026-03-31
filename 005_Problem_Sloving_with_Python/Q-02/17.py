""" 
Write a function named reverse_list
that reverses a list without using 
.reverse().
"""

def reverse_list(nums):
    return nums[::-1]

print(reverse_list([1, 2, 3, 4])) # [4, 3, 2, 1]
print(reverse_list([])) # []
print(reverse_list([5])) # [5]
