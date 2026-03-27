""" 
Write a Python function that takes a list
of numbers and returns the largest number
in the list without using max().
"""

def largest_number_in_list(nums):
    largest_nums = nums[0]
    for n in nums:
        if n > largest_nums:
            largest_nums = n
    return largest_nums


print(largest_number_in_list([11, 3, 4, 5, 8]))
print(largest_number_in_list([1, 2, 3, ]))
print(largest_number_in_list([10, -5, 5]))