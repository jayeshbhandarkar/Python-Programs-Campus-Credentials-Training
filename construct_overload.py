class Test:
    def __init__(self, a=None, b=None, c=None):
        print("Constructor with 0,1,2,3 arguments",a,b,c)

T = Test()
T = Test(10)
T = Test(10,20)
T = Test(10,20,30)
