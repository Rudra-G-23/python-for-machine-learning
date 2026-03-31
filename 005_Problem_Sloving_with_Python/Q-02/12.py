""" 
Write a function named group_words_by_vowel_start 
that takes a list of words and groups them 
into two lists:

{
  "vowel": [...],
  "consonant": [...]
}

"""

def group_words_by_vowel_start(words):
    result = {"vowel": [], "consonant": []}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    if not words:
        return result
    
    for w in words:
        first_char  = w[0].lower()
        if first_char  in vowels:
            result['vowel'].append(w)
        else:
            result['consonant'].append(w)
    
    return result

print(group_words_by_vowel_start(["apple", "banana", "orange", "grape", "umbrella"]))
# {'vowel': ['apple', 'orange', 'umbrella'], 'consonant': ['banana', 'grape']}

print(group_words_by_vowel_start([]))
# {'vowel': [], 'consonant': []}

print(group_words_by_vowel_start(None))
# {'vowel': [], 'consonant': []}
