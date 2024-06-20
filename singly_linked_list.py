class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_mid(self, data, location):
        if location == 0:
            self.insert_start(data)
            return
        newnode = Node(data)
        temp = self.head
        for i in range(location - 1):
            if temp is None:
                print("Location out of bounds:")
                return
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode

    def insert_last(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def delete_start(self):
        if not self.head:
            print("List is empty. Cannot delete.")
            return
        self.head = self.head.next

    def delete_mid(self, location):
        if location == 0:
            self.delete_start()
            return
        temp = self.head
        for i in range(location - 1):
            if temp is None or temp.next is None:
                print("Location out of bounds:")
                return
            temp = temp.next
        temp.next = temp.next.next

    def delete_last(self):
        if not self.head:
            print("Cannot delete. List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Size of the linked list:", count)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
obj = SinglylinkedList()
while True:
    print("1. Insert\n2. Delete\n3. Display\n4. Reverse\n5. Size\n6. Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data to insert: "))
        print("1. Insert at start\n2. Insert at mid\n3. Insert at last")
        pos = int(input("Enter the position to insert: "))
        if pos == 1:
            obj.insert_start(data)
            print(f"Data is inserted into the linked list at position {pos}")
        elif pos == 2:
            location = int(input("Enter the location where you want to insert: "))
            obj.insert_mid(data, location)
            print(f"Data is inserted into the linked list at position {pos}")
        elif pos == 3:
            obj.insert_last(data)
            print(f"Data is inserted into the linked list at position {pos}")
        else:
            print("Invalid position choice.")
    elif choice == 2:
        print("1. Delete at start\n2. Delete at mid\n3. Delete at last")
        pos = int(input("Enter the position where you want to delete: "))
        if pos == 1:
            obj.delete_start()
        elif pos == 2:
            location = int(input("Enter the location to delete: "))
            obj.delete_mid(location)
        elif pos == 3:
            obj.delete_last()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        obj.reverse()
    elif choice == 5:
        obj.size()
    elif choice == 6:
        break
    else:
        print("Invalid input. Choose a correct option.")
