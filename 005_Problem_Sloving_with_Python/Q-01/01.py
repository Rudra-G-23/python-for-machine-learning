""" 
Write a Python function that takes a list
of numbers and returns the largest number
in the list without using max().
"""

def largest_number_in_list(nums):
    largest_nums = nums[0]
    for i in range(len(nums)):

        if largest_nums > nums[i]:
            largest_nums = nums[i]
    return nums[i]

print(largest_number_in_list([11, 3, 4, 5, 8]))
print(largest_number_in_list([1, 2, 3, ]))
print(largest_number_in_list([10, -5, 5]))