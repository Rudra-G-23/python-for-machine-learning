# Python Basic

## 1. Python Output

!!! abstract "Python Output"

    === "Hello World"
        ```py title="Say hello to world" linenums="1" 
        print("Hello Data Points") 
        ```
    === "Your Name"
        ```py title="Your Name" linenums="1" 
        print("Rudra")
        ```
    === "Number"
        ```py title="Number" linenums="1" 
        print(7)
        ```
    === "Decimal"
        ```py title="Decimal" linenums="1" 
        print(3.3)
        ```
    === "Boolean"
        ```py title="Boolean" linenums="1" 
        print(True)
        ```
    === "Text"
        ```py title="Bunch of Text" linenums="1" 
        print("India", 7, 4.5, False, True, "z")
        ```

---

!!! info "Print Parameter"

    === "sep"
        ```py title="`sep`" linenums="1" 
        print("India", 7, 4.5, False, True, "z", sep="|")
        ```
        ```py title="`sep` Output" linenums="1" 
        India|7|4.5|False|True|z
        ```

    === "end"
        
        ??? example "Example 1"

            ```py title="end" linenums="1" 
            # Defalut is '\n'
            print('hello')
            print('world')
            ```
            ```py title="next line" linenums="1" 
            print('Hello \nWorld')
            ```
            ```py title="Output" linenums="1" 
            # Both output is the same
            hello
            world
            ```

        ??? example "Example 2"
        
            ```py title="`end`" linenums="1" 
            print('hello', end='---')
            print('world')
            ```
            ```py title="--- output" linenums="1" 
            hello-world
            ```
---

## 2. Data Types

!!! info "Data Type"

    === "Integer"
        ```py title="Integer" linenums="1" 
        print(8)
        print(1e309)
        ```
        ```py title="Output" linenums="1" 
        8
        inf
        ```

    === "Decimal/Float"
        ```py title="Decimal/Float" linenums="1" 
        print(8.55)
        print(1.7e309)
        ```
        ```py title="Output" linenums="1" 
        8.55
        inf
        ```

    === "Boolean"

        ```py title="Boolean" linenums="1"
        print(True)
        print(False) 
        ```
        ```py title="Output" linenums="1" 
        True
        False
        ```

    === "String"
        ```py title="String" linenums="1" 
        print('Hello World')
        ```
        ```py title="Output" linenums="1" 
        Hello World
        ```

    === "Complex"
        
        ```py title="" linenums="1" 
        print(5+6j)
        ```
        ```py title="Output" linenums="1" 
        (5+6j)
        ```

    === "List"

        ```py title="List" linenums="1" 
        print([1,2,3,4,5])
        ```
        ```py title="Output" linenums="1" 
        [1,2,3,4,5]
        ```

    === "Tuple"
        
        ```py title="Tuple" linenums="1" 
        print( (1, 2, 3, 4, 5) )
        ```
        ```py title="Output" linenums="1" 
        (1, 2, 3, 4, 5)
        ```

    === "Sets"
        ```py title="Sets" linenums="1" 
        print({1,2,3,4,5})
        ```
        ```py title="Output" linenums="1" 
        {1,2,3,4,5}
        ```

    === "Dictionary"

        ```py title="Dictionary" linenums="1" 
        print({'name':'Rudra', 'gender':'Male', 'weight':65})
        ```
        ```py title="Output" linenums="1" 
        {'name':'Rudra', 'gender':'Male', 'weight':65}
        ```
    === "Check Data Type"

        ```py title="Type" linenums="1" 
        type([12, 3, 4])
        ```
        ```py title="Output" linenums="1" 
        list
        ```

---

## 3. Variables

!!! info Variables

    === "Static"
        ```py title="Variables" linenums="1" 
        name = "Rudra"
        print(name)

        a = 5
        b = 6

        print(a + b)
        ```
        ```py title="Output" linenums="1" 
        Rudra
        11
        ```
    
    === "Dynamic"
        ```py title="Dynamic Typing" linenums="1" 
        a = 5
        a = 10
        a = 15
        ```
        ```py title="Output" linenums="1" 
        15
        ```

        ```py title="Dynamic" linenums="1" 
        a = 5
        b = 2
        c = 5

        print(a + b + c)
        ```
        ```py title="Output" linenums="1" 
        15
        5 5 5
        ```

---

## 4. Comments

!!! info "Comments"
    
    === "Single Line"

        ```py title="Single Line Comment" linenums="1" 
        # This is single line comment
        ```
        ```py title="Output" linenums="1" 
        ```

    === "Multi Line"
        
        ```py title="Multiline Comment" linenums="1"
        '''
        This
        is 
        multi line
        comment
        '''

        """
        This
        is 
        multiline
        comment
        """
        ```
        ```py title="Output" linenums="1" 
        ```

