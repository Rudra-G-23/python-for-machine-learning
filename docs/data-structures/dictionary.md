# Dictionary

## Creating Dictionaries

!!! info "Dictionary Creation and Properties"
    Dictionaries are key-value pairs (mappings) that are **unordered** (in older Python versions) and **mutable**. Keys must be **immutable** and unique. Values can be of any type.

=== "Ex 1: Empty Dictionary vs. Empty Set"
    An empty dictionary is created using `{}`. Note that `set()` must be used for an empty set.
    ```py title="" linenums="1"
    # empty dict
    d = {}
    s = set()
    print(type(s))
    print(type(d))
    ```
    ```py title="Output" linenums="1"
    <class 'set'>
    <class 'dict'>
    ```

=== "Ex 2: 1D Dictionary"
    A simple dictionary with one level of key-value pairs.
    ```py title="" linenums="1"
    # 1D dictionary (homo/heterogeneous keys/values allowed)
    d1 = {1:'Rudra', 'gender':'male'}
    d1
    ```
    ```py title="Output" linenums="1"
    {1: 'Rudra', 'gender': 'male'}
    ```

=== "Ex 3: Nested Dictionary (2D/JSON-like)"
    Dictionaries can be nested, where a value in the main dictionary is itself another dictionary. This is often used to represent structured data (like JSON).
    ```py title="" linenums="1"
    # 2D --> nested dictionary (JSON-like structure)

    d = {
        'name' : 'Rudra',
        'gender' : 'male',
        'age' : 20,
        'address' : 'Odisha',
        'subjects':{
            'odia': 90,
            'english': 90,
            'maths': 98,
            'science': 99,
            'coding':89
        }
    }

    d
    ```
    ```py title="Output" linenums="1"
    {'name': 'Rudra',
     'gender': 'male',
     'age': 20,
     'address': 'Odisha',
     'subjects': {'odia': 90,
      'english': 90,
      'maths': 98,
      'science': 99,
      'coding': 89}}
    ```

=== "Ex 4: Using the `dict()` Constructor"
    You can create a dictionary using the `dict()` constructor by passing it an iterable of key-value pairs (e.g., a list of tuples).
    ```py title="" linenums="1"
    # type conversion from a list of tuples
    d = dict([(1,'rudra'), (3,'z')])
    d
    ```
    ```py title="Output" linenums="1"
    {1: 'rudra', 3: 'z'}
    ```

=== "Ex 5: Unique Keys Only"
    If duplicate keys are used, the dictionary only stores the entry associated with the **last occurrence** of that key.
    ```py title="" linenums="1"
    # no duplicated value (the key must be unique)
    d2 = {1:'rudra', 1:'rudra'}
    d2
    ```
    ```py title="Output" linenums="1"
    {1: 'rudra'}
    ```

=== "Ex 6: Keys Must be Immutable (Hashable)"
    Only **immutable** types (like integers, strings, and tuples) can be used as dictionary keys. Mutable types (like lists and sets) will cause a `TypeError`.
    ```py title="" linenums="1"
    # immutable keys are required (list is mutable)
    d3 = {[1,2,3] : 'rudra'}
    d3
    ```
    ```py title="Output" linenums="1"
    1 # immutable
    ----> 2 d3 = {[1,2,3] : 'rudra'}
          3 d3

    TypeError: unhashable type: 'list'
    ```


---

## Accessing 

!!! info "Accessing"

    ```py title="" linenums="1"
    d = {'a':1,'b':2,'c':3}

    # providing key
    d['a']

    # using get function
    d.get('a')
    ```
    ```py title="Output" linenums="1" 
    1
    ```

### Adding new key-value pair

!!! info "Adding"

    ```py title="" linenums="1"
    d5 = {'a':1,'b':2,'c':3}

    # add new
    d5['d'] = 4

    # add new key
    d5['age'] = 34
    d5
    ```
    ```py title="Output" linenums="1" 
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'age': 34}
    ```


    ```py title="" linenums="1"
    # 2d accessing 
    d['subjects'] = {'maths', 'Physic'}
    d
    ```
    ```py title="Output" linenums="1" 
    {'a': 1, 'b': 2, 'c': 3, 'subjects': {'Physic', 'maths'}, 'age': 23}
    ```

