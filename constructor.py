'''
class MyPython:
    def __init__(self):
        print("Constructor is Called")

    def func(self):
        print("Func Code Execution")

M = MyPython()
M.func()
'''

class MyPython:
    def __init__(self):
        print("First Constructor")

    def __init__(self):
        print("Second Constructor")

M = MyPython()