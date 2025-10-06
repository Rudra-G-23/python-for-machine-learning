# Pattern

---

## Nested Loops

!!! info "Nested Loops"

    === "Sequence Sum"
    
        ```py title="Sequence Sum" linenums="1"
        # 1/1! + 2/2! + 3/3! ... nth
        n = int(input('Enter a number :\n'))
        print(f'Your Enter number is {n} \n')
        sum = 0
        fact = 1

        for i in range(1, n+1):
            fact = fact * i
            sum = sum + (i/fact)

        print(f'Your Total sum of this sequence is {sum}')    
        ```
        ```py title="Output" linenums="1" 
        Your Enter number is 5 

        Your Total sum of this sequence is 2.708333333333333
        ```
    
    === "Pairing"

        ```py title="" linenums="1"
        # pairing 

        for i in range (1, 3):
            for j in range (1, 5): 
                print(i, j)
        ```
        ```py title="Output" linenums="1" 
        1 1
        1 2
        1 3
        1 4
        2 1
        2 2
        2 3
        2 4
        ```

    === "Pattern 1"
    
        ```txt
        *`

        **`

        ***`

        ****`
        ```

        ```py title="" linenums="1"
        # user input 
        n = int(input('Enter the number of star you want : \n'))
        print(f'Your enter number is {n}\n')

        # loops
        for i in range(1, n+1):
            for j in range(1, i+1):
                print('*', end='')
            print()
        ```
        ```py title="Output" linenums="1" 
        Your enter number is 5

        *
        **
        ***
        ****
        *****
        ```

    === "Pattern 2"
            
        ```txt
        1

        121

        12321

        1234321
        ```
        ```py title="" linenums="1"
        # user input 
        n = int(input('Enter the number of star you want : \n'))
        print(f'Your enter number is {n}\n')

        # loops
        for i in range(1, n+1):
            for j in range (1, i+1):
                print(j, end='')
            for k in range(i-1, 0, -1):
                print(k, end='')
                
            print()
        ```
        ```py title="Output" linenums="1"
        Your enter number is 5

        1
        121
        12321
        1234321
        123454321 
        ```

---

## Loop Control Statement

### continue
!!! info "Control the Loop"

    === "Continue"

        ```py title="" linenums="1"
        # continue

        for i in range(1, 11):
          if i == 6:
            print('___ Which number is not in series')
            continue
          print(i)
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        4
        5
        ___ Which number is not in series
        7
        8
        9
        10
        ```

    === "Break"

        ```py title="" linenums="1"
        for i in range(1, 11):
          if i == 6:
            print('___ Which number is not in series')
            break
        ```
        ```py title="Output" linenums="1"
        ___ Which number is not in series 
        ```

        ```py title="" linenums="1"
        # continue

        for i in range(1, 11):
          if i == 6:
            print('___ Which number is not in series')
            break
          print(i)
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        4
        5
        ___ Which number is not in series
        ```

    === "Ex 1"
      
        ```py title="" linenums="1"
        # does primary number is ?

        lower_range = int(input('enter the Lower number :'))
        upper_range = int(input('enter the Lower number :'))
        print(f"Your Lower Range {lower_range}, Upper Range {upper_range}")
        for i in range(lower_range, upper_range+1):
            for j in range(2, i):
              if i % j == 0:
                  break
            else:
                print(i) 

        ```
        ```py title="Output" linenums="1" 
        Your Lower Range5, Upper Range 12
        5
        7
        11
        ```

    === "EX 2"
      
        ```py title="" linenums="1"
        # when using while and when using for in text

        # Use "while" when you want to loop based on a condition.
        # Example: Print numbers from 1 to 5
        count = 1
        while count <= 5:
          print(count)
          count += 1
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        4
        5
        ```

    === "Ex 3"
      
        ```py title="" linenums="1"
        # Use "for" when you want to iterate over a sequence (like a string).
        # Example: Print each character in a string
        text = "Hello"
        for char in text:
          print('\n',char)

        ```
        ```py title="Output" linenums="1" 
        H

        e

        l

        l

        o
        ```
---