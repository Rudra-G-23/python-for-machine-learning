# Lists

!!! info "Why List"

    ```py title="" linenums="1"
    l = [1, 2, 3]
    # id helps to print the  memory
    # referential array

    print(id(l))
    print(id(l[0]))
    print(id(l[1]))
    print(id(l[2]))

    print(id(1))
    print(id(2))
    print(id(3))
    ```
    ```py title="Output" linenums="1" 
    1850613472960
    140718135210792
    140718135210824
    140718135210856
    140718135210792
    140718135210824
    140718135210856
    ```
---

## Creating a Lists

!!! info "Creating"

    ```py title="" linenums="1"
    # empty
    print([])
    L= []
    print(L)


    # 1D ->
    L = [1, 2, 3, 4, 5]
    print(L)

    # 2D ->
    L = [1, 2, 3, [4, 5, 6]]
    print(L)

    # 3D ->
    L = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    print(L)

    # Heterogenous
    print(1, True, 5.9, 5+3j, 'z')

    # using type conversion
    print(list('hello'))
    print(list({1, 2, 3}))
    ```
    ```py title="Output" linenums="1" 
    []
    []
    [1, 2, 3, 4, 5]
    [1, 2, 3, [4, 5, 6]]
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    1 True 5.9 (5+3j) z
    ['h', 'e', 'l', 'l', 'o']
    [1, 2, 3]
    ```

---

## Accessing Items

!!! info "Accessing"

    === "Indexing"

        ```py title="" linenums="1"
        l = [1, 2, 3, 4, 5]
        print(l[0])
        print(l[1])
        print(l[2])
        print(l[3])
        print(l[4])
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        4
        5
        ```

    === "1D"
        ```py title="" linenums="1"
        k = [1, 3, 5, 7, 9]
        print(k[3])
        ```
        ```py title="Output" linenums="1" 
        7
        ```

    === "2D"

        ```py title="" linenums="1"
        w =  [1, 2, 3 ,4, [5, 6]]
        print(w[-1][0])
        ```
        ```py title="Output" linenums="1" 
        5
        ```
    === "3D"

        ```py title="" linenums="1"
        o = [[12, 4, 5 ],
            [24, 5, 9, 0],
              [ [45, 67],
                [24, 69] ]
            ]

        print(o[2][1][1])
        ```
        ```py title="Output" linenums="1" 
        69
        ```

---

## Adding Items

??? example "append"

    === "Ex 1"

        ```py title="" linenums="1"
        v = [1, 3, 5, 8, 9, 2]
        v.append(True)
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 3, 5, 8, 9, 2, True]
        ```

    === "Ex 2"

        ```py title="" linenums="1"
        v.append([3, 56, 67])
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 3, 5, 8, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67]]
        ```

    === "Ex 3"

        ```py title="" linenums="1"
        v.append(["Odisha"])
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 3, 5, 8, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67], 'O', 'd', 'i', 's', 'h', 'a', ['Odisha']]
        ```

??? example "extend"

    === "Ex 1"

        ```py title="" linenums="1"
        v = [1, 3, 5, 8, 9, 2]
        v.extend([2, 4, 5, 6, 9])
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 3, 5, 8, 9, 2, True, 2, 4, 5, 6, 9]
        ```
    === "Ex 2"

        ```py title="" linenums="1"
        v.extend('Odisha')
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 3, 5, 8, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67], 'O', 'd', 'i', 's', 'h', 'a']
        ```



??? example "insert"

    ```py title="" linenums="1"
    # insert
    # index place, what to place

    v.insert(0, 'hello')
    print(v)
    ```
    ```py title="Output" linenums="1" 
    [1, 3, 5, 'hello', 8, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67], 'O', 'd', 'i', 's', 'h', 'a', ['Odisha']]
    ```

---

## Editing

!!! info "Editing"

    === "Ex 1"

        ```py title="" linenums="1"
        v[1] = 'Rudra'
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 'Rudra', 5, 'hello', 8, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67], 'O', 'd', 'i', 's', 'h', 'a', ['Odisha']]
        ```

    === "Ex 2"

        ```py title="" linenums="1"
        v[3:5] = [300, 400, 500]
        print(v)
        ```
        ```py title="Output" linenums="1" 
        [1, 'Rudra', 5, 300, 400, 500, 9, 2, True, 2, 4, 5, 6, 9, [3, 56, 67], 'O', 'd', 'i', 's', 'h', 'a', ['Odisha']]
        ```

## Deleting

??? example "del"

    === "Ex 1"
      
          ```py title="" linenums="1"
          h = [1,2,3,4,5,6,7,8,9]
          del h[0]
          print(h)
          ```
          ```py title="Output" linenums="1" 
          [2, 3, 4, 5, 6, 7, 8, 9]
          ```

    === "Ex 2"

        ```py title="" linenums="1"
        h = [1,2,3,4,5,6,7,8,9]
        del h[:3]
        print(h)
        ```
        ```py title="Output" linenums="1" 
        [5, 6, 7, 8, 9]
        ```

