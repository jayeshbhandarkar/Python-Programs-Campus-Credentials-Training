# Delete middle element of a stack

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def traverse(self):
        print("Stack elements:", self.stack)

def delete_middle(stack, current_index, middle_index):
    if stack.isEmpty():
        return

    top = stack.pop()

    if current_index != middle_index:
        delete_middle(stack, current_index - 1, middle_index)
        stack.push(top)

def delete_middle_element(stack):
    middle_index = stack.size() // 2
    delete_middle(stack, stack.size() - 1, middle_index)

stack = Stack()

elements = [1, 2, 3, 4, 5]
for element in elements:
    stack.push(element)

print("---- Original Stack ----")
stack.traverse()

delete_middle_element(stack)

print("\n---- Stack after deleting the middle element ----")
stack.traverse()