---

## Deleting Dictionary Items 🗑️

!!! info "Deleting Items"
    Python provides several methods for deleting items from a dictionary, including removing a specific key-value pair, removing the last inserted item, deleting a single item or the entire dictionary, and clearing all contents.


=== "Remove Specific Key (`.pop()`)"
    The `.pop(<key>)` method removes the item with the specified key and returns its value. It's often safer than `del` as it can return a default value if the key isn't found (if provided).
    ```py title="" linenums="1"
    d5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'age': 34} # Example initialization
    # pop the item with key 'a'
    d5.pop('a')
    d5
    ```
    ```py title="Output" linenums="1"
    {'b': 2, 'c': 3, 'd': 4, 'age': 34}
    ```

=== "Remove Last Inserted Item (`.popitem()`)"
    The `.popitem()` method removes and returns the **last inserted** key-value pair as a tuple. This behavior is guaranteed in Python 3.7+ (ordered dictionary guarantee).
    ```py title="" linenums="1"
    d5 = {'b': 2, 'c': 3, 'd': 4, 'age': 34} # Example continuation
    # last pair deleted (key 'age' was last inserted)
    d5.popitem()
    d5
    ```
    ```py title="Output" linenums="1"
    {'b': 2, 'c': 3, 'd': 4}
    ```

=== "Delete Specific Item (`del` keyword)"
    The `del` keyword can be used to remove a specific key-value pair from the dictionary by key. Using `del d5` removes the entire dictionary object itself.
    ```py title="" linenums="1"
    d5 = {'b': 2, 'c': 3, 'd': 4} # Example continuation
    # del whole pair or one
    # Delete the item with key 'b'
    del d5['b']
    d5
    ```
    ```py title="Output" linenums="1"
    {'c': 3, 'd': 4}
    ```

=== "Remove All Items (`.clear()`)"
    The `.clear()` method removes all elements from the dictionary, leaving it as an empty dictionary `{}`.
    ```py title="" linenums="1"
    d5 = {'c': 3, 'd': 4} # Example continuation
    # all deleted
    d5.clear()
    d5
    ```
    ```py title="Output" linenums="1"
    {}
    ```

---

## Editing

!!! info "Editing"

    ```py title="" linenums="1"
    d['age'] = 23
    d
    ```
    ```py title="Output" linenums="1" 
    {'a': 1, 'b': 2, 'c': 3, 'subjects': 'maths', 'age': 23}
    ```

## Operations

!!! info "Operations"

    ```py title="" linenums="1"
    # membership -> it work on keys only

    print ('gender' in d)
    print ('gender' not in d)
    ```
    ```py title="Output" linenums="1" 
    False
    True
    ```

    ```py title="" linenums="1"
    # iteration -> provide only keys
    # d[i] -> value
    for i in d:
      print(i, d[i])
    ```
    ```py title="Output" linenums="1" 
    a 1
    b 2
    c 3
    subjects maths
    age 23
    ```

---

## Dictionary Built-in Functions and Methods

??? example "Length and Sorting Keys (`len`, `sorted`)"
    The `len()` function returns the number of key-value pairs. The `sorted()` function returns a sorted **list** of the dictionary's **keys**.
    ```py title="" linenums="1"
    # Example dictionary (assumed from context where 'd' is defined)
    d = {'a': 1, 'b': 2, 'c': 3, 'subjects': 'maths', 'age': 23}

    # len / sorted
    print(len(d))
    print(sorted(d)) # it provides us in lists (of keys)
    ```
    ```py title="Output" linenums="1"
    5
    ['a', 'age', 'b', 'c', 'subjects']
    ```

??? example "Viewing Keys, Values, and Items (`.items()`, `.keys()`, `.values()`)"
    These methods return view objects that represent the dictionary's contents.
    ```py title="" linenums="1"
    # items/keys/values

    print(d.items())
    print(d.keys())
    print(d.values())
    ```
    ```py title="Output" linenums="1"
    dict_items([('a', 1), ('b', 2), ('c', 3), ('subjects', 'maths'), ('age', 23)])
    dict_keys(['a', 'b', 'c', 'subjects', 'age'])
    dict_values([1, 2, 3, 'maths', 23])
    ```

