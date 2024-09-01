class Test1:
    _b = None
    __c = None

    def __init__(self):
        self.a = 101
        self.b = 201
        self.c = 301

    def show1(self):
        print("A = ",self.a)
        print("B = ",self._b)
        print("C = ",self.__c)

class Test2(Test1):
    def show2(self):
        print("A = ",self.a)
        print("B = ",self._b)
        print("C = ",self._Test1__c)

class Test3(Test2):
    def show3(self):
        print("A = ",self.a)
        print("B = ",self._b)

T = Test1()
T.show1()
T1 = Test2()
T1.show2()
T2 = Test3()
T2.show3()