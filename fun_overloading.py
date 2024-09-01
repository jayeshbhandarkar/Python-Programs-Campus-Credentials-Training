class Test:
    def fun(self):
        print("No argument method")

    def fun(self,a):
        print("One argument method : ",a)

    def fun(self,a,b):
        print("Two argument method : ",a+b)

T = Test()
T.fun(10,20)