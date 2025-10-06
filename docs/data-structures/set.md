# Sets

## Creating Sets

!!! info "Creating"

    === "Ex 1: Empty Set vs. Empty Dictionary"
        ```py title="" linenums="1"
        # Empty
        s = set()
        d = {}
        print(type(s))
        print(type(d))
        ```
        ```py title="Output" linenums="1"
        <class 'set'>
        <class 'dict'>
        ```

    === "Ex 2: 1D Set"
        ```py title="" linenums="1"
        # 1D and 2D

        s1 = {1,2,3}
        print(s1)
        ```
        ```py title="Output" linenums="1"
        {1, 2, 3}
        ```

    === "Ex 3: No Nesting of Mutable Types"
        ```py title="" linenums="1"
        # no nesting (a set can't contain mutable types like another set)
        s2 = {1,2,3,{4,5}}
        print(s2)
        ```
        ```py title="Output" linenums="1"
        1 # no nesting
        ----> 2 s2 = {1,2,3,{4,5}}
        3 print(s2)
        TypeError: unhashable type: 'set'
        ```

    === "Ex 4: Heterogeneous Set (with Tuple)"
        ```py title="" linenums="1"
        # homo and hetero
        # True is 1 (duplicate values are ignored)
        # Tuples are immutable, so they can be contained in a set

        s3 ={1, 'hello', 3 + 4j, (4,5,6),True}
        print(s3)
        ```
        ```py title="Output" linenums="1"
        {(4, 5, 6), 1, 'hello', (3+4j)}
        ```

    === "Ex 5: Cannot Contain Mutable Items (List)"
        ```py title="" linenums="1"
        # set can't have mutable item (list is mutable)
        s5 = {1,2,3,[4,5]}
        print(s5)
        ```
        ```py title="Output" linenums="1"
        1 # set can't have mutable item
        ----> 2 s5 = {1,2,3,[4,5]}
        3 print(s5)

        TypeError: unhashable type: 'list'
        ```

    === "Ex 6: Unordered Nature (Comparison)"
        ```py title="" linenums="1"
        s1 = {1, 2, 3}
        s2 = {3, 2, 1}

        print(s1 == s2)
        ```
        ```py title="Output" linenums="1"
        True
        ```
---
## Accessing

!!! warning "Cannot Access Items by Index"
    A set is **unordered** and items cannot be accessed using an index (subscript) like lists or tuples, resulting in a `TypeError`.
    ```py title="" linenums="1"
    s = {1, 2, 3}
    print(s[0])
    ```
    ```py title="Output" linenums="1"
     1 s = {1, 2, 3}
    ----> 2 print(s[0])

    TypeError: 'set' object is not subscriptable
    ```

---

## Editing

!!! warning "Cannot Edit Items"
    Sets are **mutable** (you can add/remove items), but the individual items within a set are **immutable**. You cannot change an item at a specific position, resulting in a `TypeError`.
    ```py title="" linenums="1"
    n = {1, 2, 3}
    n[0] = 5
    print(n)
    ```
    ```py title="Output" linenums="1"
      1 n = {1, 2, 3}
    ----> 2 n[0] = 5
          3 print(n)

    TypeError: 'set' object does not support item assignment
    ```

---

## Adding Items

!!! info "Adding Items"
    === "Add Single Item (`.add()`)"
        Use the `.add()` method to add a single item to the set.
        ```py title="" linenums="1"
        # adding only one item
        b = {1, 2, 3}
        b.add(4)
        print(b)
        ```
        ```py title="Output" linenums="1"
        {1, 2, 3, 4}
        ```
    === "Add Multiple Items (`.update()`)"
        Use the `.update()` method to add multiple items from an iterable (like a list, tuple, or another set).
        ```py title="" linenums="1"
        # add multiple item
        b = {1, 2, 3}
        b.update([4, 5, 6])
        print(b)
        ```
        ```py title="Output" linenums="1"
        {1, 2, 3, 4, 5, 6}
        ```

---

## Deleting

??? example "Delete Entire Set (`del`)"
    The `del` keyword completely deletes the set variable from memory.
    ```py title="" linenums="1"
    # del - del total set
    k = {1, 2, 3}
    print(k)
    del k
    print(k)
    ```
    ```py title="Output" linenums="1"
    {1, 2, 3}
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    Cell In[8], line 5
          3 print(k)
          4 del k
    ----> 5 print(k)

    NameError: name 'k' is not defined
    ```

