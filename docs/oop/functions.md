# Functions

## Docstring 📝

!!! abstract "Junior Coder Docstring Style"
    [cite_start]A simple, descriptive docstring[cite: 147]. Note that the `is_even` function must be defined with this docstring for the subsequent `__doc__` example to work correctly.

    ```py title="" linenums="1"
    def is_even (num):
      """
      This function returns if a given number is even or odd.
      input - any valid integer
      output - boolean (True if even, False if odd)
      created on - Apr 2 2025
      """
      if type(num) == int :
        if num % 2 == 0:
          return 'Even'
        else:
          return 'Odd'
      else:
        return 'Read docstring ... go...'
    ```
    ```py title="Output" linenums="1"
    ```

!!! abstract "Senior Coder Docstring Style (Using Type Hinting and Standard Format)"
    [cite_start]A more structured docstring using **type hints** (`num: int -> str`) and a formal format (like NumPy or Google style), listing arguments and return values[cite: 147].

    ```py title="" linenums="1"
    def is_even(num: int) -> str :
        """
        Check given number is even or odd.

        Args:
            num (int): Any Valid Integer

        Returns:
            str: Even or Odd

        """
        if type(num) == int : # Function body added to make it callable
          if num % 2 == 0:
            return 'Even'
          else:
            return 'Odd'
        else:
          return 'Read docstring ... go...'
    ```
    ```py title="Output" linenums="1"
    ```

    ??? example "Calling the Function"
        Assuming the function definition from the first example is active in the environment.

        ```py title="" linenums="1"
        # call the function

        for i in range (0, 14):
          print (i, is_even(i))
        ```
        ```py title="Output" linenums="1"
        0 Even
        1 Odd
        2 Even
        3 Odd
        4 Even
        5 Odd
        6 Even
        7 Odd
        8 Even
        9 Odd
        10 Even
        11 Odd
        12 Even
        13 Odd
        ```

---

### Reading Docstrings (`.__doc__`)

??? example "Custom Docstring"
    [cite_start]Access the docstring using the special `.__doc__` attribute[cite: 147].

    ```py title="" linenums="1"
    print(is_even.__doc__)
    ```
    ```py title="Output" linenums="1"
    
     This function returns if a given number is even or odd.
     input - any valid integer
     output - boolean (True if even, False if odd)
     created on - Apr 2 2025
     
    ```

??? example "Docstring of Built-in `print()`"
    Built-in functions and objects also have docstrings.

    ```py title="" linenums="1"
    print(print.__doc__)
    ```
    ```py title="Output" linenums="1"
    Prints the values to a stream, or to sys.stdout by default.

     sep
       string inserted between values, default a space.
     end
       string appended after the last value, default a newline.
     file
       a file-like object (stream); defaults to the current sys.stdout.
     flush
       whether to forcibly flush the stream.
    ```

??? example "Docstring of Built-in `type()`"

    ```py title="" linenums="1"
    print(type.__doc__)
    ```
    ```py title="Output" linenums="1"
    type(object) -> the object's type
    type(name, bases, dict, **kwds) -> a new type
    ```

---

## Two Points of View: Responsibility

!!! tip "View"

  
    > Whenever you design a function, it is your responsibility to ensure
         that your code executes without any errors.


    - [X] **Junior Coder:** Focuses on writing the logic to pass the test cases.
    - [X] **Senior Coder:** Writes robust functions that include type checking (like in the first `is_even` example) and clear documentation (**docstrings**) to prevent misuse and runtime errors, reflecting code quality and reliability.

---

## Parameter vs Arguments 🤝

!!! info "Definitions"
    * **Parameters** are the names defined in the function signature (during function **creation time**).
    * **Arguments** are the actual values passed to the function when it is **called** (during function **use time**).

    ```py title="" linenums="1"
    # def func_name(parameter1, parameter2):  <- Parameters
    #     pass
    # func_name(argument1, argument2)        <- Arguments
    ```
    ```py title="Output" linenums="1"
    ```

