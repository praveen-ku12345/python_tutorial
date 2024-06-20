class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data, index):
        new_node = Node(data, index)
        if self.top is None:
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node
    
    def pop(self):
        if self.top is None:
            return None, None
        data = self.top.data
        index = self.top.index
        self.top = self.top.prev
        if self.top is not None:
            self.top.next = None
        return data, index
    
    def is_empty(self):
        return self.top is None
    
    def peek_index(self):
        if self.top is None:
            return None
        return self.top.index

def valid_parantheses(s):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    
    index = 0
    while index < len(s):
        char = s[index]
        if char in mapping.values():
            stack.push(char, index)
        elif char in mapping.keys():
            top_char, _ = stack.pop()
            if top_char != mapping[char]:
                return index  
        else:
            return index  
        index += 1
    
    if not stack.is_empty():
        return stack.peek_index()  
    return -1  

p = input("Enter the parentheses: ")
result = valid_parantheses(p)
if result == -1:
    print("-1")
else:
    print(result+1)
