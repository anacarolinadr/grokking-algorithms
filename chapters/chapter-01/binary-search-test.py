def binary_search(list, guess):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high) // 2
        mid_value = list[mid]
        if mid_value == guess:
            return mid
        elif mid_value < guess:
            low = mid + 1
        else:
            high = mid - 1

    return None

print(binary_search([1,2,3,4,5], 3))

print(binary_search([10,20,30,40,50], 7))

