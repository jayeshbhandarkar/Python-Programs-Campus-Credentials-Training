import sys

class StackDemo:
    def __init__(self):
        self.top=-1
        self.stack=[]
        self.size=10

    def isEmpty(self):
        if self.top == self.top-1:
            return True
        else:
            return False

    def isFull(self):
        if  self.top == self.size-1:
            return True
        else:
            return False

    def push(self):
        if self.isFull():
            print("\nStack is Full")
        else:
            self.top+=1
            self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print("\nStack is Empty")
        else:
            self.top-=1
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            print("\nStack is Empty")
            return None
        else:
            return self.stack[self.top]

    def traverse(self):
        if self.isEmpty():
            print("\nStack is Empty")
        else:
            print("\nStack elements:", self.stack)

if __name__ == "__main__":
    Obj = StackDemo()

    while True:
        print("\n")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        n = int(input("\nSelect any Choice: "))

        if n==1:
            data= int(input("\nEnter Element to push in the Stack: "))
            data= Obj.push()
            print("\nElement inserted successfully")

        elif n == 2:
            result = Obj.pop()
            if result is not None:
                print("\nElement deleted successfully:", result)

        elif n == 3:
            result = Obj.peek()
            if result is not None:
                print("\nTop Element is:", result)

        elif n == 4:
            Obj.traverse()

        elif n == 0:
            sys.exit(0)

        else:
            print("\nInvalid choice. Please select a valid option")