---

### Default Argument
??? example "Default Argument"
    Parameters can be assigned a default value in the function definition. If no argument is provided for that parameter during the call, the default value is used.
    ```py title="" linenums="1"
    # default
    # if no value is provided, the default value (1) is used

    def power (a=1, b=1):
      return a**b

    power()
    ```
    ```py title="Output" linenums="1"
    1
    ```

### Positional Argument
??? example "Positional Argument"
    Arguments passed in the function call are mapped to parameters based on their **position** or order.
    ```py title="" linenums="1"
    # positional argument
    # order matters: 2 is assigned to 'a', 3 is assigned to 'b'

    power(2, 3)
    ```
    ```py title="Output" linenums="1"
    8
    ```

### Keyword Argument
??? example "Keyword Argument"
    Arguments are passed by explicitly naming the parameter they should correspond to. This allows the arguments to be specified in any order.
    ```py title="" linenums="1"
    # keyword
    # arguments are matched by name, ignoring position

    power(b=3, a=2)
    ```
    ```py title="Output" linenums="1"
    8
    ```

---

## `*args` & `**kwargs` 📦

The special Python keywords `*args` and `**kwargs` are used to pass a **variable length of arguments** to a function.

!!! info "Variable Positional Arguments (`*args`)"
    The `*args` syntax allows you to pass a variable number of **non-keyword arguments** (positional arguments) to a function. Inside the function, `args` (or whatever name you choose) is treated as a **tuple** containing all the passed non-keyword arguments.

    === "Function Definition"
        ```py title="" linenums="1"
        # *args (keyword 'kwargs' is used instead of convention 'args' to demonstrate flexibility)
        # allows us to pass a variable number of non-keyword arguments to a function.

        def multiply(*kwargs):
          product = 1

          for i in kwargs:
            product = product * i

          print(kwargs) # Prints the tuple of arguments
          return product
        ```
        ```py title="Output" linenums="1"
        ```
    === "Function Call"
        ```py title="" linenums="1"
        multiply(1, 2, 3, 4, 5, 6, 7, 8, 9)
        ```
        ```py title="Output" linenums="1"
        (1, 2, 3, 4, 5, 6, 7, 8, 9)
        362880
        ```

!!! info "Variable Keyword Arguments (`**kwargs`)"
    The `**kwargs` syntax allows you to pass any number of **keyword arguments** (key-value pairs) to a function. Inside the function, `kwargs` (or whatever name you choose) is treated as a **dictionary** containing all the passed keyword arguments.

    === "Function Definition"
        ```py title="" linenums="1"
        # **kwargs
        # **kwargs allows us to pass any number of keyword arguments.
        # Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

        def display(**kwargs):
          for (key,value) in kwargs.items():
            print(key,'->',value)

        ```
        ```py title="Output" linenums="1"
        ```
    === "Function Call"
        ```py title="" linenums="1"
        display(a=1, b=2, c=3)
        ```
        ```py title="Output" linenums="1"
        a -> 1
        b -> 2
        c -> 3
        ```

---

??? tip "Important Points to Remember"

    1.  **Order Matters**: If you use a combination of argument types, the order in the function signature must be:
        $$ \text{normal arguments} \rightarrow \text{positional args } (*\text{args}) \rightarrow \text{keyword args } (**\text{kwargs}) $$

    2.  **Naming Convention**: The words "args" and "kwargs" are just a **convention** (standard practice). You can use any valid variable names (e.g., `*elements`, `**attributes`), but stick to the convention for better readability.

---

## Functions Without a `return` Statement 🔄

!!! warning "Implicit Return Value: `None`"

    If a function or method executes without an explicit `return` statement, it implicitly returns the value **`None`**. Many list methods, like `.append()`, modify the list *in place* and return `None`.

    ```py title="" linenums="1"
    l = [1, 2, 3]
    print(l.append(5)) # The append method modifies l, but returns None
    print(l)
    ```
    ```py title="Output" linenums="1"
    None
    [1, 2, 3, 5]
    ```

