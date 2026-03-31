""" 
Write a function named group_even_odd that
takes a list of integers and returns:
{
  "even": [...],
  "odd": [...]
}

"""
def group_even_odd(nums):
    even_odd_dict = {"even": [], "odd": []}
    
    if not nums:
        return even_odd_dict
    
    for n in nums:
        if n %2 == 0:
            even_odd_dict['even'].append(n)
        else:
            even_odd_dict['odd'].append(n)
    
    return even_odd_dict
    
print(group_even_odd([1, 2, 3, 4, 5, 6]))
# {'even': [2, 4, 6], 'odd': [1, 3, 5]}

print(group_even_odd([]))
# {'even': [], 'odd': []}
