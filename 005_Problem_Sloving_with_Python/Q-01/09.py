""" 
Write a function named group_by_length
that takes a list of words and returns
a dictionary where:

- the key is the word length
- the value is a list of words of that length
"""

def group_by_length(words):
    if not words:
       return {}
    
    count = {}
    
    for w in words:
        l = len(w)
        if l in count:
            count[l].append(w)
        else:
            count[l] = [w]
            
    return count

print(group_by_length(["hi", "hy", "hello", "hey", "a"]))
# Expected output: {2: ["hi", "hy"], 5: ['hello'], 3: ['hey'], 1: ['a']}

print(group_by_length([]))
# Expected output: {}

print(group_by_length(None))
# Expected output: {}
