# String

## Creating

!!! info "Creating"

      ```py title="" linenums="1"
      a = 'Rudra1'
      print(a)

      b = "Rudra2"
      print(b)

      c = '''Rudra3'''
      print(c)
      ```
      ```py title="Output" linenums="1" 
      Rudra1
      Rudra2
      Rudra3
      ```

## Accessing Substrings

!!! info "Accessing"

    === "Positive Indexing"
         
        ```py title="" linenums="1"
        # Positive Indexing
        # in python counting start from the 0

        a = 'Hello World' 
        print(a[0])
        ```
        ```py title="Output" linenums="1"
        H 
        ```
    
    === "Negative Indexing"

        ```py title="" linenums="1"
        # Negative Indexing
        a = 'Hello World'
        print(a[-1])
        ```
        ```py title="Output" linenums="1" 
        d
        ```

    === "Slicing"
            
        ```py title="" linenums="1"
        #Slicing

        a = 'Hello World'
        print(a[0:6])
        ```
        ```py title="Output" linenums="1" 
        Hello
        ```

        ```py title="" linenums="1"
        # if you are use -ve indexing then the first number is > second number
            # 6 > 0

        a = 'Hello World'
        print(a[6:0:-2])
        ```
        ```py title="Output" linenums="1" 
        Wol
        ```

    === "Reversing"
            
        ```py title="" linenums="1"
        # Reverse the Line

        print(a[::-1])
        ```
        ```py title="Output" linenums="1" 
        dlroW olleH
        ```

## Editing & Deleting

!!! info "Editing"

      ```py title="" linenums="1"
      # python strings are immutable

      a = 'Hello World'
      a[0] = 'k'
      ```
      ```py title="Output" linenums="1" 
      1 # python strings are immutable
            3 a = 'Hello World'
      ----> 4 a[0] = 'k'

      TypeError: 'str' object does not support item assignment
      ```

!!! info "Deleting"

      ```py title="" linenums="1"
      # deleting
      s = 'Hello world'
      del s
      s
      ```
      ```py title="Output" linenums="1" 
      2 s = 'Hello world'
            3 del s
      ----> 4 print(s)
            5 s

      NameError: name 's' is not defined
      ```

      ```py title="" linenums="1"
      g = 'Hello'
      del g[1:3]
      ```
      ```py title="Output" linenums="1" 
      1 g = 'Hello'
      ----> 2 del g[1:3]

      TypeError: 'str' object does not support item deletion
      ```

## Operations

!!! info "Operations"

    === "Addition"

        ```py title="" linenums="1"
        print('Hello'+' '+'world')
        ```
        ```py title="Output" linenums="1" 
        Hello World
        ```

    === "Multiplication"

        ```py title="" linenums="1"
        print('Love_you_' * 5) # five times string 
        ```
        ```py title="Output" linenums="1" 
        Love_you_Love_you_Love_you_Love_you_Love_you_
        ```

        ```py title="" linenums="1"
        # we compare the word in lexicographically 

        'Delhi' != 'Odisha' # False
        'Delhi' > 'Odisha' # False
        'Delhi' and 'Odisha' # 'Odisha'
        'Delhi' or 'Odisha' # 'Delhi'
        '' and 'Odisha' # false and true -> false
        '' or 'Odisha' # Odisha
        not '' # empty is false --> True
        not 'Rudra' # value is True --> False
        ```
        ```py title="Output" linenums="1" 
        ```

---

## Functions

??? example "len"

    ```py title="" linenums="1"
    len('Rudra Prasad Bhuyan')
    ```
    ```py title="Output" linenums="1" 
    19
    ```
??? example "min"

    ```py title="" linenums="1"
    min('Rudra Prasad Bhuyan')
    ```
    ```py title="Output" linenums="1" 
    ' '
    ```

??? example "max"

    ```py title="" linenums="1"
    max('Rudra Prasad Bhuyan')
    ```
    ```py title="Output" linenums="1" 
    y
    ```

??? example "sorted"

    ```py title="" linenums="1"
    sorted('Rudra Prasad Bhuyan', reverse=True)
    ```
    ```py title="Output" linenums="1" 
    ['y',
    'u',
    'u',
    's',
    'r',
    'r',
    'n',
    'h',
    'd',
    'd',
    'a',
    'a',
    'a',
    'a',
    'R',
    'P',
    'B',
    ' ',
    ' ']
    ```

