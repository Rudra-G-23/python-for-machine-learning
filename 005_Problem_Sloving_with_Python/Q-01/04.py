""" 
Write a Python function named count_vowels
that takes a string and returns the number
of vowels (a, e, i, o, u) in it.
Uppercase and lowercase both count.
"""

# M1
def count_vowels(text):
    count = 0
    for t in text.lower():
        if t in ['a', 'e', 'i', 'o', 'u']:
            count+=1

    return count

# M2
def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

print(count_vowels("hello")) # 2
print(count_vowels("PYTHON")) # 1
print(count_vowels("bcdfg")) # 0