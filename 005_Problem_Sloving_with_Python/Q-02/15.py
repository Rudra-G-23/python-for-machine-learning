""" 
Write a function named square_even_numbers
that takes a list of numbers and returns a
new list containing the square of only the
even numbers.
"""

def square_even_numbers(nums):
    if not nums:
        return []
    
    even_list = []
    
    for n in nums:
        if n % 2 == 0:
            nn = n** 2
            even_list.append(nn)

    return even_list


print(square_even_numbers([1, 2, 3, 4, 5]))
# [4, 16]

print(square_even_numbers([]))
# []

print(square_even_numbers([1, 3, 5]))
# []