---

## 5. Keywords & Identifiers

!!! info "Keywords"

    ```py title="Keyword" linenums="1" 
    import keyword
    print(keyword.kwlist)
    ```
    ```py title="Output" linenums="1" 
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield']
    ```

!!! tip "Identifiers"

    - [X] You can't start with a digit
    - [X] You can't use underscore
    - [X] You can't use special Symbols

---

## 6. User Input

!!! info "Input"

    ```py title="" linenums="1" 
    # Take input from user and store them in a variable
    fnum = input('enter first number :')
    snum = input('enter second number :')

    # add tow variables
    result = int(fnum) + int(snum)

    # print the result
    print(result)

    print(type(fnum))
    # it doesn't change the original data type
    ```
    ```py title="Output" linenums="1" 
    9
    <class 'str'> 
    ```

---

## 7. Type Conversion

- **Implicit** Type Conversion: This is done automatically by Python.

- **Explicit** Type Conversion: This is done by the programmer using predefined functions

!!! info "Conversion Type"

    === "Implicit"
        ```py title="Implicit" linenums="1" 
        # implicit
        print(5+5.6)
        print(type(5), type(5.6))
        type(5+5.6)
        ```
        ```py title="Output" linenums="1" 
        10.6
        <class 'int'> <class 'float'>
        float
        ```

        ```py title="Error" linenums="1" 
        print(4 + '4') # this show an error
        ```

        ```py title="Output" linenums="1"
        ----> 1 print(4 + '4') 

        TypeError: unsupported operand type(s) for +: 'int' and 'str' 
        ```

    === "Explicit"

    ```py title="" linenums="1" 
    # Explicit
    # str -> int
    print(type(int('4')))

    # float -> int
    print(int(4.5))

    # int -> float
    print(float(4))
    ```

---

## 8. Literals

!!! info "Literals"
    
    === "All Digits"

        ```py title="" linenums="1" 
        # integer
        a = 0b1010 # Binary Literals
        b = 100 # Decimal Literal
        c = 0o310 # Octal Literal
        d = 0x12c # Hexadecimal Literal

        #float Literal
        float_1 = 10.5
        float_2 = 1.5e2 #1.5 * 1o^2  --> Very big
        float_3 = 1.5e-3 #1.5 * 1o^-3 -->Very small

        # complex Literal
        x = 3.14j

        print(a, b, c, d)
        print(float_1, float_2, float_3)
        print(x, x.imag, x.real)
        ```
        ```py title="Output" linenums="1" 
        10 100 200 300
        10.5 150.0 0.0015
        3.14j 3.14 0.0
        ```

    === "String"
            
        ```py title="" linenums="1" 
        string = 'This is Python' # single quotation
        strings = "This is Python" # double quotation

        char = 'Python'
        multieple_line = '''Hello Data Points'''
        raw_str = r"raw \n string"

        unicode = u"\U0001F642\u2764\U0001F606"

        print(string)
        print(strings)
        print(char)
        print(multieple_line)
        print(raw_str)
        print(unicode)
        ```
        ```py title="Output" linenums="1" 
        This is Python
        This is Python
        Python
        Hello Data Points
        raw \n string
        🙂❤😆
        ```

    === "Unicode"

        ```py title="" linenums="1" 
        # Unicode characters

        smile = "\U0001F642"  # 🙂
        laugh = "\U0001F602"  # 😂
        laughing = "\U0001F606"  # 😆
        clapping = "\U0001F44F"  # 👏
        dancing = "\U0001F483"  # 💃
        heart = "\u2764"  # ❤️

        print("Smile:", smile)
        print("Laugh:", laugh)
        print("Laughing:", laughing)
        print("Clapping:", clapping)
        print("Dancing:", dancing)
        print("Heart:", heart)
        ```
        ```py title="Output" linenums="1" 
        Smile: 🙂
        Laugh: 😂
        Laughing: 😆
        Clapping: 👏
        Dancing: 💃
        Heart: ❤
        ```

    === "Others"
            
        ```py title="" linenums="1" 
        # internal python think True = 1 & False = 0

        a = True + 4
        b = False + 10

        print("a:", a)
        print("b:", b)
        ```
        ```py title="Output" linenums="1" 
        a: 5
        b: 10
        ```

        ```py title="" linenums="1" 
        R = None
        print(R)
        ```
        ```py title="Output" linenums="1" 
        None
        ```

---