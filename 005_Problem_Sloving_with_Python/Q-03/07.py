""" 
This function is supposed to reverse a string.
Don't used the slicing [::-1]
"""

def reverse_string(s):
    
    result = ""
    
    for i in range(len(s)-1, -1, -1):
        
        result = result + s[i]
        
    return result

print(reverse_string("hello"))