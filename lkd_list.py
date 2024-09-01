import sys

class GetNode:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        data = int(input("\nEnter Data: "))
        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        
        else: 
            ptr = self.head

            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode
            print(data, "is added to the list....")

    def traverse(self):
        ptr = self.head
        print("Displaying Linked List")
        while ptr is not None:
            print(ptr.data, "->", end="")
            ptr = ptr.next
        print("\n")

    def addBegin(self):
        data = int(input("\nEnter Data: "))
        newNode = GetNode()
        newNode.data = data

        if self.head is None:
            self.head = newNode
        
        else: 
            newNode.next = self.head
            self.head = newNode
            print(data,"is added at the beginning of the List")

    def addBetween(self):
        data = int(input("\nEnter Data: "))
        newNode = GetNode()
        key=int(input("\nEnter data after which is to be inserted: "))

        newNode.data = data

        if self.head is None:
            self.head = newNode
        
        else: 
            ptr = self.head
            while ptr.data != key:
                ptr = ptr.next
                
            newNode.next = ptr.next
            ptr.next = newNode
            print(data, "is added after", key)

    def deleteAnywhere(self):
        if self.head is None:
            print("\nList is Empty")

        else:
            key = int(input("\nEnter data to be deleted: "))
            ptr = self.head
            ptr1=ptr
            while ptr.data != key:
                ptr1=ptr
                ptr = ptr.next
            
            ptr2 = ptr.next
            ptr1.next = ptr2
            print(key,"is deleted from the list")

    def deleteBegin(self):
        if self.head is None:
            print("\nList is Empty")

        else:
            ptr = self.head
            self.head = ptr.next
            ptr.next = None
            print("First Element is Deleted from the List")

    def deleteEnd(self):
        if self.head is None:
            print("\nList is Empty")

        else:
            ptr = self.head
            while ptr.next.next is not None:
                ptr = ptr.next
            
            ptr.next = None
            print("Last Element is Deleted from the List")

obj = LinkedList()
while True:
    print("\n---- Menu ----")
    print("1. Append")
    print("2. Traverse")
    print("3. Add at Beginning")
    print("4. Add at Between")
    print("5. Delete Anywhere")
    print("6. Delete At Beginning")
    print("7. Delete At End")
    print("8. Exit")

    n = int(input("\nSelect any Choice: "))
    if n == 1:
        obj.append()

    elif n == 2:
        obj.traverse()

    elif n == 3:
        obj.addBegin()

    elif n == 4:
        obj.addBetween()

    elif n == 5:
        obj.deleteAnywhere()

    elif n == 6:
        obj.deleteBegin()

    elif n == 7:
        obj.deleteEnd()

    elif n == 8:
        sys.exit(0)

    else:
        print("Invalid choice. Please select a valid option")