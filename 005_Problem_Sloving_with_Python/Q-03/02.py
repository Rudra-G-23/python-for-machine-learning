""" 
Write a function named is_balanced_parenthese
that checks if a string of parentheses is balanced.

Rules
- Every ( must have a matching )
- Closing brackets must come after opening ones

Stack style thinking+
"""

def is_balanced_parentheses(text):
    count = 0
    
    for ch in text:
        if ch == "(":
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    
    return count == 0
                

print(is_balanced_parentheses("(()())")) # True
print(is_balanced_parentheses("(()")) # False
print(is_balanced_parentheses(")(")) # False
print(is_balanced_parentheses("")) # True