??? example "remove"
    ```py title="" linenums="1"
    # reomve

    h.remove(8)
    print(h)
    ```
    ```py title="Output" linenums="1" 
    [5, 6, 7, 9]
    ```

??? example "pop"

    === "Ex 1"
        ```py title="" linenums="1"
        # pop
        h = [1,2,3,4,5,6,7,8,9]
        h.pop(0)
        print(h)
        ```
        ```py title="Output" linenums="1" 
        [2, 3, 4, 5, 6, 7, 8, 9]
        ```

    === "Ex 2"
        ```py title="" linenums="1"
        # del last value
        # default is -1 (Last is deleted)
        h = [1,2,3,4,5,6,7,8,9]
        h.pop()
        print(h)
        ```
        ```py title="Output" linenums="1" 
        ```

    === "Ex 3"
        ```py title="" linenums="1"
        h = [1,2,3,4,5,6,7,8,9]
        h.pop()
        print(h)
        ```
        ```py title="Output" linenums="1" 
        [1, 2, 3, 4, 5, 6, 7, 8]
        ```

??? example "clear"
    ```py title="" linenums="1"
    # clear
    # empty the list

    h.clear()
    print(h)
    ```
    ```py title="Output" linenums="1" 
    []
    ```

---

## Operations

!!! info "operations"
    === "Arithmetic"
        ```py title="" linenums="1"
        # Arithmetic ( +, *)

        l1 = [1, 2, 3]
        l2 = [4, 5, 6]

        print(l1 + l2)
        print(l1 * 3)
        ```
        ```py title="Output" linenums="1" 
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 1, 2, 3, 1, 2, 3]
        ```
    === "Membership"

          ```py title="" linenums="1"
          # Membership

          print(1 in l1)
          print(1 not in l1)
          ```
          ```py title="Output" linenums="1" 
          True
          False
          ```

        ```py title="" linenums="1"
        k = [1, 2, 3, [4, 5, 6]]
        print([4, 5, 6] in k)
        ```
        ```py title="Output" linenums="1" 
        True
        ```
    === "loop"
    
        ```py title="" linenums="1"
        # loop
        k = [1, 2, 3, [4, 5, 6]]

        for i in k:
        print(i)
        ```
        ```py title="Output" linenums="1" 
        1
        2
        3
        [4, 5, 6]
        ```

        ```py title="" linenums="1"
        o = [
        [12, 4, 5 ],
        [24, 5, 9, 0],
        [ [45, 67],
        [24, 69] ]
        ]

        for i in o:
        print(i)
        ```
        ```py title="Output" linenums="1" 
        [12, 4, 5]
        [24, 5, 9, 0]
        [[45, 67], [24, 69]]
        ```

---

## List Functions

??? example "len, min, max, sorted"

    ```py title="" linenums="1"
    r1 = [1, 2, 3, 4, 5]
    print('Length of the function is :', len(r1))
    print('Minimum item in the function is :', min(r1))
    print('Maximum item in  the function is :', max(r1))
    print('Sorted of the function is :', sorted(r1)) # reverse = True (parameter)
    ```
    ```py title="Output" linenums="1" 
    Length of the function is : 5
    Minimum item in the function is : 1
    Maximum item in  the function is : 5
    Sorted of the function is : [1, 2, 3, 4, 5]
    ```

??? example "count"
    ```py title="" linenums="1"
    # count
    r2 = [2, 3, 4, 5, 2, 4, 2, 3, 2, 1, 3]
    print(r2.count(2))
    print(r2.count(3))
    ```
    ```py title="Output" linenums="1" 
    4
    3
    ```

??? example "index"
    ```py title="" linenums="1"
    r3 = [1, 2, 3, 4, 1, 5,  5]
    r3.index(2)
    r3.index(5) # first occurrence
    ```
    ```py title="Output" linenums="1" 
    5
    ```

??? example "sorted, sort"
    ```py title="" linenums="1"
    # sorted -> permanent
    # sort -> temporary

    r5 = [1, 2, 3, 4, 5, 22, 3, 4, 65]
    print(sorted(r5))
    r5.sort()
    ```
    ```py title="Output" linenums="1" 
    [1, 2, 3, 3, 4, 4, 5, 22, 65]
    ```

??? example "copy"
    ```py title="" linenums="1"
    # copy
    # deep copy / shallow copy
    r6 = [1, 2, 3, 4, 5]
    r7 = r6.copy()
    print(r6)
    print(r7)
    ```
    ```py title="Output" linenums="1" 
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    ```

## List Comprehension