??? example "Delete Specific Item (`.discard()` vs. `.remove()`)"
    === "Discard (No Error if Not Present)"
        The `.discard()` method removes the specified item if it is present. **It does nothing and raises no error** if the item is not found.
        ```py title="" linenums="1"
        # discard
        # no error if no value present
        k = {1, 2, 3, 90}
        k.discard(2)
        print(k)
        k.discard(90)
        print(k)
        ```
        ```py title="Output" linenums="1"
        {1, 3, 90}
        {1, 3}
        ```
    === "Remove (Raises Error if Not Present)"
        The `.remove()` method removes the specified item. **It raises a `KeyError`** if the item is not found.
        ```py title="" linenums="1"
        # remove
        # error if value is not present
        k = {1, 2, 3}
        k.remove(2)
        print(k)
        ```
        ```py title="Output" linenums="1"
        {1, 3}
        ```

??? example "Delete Random Item (`.pop()`)"
    Since sets are unordered, the `.pop()` method removes and returns a **random** item from the set.
    ```py title="" linenums="1"
    # pop
    # remove random item
    k = {1, 2, 3}
    k.pop()
    print(k)
    ```
    ```py title="Output" linenums="1"
    {2, 3}
    ```

??? example "Empty Set (`.clear()`)"
    The `.clear()` method removes all elements from the set, leaving it empty.
    ```py title="" linenums="1"
    # clear
    # empty total set
    k = {1, 2, 3}
    k.clear()
    print(k)
    ```
    ```py title="Output" linenums="1"
    set()
    ```

---

## Set Operations ⚙️

!!! info "Set Operations"
    Python sets support the classic mathematical set operations. These operations can be performed using both **operators** and **methods**.

    === "Main Operations"
        ```py title="" linenums="1"
        # union
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print('\nUnion of the set is :',s1 | s2)
        print('Union of the set is :',s1.union(s2))

        # intersection
        print('\nIntersection of the set is :',s1 & s2)
        print('Intersection of the set is :',s1.intersection(s2))

        # difference
        print('\nDifference of the set is :',s1 - s2)
        print('Difference of the set is :',s1.difference(s2))

        # symmetric difference
        print('\nSymmetric difference of the set is :',s1 ^ s2)
        print('Symmetric difference of the set is :',s1.symmetric_difference(s2))
        ```
        ```py title="Output" linenums="1"
        Union of the set is : {1, 2, 3, 4, 5}
        Union of the set is : {1, 2, 3, 4, 5}

        Intersection of the set is : {3}
        Intersection of the set is : {3}

        Difference of the set is : {1, 2}
        Difference of the set is : {1, 2}

        Symmetric difference of the set is : {1, 2, 4, 5}
        Symmetric difference of the set is : {1, 2, 4, 5}
        ```

| Operation | Description | Operator | Method |
| :--- | :--- | :--- | :--- |
| **Union** | All unique elements in both sets. | `\|` | `.union()` |
| **Intersection** | Elements common to both sets. | `&` | `.intersection()` |
| **Difference** | Elements in the first set but **not** in the second. | `-` | `.difference()` |
| **Symmetric Difference** | Elements in either set, but **not** in both. | `^` | `.symmetric_difference()` |

---

## Membership Testing

!!! tip "Check for Elements"
    You can efficiently check if an element is present in a set using the `in` and `not in` keywords.
    ```py title="" linenums="1"
    # membership
    s1 = {1, 2, 3}
    print(f'Is 1 in s1? : {1 in s1}')
    print(f'Is 1 not in s1? : {1 not in s1}')
    ```
    ```py title="Output" linenums="1"
    True
    False
    ```

---

## Iteration (Looping)

!!! example "Looping Through a Set"
    You can iterate over the elements of a set using a standard `for` loop. Since sets are unordered, the elements will be retrieved in an arbitrary order.
    ```py title="" linenums="1"
    # loop
    s1 = {1, 2, 3}
    print("Looping results:")
    for i in s1:
      print(i)
    ```
    ```py title="Output" linenums="1"
    Looping results:
    1
    2
    3
    ```

---


