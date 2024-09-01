class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def setPercentage(self,percentage):
        self.percentage = percentage

    def getPercentage(self):
        return self.percentage
    
n = int(input("Enter No of Student: "))
s = Student()

for i in range(n):
    name = input("Enter Student Name: ")
    s.setName(name)

    percentage = int(input("Enter Student Percentage: "))
    s.setPercentage(percentage)

    print("Hi", s.getName(),"Your Percentage is : ",s.getPercentage())
    print()



# A class whose all the data members as private then it is called as tightly encapsulation
# By using mangling we can acces private data members