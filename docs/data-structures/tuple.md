# Tuple

## Creating

!!! info "Creating"

    ```py title="" linenums="1"
    # tuple
    t1 = ()
    print(t1)

    # single item tuple
    t2 =(1,)
    print(t2)

    # homogenous
    t3 = (1,2,3)
    print(t3)

    # heterogenous
    t4 = (1,2.3,True,'hello')
    print(t4)

    # tuple in tuple
    t5 = (1,2,3,(4,5))
    print(t5)

    # using type conversion
    t6 = tuple((1,2,3, 'Rudra', 'z'))
    print(t6)
    ```
    ```py title="Output" linenums="1" 
    ()
    (1,)
    (1, 2, 3)
    (1, 2.3, True, 'hello')
    (1, 2, 3, (4, 5))
    (1, 2, 3, 'Rudra', 'z')
    ```



    ```py title="" linenums="1"
    # if we don;t use comma in singe then it show the singe input type 
    # example
    t7 = (1)
    print(type(t7))

    t8 = (1,)
    print(type(t8))
    ```
    ```py title="Output" linenums="1" 
    <class 'int'>
    <class 'tuple'>
    ```

## Accessing

!!! info "Accessing"
    === "Ex 1"
        ```py title="" linenums="1"
        t3 = (1,2,3)
        print(t3[0])
        print(t3[-1])

        # silicing
        print(t3[0:2])
        ```
        ```py title="Output" linenums="1" 
        1
        3
        (1, 2)
        ```

    === "Ex 2"
        ```py title="" linenums="1"
        t5 = (1,2,3,(4,5))
        print(t5[3][0])
        ```
        ```py title="Output" linenums="1" 
        4
        ```
    === "Ex 3"
      ```py title="" linenums="1"
      t5 = (1, 2, (3, 4, (5, 6), 8, 9), 10)

      t5[2][0]
      ```
      ```py title="Output" linenums="1" 
      3
      ```

    === "Ex 5"
      ```py title="" linenums="1"
      t5 = (1, 2, (3, 4, (5, 6), 8, 9), 10)

      print(f'accessing the 2 : {t5[1]} \n')
      print(f'accessing the 3 : {t5[2][0]} \n')
      print(f'accessing the 5 : {t5[2][2][0]} \n')
      ```
      ```py title="Output" linenums="1" 
      accessing the 2 : 2 

      accessing the 3 : 3 

      accessing the 5 : 5
      ```
    === "Ex 6"
        ```py title="" linenums="1"
        # first number must be greater than the second

        t6 = tuple((1,2,3, 'Rudra', 'z'))
        print(t6[-1:-4]) # -1>-4 no output
        print(t6[-4:-1]) # -4>-1 output
        ```
        ```py title="Output" linenums="1" 
        ()
        (2, 3, 'Rudra')
        ```

---

## Editing Items
!!! info "Editing"
    ```py title="" linenums="1"
    t3 = (1, 2, 3, 5)
    print(t3)
    t3[0] = 5 # immutable 
    print(t3)
    ```
    ```py title="Output" linenums="1" 
    1 t3 = (1, 2, 3, 5)
          2 print(t3)
    ----> 3 t3[0] = 5
          4 print(t3)

    TypeError: 'tuple' object does not support item assignment
    ```

## Adding Item

!!! info "Adding"
    === "Ex 1"
        ```py title="" linenums="1"
        # tuple is immutable
        t3 = (1,2,3)
        t3 = t3 + (4,5)
        print(t3)

        ```
        ```py title="Output" linenums="1" 
        (2, 3, 6, 5)
        ```
    === "Ex 2"
        ```py title="" linenums="1"
        t4 = (2, 3)
        t5 = (6, 5)

        t6 = t4 + t5
        t6
        ```
        ```py title="Output" linenums="1" 
        (2, 3, 6, 5)
        ```

