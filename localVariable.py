class Test:
    def func1(self):
        a = 100
        print(a)

    def func2(self):
        b = 222
        a = 666
        print(b)
        print(a)

T = Test()
T.func1()
T.func2()