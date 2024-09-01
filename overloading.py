class Test:
    def __init__(self, *n):
        total = 0
        for x in n:
            total = total + x
        print(total)

T = Test()
T = Test(10)
T = Test(10,20)
T = Test(10,20,30)