??? example "capitalize"
    ```py title="" linenums="1"
    a = 'Rudra prsad bhuyan'
    a.capitalize()
    ```
    ```py title="Output" linenums="1" 
    'Rudra prsad bhuyan'
    ```

??? example "title"

    ```py title="" linenums="1"
    a.title() # only first letter of the word is capital letter
    ```
    ```py title="Output" linenums="1" 
    'Rudra Prsad Bhuyan'
    ```

??? example "upper"

    ```py title="" linenums="1"
    a.upper()
    ```
    ```py title="Output" linenums="1" 
    'RUDRA PRSAD BHUYAN'
    ```
??? example "swapcase"
    ```py title="" linenums="1"
    'Rudra Prasad Bhuyan'.swapcase()
    ```
    ```py title="Output" linenums="1" 
    'rUDRA pRASAD bHUYAN'
    ```

??? example "lower"

    ```py title="" linenums="1"
    'Rudra Prasad Bhuyan'.lower()
    ```
    ```py title="Output" linenums="1" 
    'rudra prasad bhuyan'
    ```
??? example "count"

    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.count('a')
    ```
    ```py title="Output" linenums="1" 
    5
    ```

??? example "index"

    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.index('Rudra') 
    'My name is Rudra Prasad Bhuyan'.index('z')  # ValueError: substring not found

    # showing error if hte string iss not present  
    ```
    ```py title="Output" linenums="1" 
    11
    ```

??? example "endswith"

    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.endswith('z')
    ```
    ```py title="Output" linenums="1"
    False 
    ```

??? example "startswith"

    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.startswith('My')
    ```
    ```py title="Output" linenums="1" 
    True
    ```
    ??? example "format"
    ```py title="" linenums="1"
    name = 'Rudra'
    age = 20
    'My name is {} and my age is {}'.format(name, age)
    ```
    ```py title="Output" linenums="1" 
    'My name is Rudra and my age is 20'
    ```

??? example "isalnum"
    ```py title="" linenums="1"
    'Rudra_1234'.isalnum()
    ```
    ```py title="Output" linenums="1" 
    False
    ```
??? example "isalnum"
    ```py title="" linenums="1"
    'Rudra_1234$%'.isalnum()
    ```
    ```py title="Output" linenums="1" 
    False
    ```

??? example "title"

    ```py title="" linenums="1"
    'RUDRA'.isalpha()
    ```
    ```py title="Output" linenums="1" 
    True
    ```
??? example "isdigit"

    ```py title="" linenums="1"
    '1234'.isdigit()
    ```
    ```py title="Output" linenums="1" 
    True
    ```

??? example "isidentifier"
    ```py title="" linenums="1"
    'Rudra'.isidentifier()
    ```
    ```py title="Output" linenums="1" 
    True
    ```
??? example "split"
    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.split(sep=None)
    ```
    ```py title="Output" linenums="1" 
    ['My', 'name', 'is', 'Rudra', 'Prasad', 'Bhuyan']
    ```


    ```py title="" linenums="1"
    'My name is Rudra Prasad Bhuyan'.split('a')
    ```
    ```py title="Output" linenums="1" 
    ['My n', 'me is Rudr', ' Pr', 's', 'd Bhuy', 'n']
    ```
??? example "join"
    ```py title="" linenums="1"
    ' '.join(['My', 'name', 'is', 'Rudra', 'Prasad', 'Bhuyan'])
    ```
    ```py title="Output" linenums="1" 
    'My name is Rudra Prasad Bhuyan'
    ```


    ```py title="" linenums="1"
    ' ---'.join(['My', 'name', 'is', 'Rudra', 'Prasad', 'Bhuyan'])
    ```
    ```py title="Output" linenums="1" 
    'My ---name ---is ---Rudra ---Prasad ---Bhuyan'
    ```

    ```py title="" linenums="1"
    'My name is Rudra Bhuyan'.replace('Rudra', 'Nitesh')
    ```
    ```py title="Output" linenums="1" 
    'My name is Nitesh Bhuyan'
    ```

---