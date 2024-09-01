class Test:
    def __init__(self):
        print("No argument method")

    def __init__(self,a):
        print("One argument method : ",a)

    def __init__(self,a,b):
        print("Two argument method : ",(a+b))

#T = Test()
T = Test(10,30)