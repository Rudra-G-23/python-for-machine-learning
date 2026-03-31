""" 
Write a function named group_numbers_by_digits
that takes a list of integers and groups them
by number of digits.
"""

def group_numbers_by_digits(nums):
    if not nums:
        return {}
    
    result = {}
    for n in nums:
        count = len(str(n))
        if count in result:
            result[count].append(n)
        else:
            result[count] = [n]
    return result
        

print(group_numbers_by_digits([1, 22, 333, 4, 55, 6666]))
# {1: [1, 4], 2: [22, 55], 3: [333], 4: [6666]}

print(group_numbers_by_digits([]))
# {}

print(group_numbers_by_digits(None))
# {}