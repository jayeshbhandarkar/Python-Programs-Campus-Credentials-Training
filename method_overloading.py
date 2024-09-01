class MyPython:
    def sum(self,*n):
        total = 0
        for x in n:
            total = total + x

        print("Sum = ",total)

M = MyPython()
M.sum(10,20,30,40)
M.sum(10,20,30)
M.sum(10,20)
M.sum(10)
M.sum()
