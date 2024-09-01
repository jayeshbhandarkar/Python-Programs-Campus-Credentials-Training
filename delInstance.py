# the variable which is called using self is called as self variable

class MyPython:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def func(self):
        del self.d

M = MyPython()
print(M.__dict__)
M.func()
print(M.__dict__)
del M.c
print(M.__dict__)
