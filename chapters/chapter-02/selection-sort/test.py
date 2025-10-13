# Example from the book
def searchLow(arr):
    low = arr[0] 
    low_i = 0 
    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
            low_i = i
    return low_i

def selectionSort(arr): 
    newArr = []
    for i in range(len(arr)):
        low = searchLow(arr) 
        newArr.append(arr.pop(low))
    return newArr

print(selectionSort([5, 10, 4, 7,]))