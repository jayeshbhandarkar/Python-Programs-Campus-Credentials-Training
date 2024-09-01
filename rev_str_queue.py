# Reverse the Queue using Stack

from queue import Queue

def reverseQueue(q):
    stack = []

    while not q.empty():
        stack.append(q.get())

    while stack:
        q.put(stack.pop())

def displayQueue(q):
    temp_queue = Queue()
    print("Queue elements:", end=" ")

    while not q.empty():
        element = q.get()
        print(element, end=" ")
        temp_queue.put(element)

    while not temp_queue.empty():
        q.put(temp_queue.get())
    print()

def main():
    q = Queue()

    elements = [1, 2, 3, 4, 5]
    print("Original Queue:")
    for element in elements:
        q.put(element)
    displayQueue(q)

    reverseQueue(q)

    print("Reversed Queue:")
    displayQueue(q)

if __name__ == "__main__":
    main()
