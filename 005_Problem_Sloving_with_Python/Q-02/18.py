""" 
Write a function named running_sum that
returns a list where each element is the
sum of all previous elements including itself.
"""

def running_sum(nums):
    new_list = []
    total = 0
    for n in nums:
        total += n
        new_list.append(total)
    return new_list

print(running_sum([1, 2, 3, 4])) # [1, 3, 6, 10]
print(running_sum([])) # []
print(running_sum([5])) # [5]
