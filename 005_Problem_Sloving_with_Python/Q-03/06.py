""" 
This function is supposed to
find the maximum number in a list.
"""

def find_max(nums):
    max_num = nums[0]
    
    for num in nums:
        if num > max_num:
            max_num = num
            
    return max_num

print(find_max([-2, -5, -12, -8]))