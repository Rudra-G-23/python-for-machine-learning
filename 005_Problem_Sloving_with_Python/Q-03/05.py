""" 
You are given a function that is
supposed to count the frequency of
each element in a list.
"""

def count_frequency(nums):
    freq = {}
    
    for i in range(len(nums)):
        if nums[i] in freq:          
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    
    return freq

print(count_frequency([1, 2, 2, 3, 1, 1]))