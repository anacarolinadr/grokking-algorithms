## Binary Search 

#### Chapter One - B.S. Notes 

* The input list for binary search must be sorted

* The algorithm calculates the middle index and analyzes whether the element is greater or smaller than it. Based on that, it chooses the portion where the element is located and continues to search.

* So, binary search needs log(n) to return the correct element, unlike linear search, which requires n steps

* Practical example in Python:

```python 

def binary_search(list, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        middle = (low + high) / 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle - 1

    return None

list = [1, 3, 5, 7, 9]
```

* Even if the input contains 4.000.000.000 elements, the execution time is still very short, just 32 guesses, unlike linear search which may require all 4,000,000,000 guesses in the worst case

