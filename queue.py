class Queue:
    def __init__(self, max_size):
        # Initialize the queue with a fixed size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def isEmpty(self):
        # Check if the queue is empty
        return self.front == -1

    def isFull(self):
        # Check if the queue is full
        return self.rear == self.max_size - 1

    def enqueue(self, item):
        # Add an item to the rear of the queue
        if self.isFull():
            print("Queue is Full")
            return

        if self.isEmpty():
            # Set front and rear to 0 if the queue is initially empty
            self.front = 0
            self.rear = 0
        else:
            # Increment rear to add the new item
            self.rear += 1

        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        # Remove an item from the front of the queue
        if self.isEmpty():
            print("Queue is Empty")
            return None

        item = self.queue[self.front]

        # Move the front pointer to the next element
        if self.front == self.rear:
            # Reset the queue when the last element is dequeued
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        print(f"Dequeued: {item}")
        return item

    def display(self):
        # Display the elements of the queue
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def getFront(self):
        # Return the front element of the queue without removing it
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]

    def getRear(self):
        # Return the rear element of the queue without removing it
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.rear]


# Menu-driven implementation
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
