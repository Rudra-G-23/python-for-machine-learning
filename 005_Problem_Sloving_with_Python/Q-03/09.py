""" 
Write a function to remove duplicates
from a list WITHOUT using set()
Input:  [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]
"""

def remove_duplicates(list):
    new_list = []
    
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 2, 3, 4, 1, 4]))

# Method 2

def remove_duplicates(nums):
    seen = {}
    result = []
    
    for num in nums:
        if num not in seen:
            seen[num] = True
            result.append(num)
            
    return seen, result

print(remove_duplicates([1, 2, 3, 4, 1, 4]))
