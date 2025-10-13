## Array vs Linked List

#### Chapter Two - A.Vs.L Notes

##### Array

- **Benefits**
  - Easy access — constant time **O(1)**.  
  - You know the address of each item.

- **Drawbacks**
  - If you add an element to the array, it might be full, and you’ll need to create a new one (**O(N)**).  
  - If you delete an element, you must shift all the elements to the left (**O(N)**).

##### Linked List

- **Benefits**
  - To insert or delete an element, you only need to change the address the previous item is pointing to.

- **Drawbacks**
  - Works well for sequential access, but random access takes **O(N)**, since if the element you want is the last one, you must iterate through every item.
