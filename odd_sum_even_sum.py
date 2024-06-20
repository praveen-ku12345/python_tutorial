class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
def recursive_sum(node, index, even_sum, odd_sum):
    if node is None:
        return even_sum, odd_sum
    if index % 2 == 0:
        even_sum += node.data
    else:
        odd_sum += node.data
    return recursive_sum(node.next, index + 1, even_sum, odd_sum)
n = int(input("Enter the number of elements: "))
elements = list(map(int, input("Enter the numbers: ").split()))
dll = DoublyLinkedList()
for element in elements:
    dll.append(element)
even_sum, odd_sum = recursive_sum(dll.head, 0, 0, 0)
print(abs(even_sum - odd_sum))