??? example "Merging Dictionaries (`.update()`)"
    The `.update()` method merges a second dictionary into the first. If keys overlap, the value from the second dictionary overwrites the value in the first.
    ```py title="" linenums="1"
    # update
    # see key 2: 'b' is overwritten by 'c'
    d1 = {1:'a', 2:'b'}
    d2 = {2:'c', 3:'d'}

    d1.update(d2)
    d1
    ```
    ```py title="Output" linenums="1"
    {1: 'a', 2: 'c', 3: 'd'}
    ```

---

## Dictionary Comprehension 📝

!!! abstract "Single Loop Comprehension"

    === "Ex 1: Squares of Numbers"
        Dictionary comprehension provides a concise way to create dictionaries.
        ```py title="" linenums="1"
        # print 1st 10 members and their squares

        {i: i**2 for i in range(1, 11)}
        ```
        ```py title="Output" linenums="1"
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
        ```
    === "Ex 2: Using `zip` for Mapping"
        Use `zip()` to pair elements from two lists and create a dictionary.
        ```py title="" linenums="1"
        # using zip
        days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
        temp = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

        {i:j for (i,j) in zip(days, temp)}
        ```
        ```py title="Output" linenums="1"
        {'sun': 30.5,
         'mon': 32.6,
         'tue': 31.8,
         'wed': 33.4,
         'thu': 29.8,
         'fri': 30.2,
         'sat': 29.9}
        ```
    === "Ex 3: Transforming Values"
        Iterate over existing key-value pairs and apply a transformation (e.g., converting distance from meters to miles approx. by raising to the power of 0.62).
        ```py title="" linenums="1"
        distance = {'odisha':2999,
                'puri' : 299,
                'j&k' :2183028
                }

        print(distance.items())
        {key: value**0.62 for (key, value) in distance.items()}
        ```
        ```py title="Output" linenums="1"
        dict_items([('odisha', 2999), ('puri', 299), ('j&k', 2183028)])

        {'odisha': 143.1282656510908,
         'puri': 34.270160370805556,
         'j&k': 8515.629735134355}
        ```

!!! abstract "Conditional and Nested Comprehension"

    === "Ex 4: Filtering with `if`"
        Add an `if` condition to the comprehension to filter items based on their value.
        ```py title="" linenums="1"
        # using if condition
        products = {'phone':10,
                    'laptop':0,
                    'charger':7,
                    'tablet':0
                    }

        {key:value for (key, value) in products.items() if value > 0}
        ```
        ```py title="Output" linenums="1"
        {'phone': 10, 'charger': 7}
        ```

    === "Ex 5: Nested (Power Table)"
        Nested dictionary comprehension to create a table where outer keys are bases and inner key-value pairs are powers.
        ```py title="" linenums="1"
        # table of cubes/powers through nested comprehension

        {i:{j:i**j for j in range(1, 11)} for i in range(2, 5)}
        ```
        ```py title="Output" linenums="1"
        {2: {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024},
         3: {1: 3,
          2: 9,
          3: 27,
          4: 81,
          5: 243,
          6: 729,
          7: 2187,
          8: 6561,
          9: 19683,
          10: 59049},
         4: {1: 4,
          2: 16,
          3: 64,
          4: 256,
          5: 1024,
          6: 4096,
          7: 16384,
          8: 65536,
          9: 262144,
          10: 1048576}}
        ```

    === "Ex 6: Nested (Multiplication Table)"
        Nested dictionary comprehension to create multiplication tables.
        ```py title="" linenums="1"
        # table through nested comprehension

        {i:{j:i*j for j in range(1, 11)} for i in range(2, 5)}
        ```
        ```py title="Output" linenums="1"
        {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20},
         3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27, 10: 30},
         4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20, 6: 24, 7: 28, 8: 32, 9: 36, 10: 40}}
        ```

---