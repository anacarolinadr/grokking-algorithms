## Chapter 04  

##### Chapter Four - Answers

- 4.1 
```python
def plus(array):
    if array == []:
        return 0
    else:
        return array[0] + plus(array[1:])

```

- 4.2
```python
def count(array):
    if array == []:
        return 0
    else:
        return 1 + count(array[1:])
```

- 4.3
```python
def larger(array):
    if array == []:
        return None
    else:
        max_rest = larger(array[1:])
        return array[0] if array[0] > max_rest else max_rest
```

- 4.4 The base case occurs when the element is found, or when the search range becomes empty.
The recursive case occurs when the element has not yet been found, so the array (or range) is divided in half and the search continues in the appropriate half.

- 4.5 O(N)

- 4.6 O(N)

- 4.7 O(1)

- 4.8 O(N²)