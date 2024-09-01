class StackDemo:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            return self.stack.pop()

def reverse_string_using_stack(s):
    stack = StackDemo()

    for char in s:
        stack.push(char)
    
    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()
    
    return reversed_string

data = input("Enter any String: ")
reversed_string = reverse_string_using_stack(data)
print("Reversed String:", reversed_string)
