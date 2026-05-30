""" 
Write a function named first_non_repeating_char
that returns the first character that does not
repeat in a string. Return None if none exists.
"""

def first_non_repeating_char(text):
    ch_dict = {}
    
    for ch in text:
        if ch in ch_dict:
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 1
    
    for ch in text:
        if ch_dict[ch] == 1:
            return ch
 
    return None
    

print(first_non_repeating_char("swiss")) # 'w'
print(first_non_repeating_char("aabbcc")) # None
print(first_non_repeating_char("")) # None
