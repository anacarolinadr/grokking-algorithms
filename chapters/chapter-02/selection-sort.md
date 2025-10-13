## Selection Sort

#### Chapter Two - S.S. Notes

* This algorithm iterates through the list, finding the smallest (or largest) element in each pass and placing it in its correct position in the array.

* The execution time is O(N²), because it iterates over each element and compares it with all the others

* Quick sort is faster and more efficient (O(N * log(N))) than selection sort and will be explained in the next chapters

* Chapter Example

```python

def searchLow(arr):
    low = arr[0] # gets the lowest value
    low_i = 0 # gets index of the lowest value
    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
            low_i = i
    return low_i

def selectionSort(arr): # selection sort
    newArr = []
    for i in range(len(arr)):
        # finds the lowest element and pops it into the new array
        low = searchLow(arr) 
        newArr.append(arr.pop(low))
    return newArr

print(selectionSort([5, 10, 4, 7,]))
```



