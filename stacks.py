class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item_push):
        self.items.append(item_push)
    def pop(self,poped_item):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty cannot pop")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")
    def size(self):
        return len(self.items)
    def is_empty(self):
        return (self.items)==0
if __name__=="__main__":
    stack=Stack()
    while True:
        print("choose any one option :")
        print("1.push item :")
        print("2.pop item :")
        print("3.size of stack :")
        print("4.peek of stack :")
        print("5.is the stack is empty :")
        print("6.exit :")
        choice=input("choose any option ")
        if choice=='1':
            item_push=int(input("enterthe item to push :"))
            stack.push(item_push)
        elif choice=='2':
            poped_item=stack.pop()
            if stack is not None:
                print(f"poped item is{poped_item}")
        elif choice=='3':
            print(f"size of stack is {stack.size()}")
        elif choice=='4':
            peek_stack=stack.peek()
            print(peek_stack)
        elif choice=='5':
            if stack.is_empty():
                print("stack is not empty")
            else:
                print("stack is empty")
        elif choice=='6':
            print("existing")
            break
        else:
            print("invalid option")
