# TypeError: Can't instantiate abstract class MyPython with abstract methods m1, m2
"""from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class MyPython(Test):
    pass

M = MyPython()"""

# --------------------------------------------------------------------------------------------------------

"""from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class MyPython(Test):
    def m1(self):
        print("M1 Method Implementation")

    def m2(self):
        print("M2 Method Implementation")

M = MyPython()
M.m1()
M.m2()"""

# --------------------------------------------------------------------------------------------------------

"""from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        print("M2 Method Implementation")

class MyPython(Test):
    def m1(self):
        pass

class Child(MyPython):
    def m1(self):
        print("M1 Method Implementation")

M = Child()
M.m1()
M.m2()"""

# --------------------------------------------------------------------------------------------------------

# Inside the abstract class we can declare the constructor abstract class constructor is executed but object is 
# not created.

from abc import ABC, abstractmethod

class Test(ABC):
    def __init__(self):
        print("Constructor is called...")

    @abstractmethod
    def m1(self):
        pass

class MyPython(Test):
    def m1(self):
        print("M1 Method Implemented")

M = MyPython()
M.m1()