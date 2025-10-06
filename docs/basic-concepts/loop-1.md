# Loops

## Operators


- [ ] Add All kinds of operations charts or table

!!! info "Operators"

    === "Arithmetic"
    
        ```py title="Arithmetic" linenums="1"
        # Arithmetic Operators

        print(5 + 2)
        print(10 - 3)
        print(4 * 6)
        print(15 / 4)
        print(15 // 4)
        print(15 % 4)
        print(2 ** 3)
        ```
        ```py title="Output" linenums="1" 
        7
        7
        24
        3.75
        3
        3
        8
        ```

    === "Rational"
            
        ```py title="Rational" linenums="1"
        # Rational Operators

        print(5 == 9)

        print(5 != 3)

        print(8 > 3)

        print(2 < 7)

        print(6 >= 5)

        print(4 <= 7)
        ```
        ```py title="Output" linenums="1" 
        False
        True
        True
        True
        True
        True
        ```

    === "Logical"
            
        ```py title="Logical" linenums="1"
        # Logic Operators

        print( 1 and 0)

        print(1 or 0)

        print(not 1)
        ```
        ```py title="Output" linenums="1" 
        0
        1
        False
        ```

    === "Bitwise"
            
        ```py title="Bitwise" linenums="1"
        # Bitwise Oprators -- it operate on binary code

        # bitwise and
        print(2 & 3)

        # bitwise or
        print(2 | 3)

        # bitwise xor
        # if both same then 1 otherwise 0
        print(2 ^ 3)

        print(~2)

        print(2 << 1)

        print(8 >> 1)
        ```
        ```py title="Output" linenums="1" 
        2
        3
        1
        -3
        4
        4
        ```

    === "Assign"

        ```py title="" linenums="1"
        # Assignment Operators

        x = 10

        # x = x + 2
        x += 5

        print(x)
        ```
        ```py title="Output" linenums="1" 
        15
        ```

    === "Membership"
            
        ```py title="Membership" linenums="1"
        # Membership Operators

        # in/not in
        print('d' in 'Odisha')
        print('d' not in 'Odisha', '\n')

        print(1 in [1,2,3])
        print(1 not in [1,2,3])
        ```
        ```py title="Output" linenums="1" 
        True
        False 

        True
        False
        ```


---

### if-else

!!! info "if-els"

    === "Program 1"

        ```py title="Program" linenums="1"
        input_email = input("Enter the email :")
        input_password = int(input("Enter Password :"))


        email = "rudra@gmail.com"
        password = 123

        if email == input_email and password == input_password:
            print("Welcome !")
        elif email != input_email or password != input_password:
            print("Incorrect ...")
        ```
        ```py title="Output" linenums="1" 
        ```

    === "Program 2"

        ```py title="Program: Smallest Number" linenums="1"
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))

        if a<b and a<c:
            print('Smallest num is a', a)
        elif b<a and b<c:
            print('Smallest num is b', b)
        else:
            print('Smallest num is c', c)
        ```
        ```py title="Output" linenums="1" 
        ```

---

### Modules

!!! info "Modules"

    === "Math"

        ```py title="" linenums="1"
        # Math

        import math

        print(math.sqrt(196))
        ```
        ```py title="Output" linenums="1" 
        14.0
        ```

    === "Keyword"

        ```py title="" linenums="1"
        import keyword
        print(keyword.kwlist)
        ```
        ```py title="Output" linenums="1" 
        ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
        ```

    === "Random"
            
        ```py title="" linenums="1"
        # random
        import random
        print(random.randint(1, 20)) # only one number it show 
        ```
        ```py title="Output" linenums="1" 
        4
        ```

    === "Date Time"
            
        ```py title="" linenums="1"
        # datetime

        import datetime
        print(datetime.datetime.now())
        ```
        ```py title="Output" linenums="1" 
        2025-10-04 17:17:30.227588
        ```

---

## While loops

!!! info "While loops"

    === "Ex 1"
        
        ```py title="" linenums="1"
        num = int(input('Enter the number :'))

        i = 1

        while i<11:
        print(num, '*', i, '=', num * i)
        i +=1
        ```
        ```py title="Output" linenums="1" 
        5 * 1 = 5
        5 * 2 = 10
        5 * 3 = 15
        5 * 4 = 20
        5 * 5 = 25
        5 * 6 = 30
        5 * 7 = 35
        5 * 8 = 40
        5 * 9 = 45
        5 * 10 = 50
        ```

    === "Ex 2"
            
        ```py title="While with else" linenums="1"
        # while with else

        x = 1

        while x < 10:
        print(x)
        x+=1

        else:
        print('Limit Crossed ...')
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        4
        5
        6
        7
        8
        9
        Limit Crossed ...
        ```

    === "Ex 3"
            
        ```py title="Guessing Game" linenums="1"
        import random
        jackpot = random.randint(1, 10)

        guess = int(input("Enter a number between (1 to 10):"))
        count = 1

        while guess != jackpot:
            if guess < jackpot:
                print(f"Your Number is {guess}, Guess Higher ...")
            else:
                print(f"Your Number is {guess}, Guess Lower ... ")
            
            guess = int(input("Enter the Number :"))
            count +=1

        print(f"\nActual Number is {guess}. 🥳")
        print(f"\nYou take {count} attempts")
        ```
        ```py title="Output" linenums="1" 
        Your Number is 3, Guess Higher ...
        Your Number is 4, Guess Higher ...
        Your Number is 5, Guess Higher ...
        Your Number is 6, Guess Higher ...
        Your Number is 7, Guess Higher ...

        Actual Number is 8. 🥳
        You took 6 attempts

        ```

## For Loops

!!! info "For loops"

    === "Ex 1"
            
        ```py title="" linenums="1"
        for i in 67, 2, 3:
            print(i)
        ```
        ```py title="Output" linenums="1" 
        67
        2
        3
        ```

    === "Ex 2"

        ```py title="" linenums="1"
        for i in range(1, 4):
            print(i)
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        ```

    === "Ex 3"
            
        ```py title="" linenums="1"
        for i in range (1, 11, 2): #(star, end , steps)
        print(i)
        ```
        ```py title="Output" linenums="1" 
        1
        3
        5
        7
        9
        ```

    === "Ex 4"
            
        ```py title="" linenums="1"
        for i in range (10, 1, -1):
        print(i)
        ```
        ```py title="Output" linenums="1"
        10
        9
        8
        7
        6
        5
        4
        3
        2
        ```

    === "Ex 5"
            
        ```py title="" linenums="1"
        for i in 'Odisha':
            print(i, end='-')
        ```
        ```py title="Output" linenums="1" 
        O-d-i-s-h-a-
        ```
---