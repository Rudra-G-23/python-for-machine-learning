## Lambda Function💡

!!! info "Lambda Functions"

    A **lambda function** is a small anonymous (nameless) function defined using the keyword `lambda`. It can take any number of arguments, but can only have **one expression**, which is implicitly returned. They are often used for small, single-operation tasks, especially when passed as arguments to higher-order functions.

    === "Ex 1: Square of a Number"
        Syntax: `lambda arguments: expression`
        ```py title="" linenums="1"
        # square

        sq = lambda x :x**2
        sq(5)
        ```
        ```py title="Output" linenums="1"
        25
        ```
    === "Ex 2: Addition of Two Numbers"
        Lambda functions can take multiple arguments.
        ```py title="" linenums="1"
        # x,y -> x+y
        a = lambda x,y:x+y
        a(5,2)
        ```
        ```py title="Output" linenums="1"
        7
        ```
    === "Ex 3: Check for Character"
        The expression is evaluated and returned.
        ```py title="" linenums="1"
        # check if a string has 'a'

        a = lambda s : 'a' in s
        a('hello')
        ```
        ```py title="Output" linenums="1"
        False
        ```
    === "Ex 4: Simple `is_even`"
        Returns a boolean result.
        ```py title="" linenums="1"
        # is_even

        is_even = lambda x : x%2==0
        is_even(5)
        ```
        ```py title="Output" linenums="1"
        False
        ```
    === "Ex 5: Conditional Expression"
        Lambda functions support conditional expressions (ternary operators).
        ```py title="" linenums="1"
        is_even = lambda x :'even' if x%2==0 else 'odd'
        is_even(5)
        ```
        ```py title="Output" linenums="1"
        'odd'
        ```


-----

## Higher Order Function ⬆️

!!! info "Higher Order Function"
    A **Higher Order Function (HOF)** is a function that either takes one or more functions as arguments or returns a function as its result. `map`, `filter`, and `reduce` are common HOFs.

    === "Custom `my_map` HOF Example"
        This custom function demonstrates a basic higher-order function that takes another function (`func`) and a list (`arg_list`) as input.
        ```py title="" linenums="1"
        def square(x):
            return x**2

        def cube(x):
            return x**3

        def my_map(func,arg_list): # my_map is a HOF
            result = []
            for i in arg_list:
                result.append(func(i))
            return result
        ```
        ```py title="Output" linenums="1"
        ```

---

### Map

The **`map()` function** applies a given function to all items in an input list (or other iterable) and returns a map object (which can be converted to a list).

**Syntax**: `map(function, iterable)`

??? example "Mapping Examples"

    === "Ex 1: Squaring using a Defined Function"
        ```py title="" linenums="1"
        # square the items of a list
        def square(x):
            return x**2

        list(map(square,[1,2,3,4,5]))
        ```
        ```py title="Output" linenums="1"
        [1, 4, 9, 16, 25]
        ```
    === "Ex 2: Squaring using a Lambda Function"
        ```py title="" linenums="1"
        list(map(lambda x:x**2, [1,2,3,4,5]))
        ```
        ```py title="Output" linenums="1"
        [1, 4, 9, 16, 25]
        ```
    === "Ex 3: Conditional Mapping"
        ```py title="" linenums="1"
        # odd/even labelling of list items
        L = [1,2,3,4,5]
        list(map(lambda x:'even' if x%2 == 0 else 'odd',L))
        ```
        ```py title="Output" linenums="1"
        ['odd', 'even', 'odd', 'even', 'odd']
        ```
    === "Ex 4: Fetching Data from Dictionary List (Gender)"
        ```py title="" linenums="1"
        # fetch gender from a list of dict

        users = [
            { 'name':'Rahul', 'age':45, 'gender':'male' },
            { 'name':'Nitish', 'age':33, 'gender':'male' },
            { 'name':'Ankita', 'age':50, 'gender':'female' }
        ]

        list(map(lambda users:users['gender'],users))
        ```
        ```py title="Output" linenums="1"
        ['male', 'male', 'female']
        ```
    === "Ex 5: Fetching Age Data"
        ```py title="" linenums="1"
        users = [
            { 'name':'Rahul', 'age':45, 'gender':'male' },
            { 'name':'Nitish', 'age':33, 'gender':'male' },
            { 'name':'Ankita', 'age':50, 'gender':'female' }
        ]
        list(map(lambda users: users['age'], users))
        ```
        ```py title="Output" linenums="1"
        [45, 33, 50]
        ```

---

### Filter

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

**Syntax**: `filter(function, iterable)`

??? example "Filtering Examples"
    === "Ex 1: Numbers Greater Than 5"
        ```py title="" linenums="1"
        # numbers greater than 5
        L = [3,4,5,6,7]
        list(filter(lambda x:x>5,L))
        ```
        ```py title="Output" linenums="1"
        [6, 7]
        ```
    === "Ex 2: Filtering Strings by Prefix"
        ```py title="" linenums="1"
        # fetch fruits starting with 'a'
        fruits = ['apple','guava','cherry']

        list(filter(lambda x:x.startswith('a'),fruits))
        ```
        ```py title="Output" linenums="1"
        ['apple']
        ```


### Reduce

The `reduce()` function applies a function cumulatively to the items of an iterable, reducing the iterable to a single value. It is located in the `functools` module.

**Syntax**: `functools.reduce(function, iterable)`

??? example "Reduce Examples"
    === "Ex 1: Sum of All Items"
        Accumulates the sum: `( ( (1+2)+3 )+4 )+5`
        ```py title="" linenums="1"
        # sum of all item
        import functools
        functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
        ```
        ```py title="Output" linenums="1"
        15
        ```

    === "Ex 2: Finding Maximum Value"

        The lambda function returns the greater of the two values being compared at each step, accumulating the maximum value.
        ```py title="" linenums="1"
        # find max (The example in the prompt is titled 'find min' but the lambda x if x>y else y finds the max)
        import functools

        functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1])
        ```
        ```py title="Output" linenums="1"
        45
        ```
---