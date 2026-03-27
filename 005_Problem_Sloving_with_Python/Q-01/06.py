""" 
Write a Python function named word_count 
that takes a string and returns a dictionary
where the keys are words and the values are
how many times each word appears.
"""

def word_count(text):
    if not text:
        return {}
    
    words = text.lower().split(" ")
    counts = {}
    
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts
    

print(word_count("apple banana apple"))
# Expected output: {'apple': 2, 'banana': 1}

print(word_count("Python python PYTHON"))
# Expected output: {'python': 3}

print(word_count(""))
# Expected output: {}
