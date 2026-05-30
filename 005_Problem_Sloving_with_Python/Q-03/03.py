""" 
Rotate List to the Right

Assumptions
- nums is a list of integers
- k is a non-negative integer
- If k is greater than length of list → handle it properly
- If list is empty → return empty list
- Do NOT use any external libraries

ex- 
nums = [1, 2, 3, 4, 5], k = 2 -> [4, 5, 1, 2, 3]
nums = [10, 20, 30], k = 4 -> [30, 10, 20]

"""

def rotate_right(nums, k):
    if not nums:
        return []
    
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([10, 20, 30], 4))
print(rotate_right([], 3))
