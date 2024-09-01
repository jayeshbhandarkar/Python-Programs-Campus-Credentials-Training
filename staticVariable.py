class MyPython:
    x = 10                             # Static Variable
    def __init__(self):
        self.y = 20                    # Instance Variable+``

M1 = MyPython()
M2 = MyPython()
print("M1 ==>> ", M1.x, M1.y)
print("M2 ==>> ", M2.x, M2.y)

MyPython.x = 111
M1.y = 222

print("M1 ==>> ", M1.x, M1.y)
print("M2 ==>> ", M2.x, M2.y)