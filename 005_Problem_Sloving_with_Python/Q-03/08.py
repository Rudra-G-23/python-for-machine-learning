""" 
This function is supposed to check if a string is a palindrome
(A palindrome reads the same forward and backward)
"""

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

print(is_palindrome("madam"))