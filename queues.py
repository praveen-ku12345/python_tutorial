class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, queue_item):
        self.items.append(queue_item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Cannot dequeue. Queue is empty.")

    def front(self):
        if self.items:
            return self.items[0]
        else:
            print("Cannot get the front element. Queue is empty.")

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue = Queue()
    while True:
        print("Choose an option:")
        print("1. Enqueue the queue")
        print("2. Dequeue the queue")
        print("3. Front element of the queue")
        print("4. Size of the queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            queue_item = int(input("Enter the element to enqueue: "))
            queue.enqueue(queue_item)
            print(f"{queue_item} enqueued to the queue.")
        elif choice == '2':
            dequeued_item = queue.dequeue()
            if dequeued_item is not None:
                print(f"Dequeued item is {dequeued_item}")
            else:
                print("Cannot dequeue. Queue is empty.")
        elif choice == '3':
            front_item = queue.front()
            if front_item is not None:
                print(f"Front element: {front_item}")
            else:
                print("Cannot get the front element. Queue is empty.")
        elif choice == '4':
            print(f"Size of the queue: {queue.size()}")
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option.")
