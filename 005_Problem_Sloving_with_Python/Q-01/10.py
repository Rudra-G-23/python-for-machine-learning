""" 
Write a function named group_by_first_letter
that takes a list of words and groups them by
their first character.
"""

def group_by_first_letter(words:list) -> dict:
    if not words:
        return {}
    
    count_dict = {}

    for w in words:
        key = w[0]
        if key in count_dict:
            count_dict[key].append(w)
        else:
            count_dict[key] = [w]
    
    return count_dict

print(group_by_first_letter(["apple", "ant", "banana", "bat"]))
# Expected output: {'a': ['apple', 'ant'], 'b': ['banana', 'bat']}

print(group_by_first_letter([]))
# Expected output: {}

print(group_by_first_letter(None))
# Expected output: {}