!!! info "Comprehensions"
    === "Ex 1"
        ```txt
        new_list = [ Expression for item in iterable if condition == True ]
        ```

        ```py title="" linenums="1"
        l: list[int] = [ i for i in range(1, 11)]
        l
        ```
        ```py title="Output" linenums="1" 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ```

    === "Ex 2"
        ```py title="" linenums="1"
        l: list[int] = [ i**2 for i in range(1, 11)]
        l
        ```
        ```py title="Output" linenums="1" 
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        ```
    
    === "Ex 3"
        ```py title="" linenums="1"
        v = [2, 3, 4 ]
        s = -3
        l3 = [i*s for i in v]
        print(l3)
        ```
        ```py title="Output" linenums="1" 
        [-6, -9, -12]
        ```

    === "Ex 4"
        ```py title="" linenums="1"
        l5: list[int] = [i for i in range(1, 52) if i % 5== 0]
        l5
        ```
        ```py title="Output" linenums="1" 
        [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        ```
    === "Ex 5"
        ```py title="" linenums="1"
        # words start with p
        words: list[str] = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'python', 'php', 'pandas']
        l6 = [ i for i in words if i.startswith('p')]
        l6
        ```
        ```py title="Output" linenums="1" 
        ['python', 'php', 'pandas']
        ```
    === "Ex 6"
        ```py title="" linenums="1"
        # nested if

        l7 = [ i for i in range(1, 101) if i%5 == 0 if i%8 == 0]
        l7
        ```
        ```py title="Output" linenums="1" 
        [40, 80]
        ```
    === "Ex 7"
        ```py title="" linenums="1"
        [[i*j for i in range(1, 3)] for j in range(1, 5)]
        ```
        ```py title="Output" linenums="1" 
        [[1, 2], [2, 4], [3, 6], [4, 8]]```
        ```
    === "Ex 8"
        ```py title="" linenums="1"
        # pair

        h: list[int] = [1, 2]
        k: list[int] = [5, 9]

        l8 = [(i, j) for i in h for j in k]
        l8
        ```
        ```py title="Output" linenums="1" 
        [(1, 5), (1, 9), (2, 5), (2, 9)]
        ```
    === "Ex 8"
        ```py title="" linenums="1"
        # pairing
        g = [1, 2, 3]
        h = [4, 5, 6]
        l8 = [(i, j) for i in g for j in h]
        print(l8)
        ```
        ```py title="Output" linenums="1" 
        [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
        ```

    === "Ex 9"
        ```py title="" linenums="1"
        # cartesian product

        g = [1, 2, 3]
        h = [4, 5, 6]
        l9 = [ i*j for i in g for j in h]
        print(l9)
        ```
        ```py title="Output" linenums="1" 
        [4, 5, 6, 8, 10, 12, 12, 15, 18]
        ```

## Transverse a List

!!! info
    === "Item wise"
        ```py title="" linenums="1"
        # item wise

        for l in l9:
          print(l)
        ```
        ```py title="Output" linenums="1" 
        4
        5
        6
        8
        10
        12
        12
        15
        18
        ```

    === "Id-wise"

        ```py title="" linenums="1"
        # id-xwise
        y = [1, 2, 3, 4, 5]

        for i in range(0, len(y)):
          print(y[i])
        ```
        ```py title="Output" linenums="1" 
        [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
        ```

## Zip

!!! abstract "Zip"
    === "Ex 1"
        ```py title="" linenums="1"
        b1 = [1, 2, 3]
        b2 = [4, 5, 6, 4]

        print(list(zip(b1, b2)))
        ```
        ```py title="Output" linenums="1" 
        [(1, 4), (2, 5), (3, 6)]
        ```

    === "Ex 2"
        ```py title="" linenums="1"
        b1 = [1, 2, 3]
        b2 = [4, 5, 6, 4]
        [i+j for i,j in zip(b1, b2)]
        ```
        ```py title="Output" linenums="1" 
        [5, 7, 9]
        ```
    === "Ex 3"
        ```py title="" linenums="1"
        m = [1, 7, True, 5+3j, input, 'hello', print, 'print']
        print(m)
        ```
        ```py title="Output" linenums="1" 
        [1, 7, True, (5+3j), <bound method Kernel.raw_input of <ipykernel.ipkernel.IPythonKernel object at 0x000001AEDF88BAD0>>, 'hello', <built-in function print>, 'print']
        ```

    === "Ex 4"
        ```py title="" linenums="1"
        a = [1, 2, 3]
        b = a.copy()

        print(a)
        print(b)

        a.append(4)
        print(a)
        print(b)
        ```
        ```py title="Output" linenums="1" 
        [1, 2, 3]
        [1, 2, 3]
        [1, 2, 3, 4]
        [1, 2, 3]
        ```

---