-----

## Variable Scope 🌐

- [x] In Python, variables are resolved based on the LEGB rule (Local, Enclosing, Global, Built-in).

!!! tip "Global vs. Local Variables"

    === "Ex 1: Reading a Global Variable"
        A function can access (read) a variable defined in the **Global scope** if no local variable with the same name exists.
        ```py title="" linenums="1"
        def g(y):
          print(x)
          print(x+1)

        x=5 # Global variable
        g(x)
        print(x)
        ```
        ```py title="Output" linenums="1"
        5
        6
        5
        ```

    === "Ex 2: Local Variable Overrides Global"
        When a variable is assigned a value *inside* a function, it becomes a **Local variable**, which takes precedence over the global variable with the same name. It does not affect the global variable.
        ```py title="" linenums="1"
        def f(y):
          x=1 # x is local to f
          x+=1
          print(x)

        x=5 # Global variable
        f(x)
        print(x) # Global x remains unchanged
        ```
        ```py title="Output" linenums="1"
        2
        5
        ```

    === "Ex 3: Immutable Data and Scope"
        When an immutable argument (`x=3`) is passed to a function, the function receives a copy of the reference (pass-by-object-reference). Operations that modify the variable (like `x = x + 1`) create a new local variable `x` inside the function's scope, leaving the global `x` untouched.
        ```py title="" linenums="1"
        def f(x):
           x = x + 1 # Creates new local x
           print('in f(x): x =', x)
           return x

        x = 3 # Global x
        z = f(x)
        print('in main program scope: z =', z)
        print('in main program scope: x =', x) # Global x is still 3
        ```
        ```py title="Output" linenums="1"
        in f(x): x = 4
        in main program scope: z = 4
        in main program scope: x = 3
        ```

    === "Ex 4: `global` Keyword Error"
        The `global` keyword declares that a variable *inside* the function should refer to the global one. You cannot use `global` on a variable that is already defined as a function parameter, as parameters are always local to the function.
        ```py title="" linenums="1"
        # we can't change the global function

        def h(x): # x is already a local parameter
            global x # Error: cannot redeclare parameter as global
            x+=1

        x=5
        h(x)
        print(x)
        ```
        ```py title="Output" linenums="1"
        global x
            ^
        SyntaxError: name 'x' is parameter and global
        ```


-----

## Nested Functions 🪜

!!! abstract "Nested Function Execution"
    === "Ex 1: Simple Nesting"
        A function defined inside another function (a **nested function**) can only be called from within its enclosing function.
        ```py title="" linenums="1"
        def f():
          def g(): # g is local to f
            print('Inside g')
          g() # g() is called inside f
          print('Inside f')

        ```
        ```py title="Output" linenums="1"
        ```

    === "Ex 2: Calling the Enclosing Function"
        Calling the outer function executes it, which in turn calls the inner function.
        ```py title="" linenums="1"
        f()
        ```
        ```py title="Output" linenums="1"
        Inside g
        Inside f
        ```

    === "Ex 3: Inner Function Does Not Affect Outer Scope"
        A variable assignment (`x = 'abc'`) inside the inner function (`h`) creates a **local** variable `x` within `h`. This new `x` does not affect the `x` in the enclosing function (`g`).
        ```py title="" linenums="1"
        def g(x):
            def h():
                x = 'abc' # x is local to h
            x = x + 1 # x is local to g (from parameter)
            print('in g(x): x =', x)
            h() # h is executed but changes only its local x, which is immediately discarded
            return x

        x = 3 # Global x
        z = g(x)
        ```
        ```py title="Output" linenums="1"
        in g(x): x = 4
        ```

    === "Ex 4: Separate Scopes for Parameters"
        When the inner function (`h`) also takes a parameter named `x`, it has its own separate local scope. Modifications to `x` inside `h` do not affect the `x` in the enclosing function (`g`) or the global `x`.
        ```py title="" linenums="1"
        def g(x): # x is local to g (4)
            def h(x): # x is local to h (5)
                x = x+1
                print("in h(x): x = ", x)
            x = x + 1
            print('in g(x): x = ', x)
            h(x)
            return x

        x = 3 # Global x (3)
        z = g(x)
        print('in main program scope: x = ', x)
        print('in main program scope: z = ', z)
        ```
        ```py title="Output" linenums="1"
        in g(x): x = 4
        in h(x): x = 5
        in main program scope: x = 3
        in main program scope: z = 4
        ```


