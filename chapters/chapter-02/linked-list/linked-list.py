class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_at_index(self, index, value):
        if index == 0:
            self.add_at_beginning(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def remove_at_beginning(self):
        if not self.head:
            raise IndexError("List is empty")
        self.head = self.head.next

    def remove_at_end(self):
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at_index(self, index):
        if not self.head:
            raise IndexError("List is empty")
        if index == 0:
            self.remove_at_beginning()
            return

        current = self.head
        for _ in range(index - 1):
            if not current.next:
                raise IndexError("Index out of range")
            current = current.next

        if not current.next:
            raise IndexError("Index out of range")
        current.next = current.next.next

    def get_by_index(self, index):
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        return current.value if current else None

    def find_by_value(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1 

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_end(30)
ll.add_at_beginning(5)
ll.add_at_index(2, 15)

print("Initial list:")
ll.print_list()

print("Element at index 2:", ll.get_by_index(2))
print("Index of element 20:", ll.find_by_value(20))

ll.remove_at_beginning()
ll.remove_at_end()
ll.remove_at_index(1)
ll.print_list()
