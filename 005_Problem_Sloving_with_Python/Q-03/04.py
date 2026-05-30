""" 
Rotate Left

Constraints:
- Do NOT use slicing (nums[a:b])
- Do NOT create a second full list
- Try to modify using loops
"""

def rotate_left(nums, k):

    for i in range(len(nums)):
        if i < k:
            nums.append(nums[i])
    for i in range(k-2):
        nums.pop(i)
            
    return nums

def rotate_left(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    
    k = k % n
    
    # Reverse first k
    reverse(nums, 0, k - 1)
    
    # Reverse rest
    reverse(nums, k, n - 1)
    
    # Reverse whole list
    reverse(nums, 0, n - 1)
    
    return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

print(rotate_left([1,2,3,4,5], 2)) # [3,4,5,1,2]
