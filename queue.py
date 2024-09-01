class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.max_size - 1

    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full")
            return

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None

        item = self.queue[self.front]

        if self.front == self.rear
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.rear]

def main():
    queue_size = int(input("Enter the size of the queue: "))
    q = Queue(queue_size)

    while True:
        print("\nQueue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Show Front Element")
        print("5. Show Rear Element")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element to enqueue: "))
            q.enqueue(element)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            front = q.getFront()
            if front is not None:
                print("Front element:", front)
        elif choice == 5:
            rear = q.getRear()
            if rear is not None:
                print("Rear element:", rear)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