#  Deleting
??? example "del"
    ```py title="" linenums="1"
    # delete the whole cell
    t3 = (1, 2, 3, 4, 5)
    print(t3)
    del t3
    print(t3)
    ```
    ```py title="Output" linenums="1" 
    3 print(t3)
          4 del t3
    ----> 5 print(t3)

    NameError: name 't3' is not defined
    ```

## Operations
!!! info "Operations"
    ```py title="" linenums="1"
    # *, +
    t1 = (1,2,3)
    t2 = (4,5,6)
    print('Addition :',t1+t2)
    print('Multiplication :',t1*3)

    # membership
    print(1 in t1)
    print(10 in t1)

    #iteration
    t1 = (1,2,3)
    for i in t1:
        print(i)
    ```
    ```py title="Output" linenums="1"
    Addition : (1, 2, 3, 4, 5, 6)
    Multiplication : (1, 2, 3, 1, 2, 3, 1, 2, 3)
    True
    False
    1
    2
    3
    ```

## Tuple Function

??? example "len, min, max, sorted"
    ```py title="" linenums="1"
    # len/ max/ min/ sorted

    t = (1,2,3,4,5,1,1)
    print('Lenth of the tuple is :',len(t))
    print('Max of the tuple is :',max(t))
    print('Min of the tuple is :',min(t))
    print('Sorted tuple is :',sorted(t, reverse=True))
    ```
    ```py title="Output" linenums="1"
    Lenth of the tuple is : 7
    Max of the tuple is : 5
    Min of the tuple is : 1
    Sorted tuple is : [5, 4, 3, 2, 1, 1, 1] 
    ```
??? example "count"
    ```py title="" linenums="1"
    # count
    t = (1,2,3,4,5,1,1)
    t.count(1)
    ```
    ```py title="Output" linenums="1" 
    3
    ```

    ```py title="" linenums="1"
    t = (1,2,3,4,5,1,1)
    t.count(79)
    ```
    ```py title="Output" linenums="1" 
    0
    ```

    ??? example "index"
    ```py title="" linenums="1"
    t = (1,2,3,4,5,1,1)
    t.index(3)
    ```
    ```py title="Output" linenums="1" 
    2
    ```

## Difference between lists and Tuple

??? example "Timing"
    ```py title="" linenums="1"
    import time
    l = list(range(10000000))
    t = tuple(range(10000000))

    start = time.time()
    for i in l:
      i*20
    print('List timing :',time.time()-start)

    start = time.time()
    for i in t:
      i*20
    print('tuple timing :',time.time()-start)
    ```
    ```py title="Output" linenums="1" 
    List timing : 1.1185483932495117
    tuple timing : 1.1489591598510742
    ```

## Special Syntax
??? example "Unpacking"
    ```py title="" linenums="1"
    # tuple unpacking
    a, b, c = (1, 2, 3)
    print(a, b, c)
    ```
    ```py title="Output" linenums="1" 
    1 2 3
    ```

??? example "Value Swap"
    ```py title="" linenums="1"
    # value swap

    a = 1
    b = 2
    a, b = b, a
    print(a, b)
    ```
    ```py title="Output" linenums="1" 
    2 1
    ```

??? example "*others"
    ```py title="" linenums="1"
    # '*' help to handle the rest of numbers
    a, b, *others = (1, 2, 3, 4, 5) 
    print(a, b)
    print(others)
    ```
    ```py title="Output" linenums="1" 
    1 2
    [3, 4, 5]
    ```


??? example "zipping"
    ```py title="" linenums="1"
    # zipping tuple
    t1 = (1, 2, 3)
    t2 = ('a', 'b', 'c')

    t3 = zip(t1, t2)
    print(t3)

    type(t3)
    # if we zip the tuple then we access by using the list 
    print(list(t3))
    ```
    ```py title="Output" linenums="1" 
    <zip object at 0x000001EA98B70280>
    zip
    [(1, 'a'), (2, 'b'), (3, 'c')]
    ```

---