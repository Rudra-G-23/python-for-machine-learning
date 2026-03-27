""" 
Write a function named count_positive_negative
that takes a list of numbers and returns a
dictionary with counts of positive, negative,
and zero numbers.
"""

def count_positive_negative(nums):
    count = {"positive": 0, "negative": 0, "zero": 0}

    if nums is None:
        return count
    
    for n in nums:
        if n > 0:
            count["positive"] += 1
        elif n < 0:
            count["negative"] += 1
        else:
            count["zero"] +=1
    
    return count
        

print(count_positive_negative([1, -2, 0, 3, -1, 0]))
# Expected output: {'positive': 2, 'negative': 2, 'zero': 2}

print(count_positive_negative([]))
# Expected output: {'positive': 0, 'negative': 0, 'zero': 0}
