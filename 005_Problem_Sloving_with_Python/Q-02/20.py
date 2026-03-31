""" 
Write a function named max_difference that returns
the maximum difference between two numbers in a list
such that the larger number comes after the smaller one
without using sort.
Ex-
max_difference([2, 3, 10, 6, 4, 8, 1]) # 8  (10 - 2)
"""

def max_difference(nums):
    min_so_far = nums[0]
    max_diff = nums[1] - nums[0]
    
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - min_so_far)
        min_so_far = min(nums[i], min_so_far)
    
    return max_diff

print(max_difference([2, 3, 10, 6, 4, 8, 1])) 
