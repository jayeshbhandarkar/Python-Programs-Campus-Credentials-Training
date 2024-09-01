class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def showCountObject(cls):
        print("The Number of Objects are created ", cls.count)

t1 = Test()
t2 = Test()
Test.showCountObject()

t3 = Test()
t4 = Test()
Test.showCountObject()