---

## Functions as First-Class Citizens 🥇

In Python, functions are considered **first-class citizens**, meaning they possess the following properties, similar to data types like integers or strings:

  - [x] Functions are a **data type** (`<class 'function'>`).
  - [x] They can be **assigned to variables**.
  - [x] They can be **stored** in data structures (lists, tuples, sets, dictionaries).
  - [x] They can be passed as **arguments** to other functions.
  - [x] They can be **returned** as values from other functions.

!!! info "Properties of Functions as Data"

    === "Ex 1: Type and ID"
        A function is a distinct type, and like any object, it has a unique memory address (`id`).
        ```py title="" linenums="1"
        # type and id

        def square(num):
          return num**2

        print(type(square))
        print(id(square))
        ```
        ```py title="Output" linenums="1"
        <class 'function'>
        1398082569376
        ```

    === "Ex 2: Reassignment (Aliasing)"
        The function object can be assigned to a new variable (`x`). Both names point to the **same object** (same ID).
        ```py title="" linenums="1"
        # reassign

        x = square
        print(id(x))
        print(id(square))
        print(x(5))
        ```
        ```py title="Output" linenums="1"
        1398082569376
        1398082569376
        25
        ```

    === "Ex 3: Deleting and Redefining"
        You can delete the original name, but the function object remains if it is referenced by another name (like `x` in the previous step). The function must be redefined to use the original name again.
        ```py title="" linenums="1"
        # deleting a function

        del square
        ```
        ```py title="Output" linenums="1"
        ```

        ```py title="" linenums="1"
        def square(num):
          return num**2
        ```
        ```py title="Output" linenums="1"
        ```

    === "Ex 4: Storing in Data Structures"
        Function objects can be stored inside lists, tuples, sets, or dictionaries.
        ```py title="" linenums="1"
        # storing in a list

        l = [1, 2, 3, square]
        print(l)
        ```
        ```py title="Output" linenums="1"
        [1, 2, 3, <function square at 0x00000233B2713420>]
        ```

    === "Ex 5: Storing in a Set"
        Functions are considered **immutable/hashable**, allowing them to be stored in sets.
        ```py title="" linenums="1"
        # storing in a set

        s = {square}
        print(s)
        ```
        ```py title="Output" linenums="1"
        {<function square at 0x00000233B2713420>}
        ```

    === "Ex 6: Returning a Function"
        A function (`f`) can define and return another function (`x`), which can then be called immediately.
        ```py title="" linenums="1"
        # returning a function

        def f():
          def x(a, b):
            return a+b
          return x

        # f() returns x; (3, 4) calls x
        val = f()(3, 4) 
        print(val)
        ```
        ```py title="Output" linenums="1"
        7
        ```

    === "Ex 7: Function as an Argument (Higher-Order Function)"
        A function (`func_c`) can accept another function (`func_a`) as an argument and execute it.
        ```py title="" linenums="1"
        # function as argument

        def func_a():
          print('inside func_a')

        def func_c(z): # z accepts a function
          print('inside func_c')
          return z() # executes the function passed as z

        print(func_c(func_a))
        ```
        ```py title="Output" linenums="1"
        inside func_c
        inside func_a
        None
        ```

---