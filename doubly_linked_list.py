class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insert_last(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
    def insert_last(self,data,pos):
        if pos==0:
            self.insert_start(data)
            return
        newnode=Node(data)
        temp=self.head
        for i in range(pos-1):
            if temp is None:
                print("position out of bounds")
                return
            temp=temp.next
        newnode.next=temp.next
        if temp:
            temp.next.prev=newnode
        temp.next=newnode
        newnode.prev=temp
    def display(self):
        temp=self.head
        while temp.next:
            print(temp.data,end='->')
            temp=temp.next
        
obj = DoublyLinkedList()
while True:
    print("1. Insert\n2. Delete\n3. Display\n5. Size\n6. Exit\n4.dispaly forwarad\n7.display backword\n")
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
        obj.forward_display()
    elif choice ==7:
        obj.backward_display()
    elif choice == 5:
        obj.size()
    elif choice == 6:
        break
    else:
        print("Invalid input. Choose a correct option.")
