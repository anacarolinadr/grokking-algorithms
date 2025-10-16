## Quick Sort

#### Chapter Four - Q.S. Notes

* It is a sorting algorithm, is faster than selection sort 

* The base case is arrays with length 0 or 1, since you don't need to sort it

* To larger arrays, you must use the technique **Divide and Conquer**, choose a pivot and divide the array into numbers smaller than the pivot and larger than the pivot.

```python

[15,10,45,33] # pivot: 33

[15,10] + [33] + [45] # divide

[15,10] + [33] + [45] # sort 

[10,15,33,45] # quick sort

```

* A practical example  

``` python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller = [i for i in array[1:] if i <= pivot]
        larger = [i for i in array[1:] if i > pivot]
        # recursion
        return quicksort(smaller) + [pivot] + quicksort(larger)

```

* Average time complexity: medium - O(N * log(N)) and worst - O(N²)

