""" 
Write a function named second_largest that returns
the second largest number in a list.

- Do not use sorted()
- Assume the list has at least two distinct numbers
"""

def second_largest(nums):
    first = float('-inf')
    second = float('-inf')
    
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n < first and n > second:
            second = n
            
    return first, second

print(second_largest([10, 5, 20, 8])) # 10
print(second_largest([1, 2, 3, 4])) # 3
print(second_largest([5, 5, 3, 2, 5])) # 3