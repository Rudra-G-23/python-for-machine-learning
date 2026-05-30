""" 
Find the first non-repeating character in a string
Input:  "aabbcde"
Output: "c"
"""

def first_non_repeating_chr(chr):
    string_set = {}
    
    for i in chr:
        if i not in string_set:
            string_set[i] = 1
        else:
            string_set[i] += 1
            
    for i in chr:
        if string_set[i] == 1:
            return i
    
    return None

print(first_non_repeating_chr("aabbcde"))