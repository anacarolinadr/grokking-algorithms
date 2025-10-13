array = [10, 20, 30]

print("Access second element:", array[1]) # O(1) 

array.append(40) 
print("After append:", array) # O(1) amortized

array.insert(0, 5)
print("After insert at beginning:", array) # O(N)

array.pop(0)
print("After removing first element:", array) # O(N)

'''

'''
