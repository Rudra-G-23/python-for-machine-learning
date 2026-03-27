"""
Write a Python function named char_count
that takes a string and returns a dictionary
showing how many times each character appears
(ignore spaces).
"""

def char_count(text):
    
    if text is None:
        return {}
    
    counts = {}
    for w in text:
        if w == " ":
            continue
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

print(char_count("hello"))
# Expected output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(char_count("a a b"))
# Expected output: {'a': 2, 'b': 1}

print(char_count(""))
# Expected output: {}


# https://cscircles.cemc.uwaterloo.ca/visualize#mode=edit