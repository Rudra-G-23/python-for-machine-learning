""" 
Write a Python function named count_even_numbers 
that takes a list of integers as input and returns
the count of even numbers in the list.
Do not use count() or any built-in shortcuts.
"""

def count_even_numbers(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += 1
    return total

print(count_even_numbers([1, 2, 3, 4, 5, 6]))#  3
print(count_even_numbers([10, 20, 30])) # 3
print(count_even_numbers([1, 3, 5])) # 0
