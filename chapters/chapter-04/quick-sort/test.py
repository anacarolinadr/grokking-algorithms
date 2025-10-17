def quicksort(array):
    if len(array) < 2:
        return array
    else:
        middle = len(array) // 2
        pivot = array[middle]
        rest = array[:middle] + array[middle+1:]  
        less = [i for i in rest if i <= pivot]
        greater = [i for i in rest if i > pivot]
        print(f"pivot: {pivot}, less: {less}, greater: {greater}")
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2, 3, 6, 8, 11]))