## Set Function
??? example "len, min, max, sorted"
      ```py title="" linenums="1"
      s = {1, 2, 3}
      print(" lenght of the function :",len(s))
      print(" max of the function :",max(s))
      print(" min of the function :",min(s))
      print(" sorted of the function :",sorted(s))
      ```
      ```py title="Output" linenums="1" 
      lenght of the function : 3
      max of the function : 3
      min of the function : 1
      sorted of the function : [1, 2, 3]
      ```

??? example "union, update"
      ```py title="" linenums="1"
      # union/ update
      s1 = {1, 2, 3}
      s2 = {3, 4, 5}
      s3 = {5, 6, 7}

      # union
      s1.union(s3)
      print(s3)

      # s1 parmanet change
      s1.update(s2)
      print(s1)
      print(s2)
      ```
      ```py title="Output" linenums="1" 
      {5, 6, 7}
      {1, 2, 3, 4, 5}
      {3, 4, 5}
      ```
??? example "isdisjoint, issubjoint, issupjoint"
      ```py title="" linenums="1"
      # isdisjoint/ issubjoint /issupjoint

      s1 = {1, 2, 3}
      s2 = {3, 4, 5}
      s3 = {1, 2, 3, 5, 6, 7}

      print(" Disjoint set is :",s1.isdisjoint(s2))
      print(" Subjoint set is :",s1.issubset(s2))
      print(" Supjoint set is :",s3.issuperset(s1))

      ```
      ```py title="Output" linenums="1" 
      Disjoint set is : False
      Subjoint set is : False
      Supjoint set is : True
      ```

??? example "copy"
      ```py title="" linenums="1"
      # copy
      s1 = {1, 2, 3}
      s2 = s1.copy()
      print(s2)
      ```
      ```py title="Output" linenums="1" 
      {1, 2, 3}
      ```
---
## Frozenset (Immutable Set)

!!! info "Creating and Properties"
    Frozensets are **immutable** versions of Python sets. Like tuples for lists, frozensets can be nested inside other sets (or used as dictionary keys) because they are hashable. All read-only set functions work, but all methods that modify the set (write functions like `.add()`, `.remove()`, etc.) will not work.

    === "Creating a Frozenset"
        A frozenset is created using the built-in `frozenset()` constructor, usually passed an iterable (like a list or a regular set).
        ```py title="" linenums="1"
        # creating frozenset from a set
        s1 = {1, 2, 3}
        fs2 = frozenset(s1)
        print(fs2)
        ```
        ```py title="Output" linenums="1"
        frozenset({1, 2, 3})
        ```

    === "Nesting Frozensets (2D)"
        Because a frozenset is **immutable** (and thus **hashable**), it can be nested inside another frozenset or a regular set.
        ```py title="" linenums="1"
        # 2d (frozenset containing another frozenset)
        fs = frozenset([1, 2, 3, frozenset([4, 5])])
        print(fs)
        ```
        ```py title="Output" linenums="1"
        frozenset({frozenset({4, 5}), 1, 2, 3})
        ```
---

#### Frozenset Operations (Read-Only)

!!! success "Set Operations Work"
    Frozensets support all set theory operations (union, intersection, difference, etc.) using both operators and methods, which return a new frozenset as a result.

    ```py title="" linenums="1"
    fs1 = frozenset([1, 2, 3])
    fs2 = frozenset([3, 4, 5])

    # union
    print(fs1 | fs2)

    # intersection
    print(fs1 & fs2)

    # difference
    print(fs1 - fs2)
    ```
    ```py title="Output" linenums="1"
    frozenset({1, 2, 3, 4, 5})
    frozenset({3})
    frozenset({1, 2})
    ```

##### Key Takeaway on Frozensets
- [x] **All read functions work** (e.g., `in`, iteration, `union()`, `intersection()`).
- [ ] **All write functions not work** (e.g., `.add()`, `.remove()`, `.clear()` will raise an `AttributeError`).

---

## Set Comprehension

!!! info "Set Comprehension"

    === "Ex 1"

        ```py title="" linenums="1"
        {i for i in range(10)}
        ```
        ```py title="Output" linenums="1" 
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        ```
            
    === "Ex 2"
        ```py title="" linenums="1"
        {i**2 for i in range(10)}
        ```
        ```py title="Output" linenums="1" 
        {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
        ```
        
---