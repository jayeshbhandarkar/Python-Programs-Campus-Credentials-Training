'''class Person:
    def __init__(self):
        self.pid = 61
        self.name = "Jayesh"
        self.city = "Dhule"

    def show(self):
        print("Pid= ",self.pid)
        print("Name = ",self.name)
        print("City = ",self.city)

P = Person()
P.show()
'''


# Person P;                     // Static Object in C++
# Person *p = new Person;       // Dynamic Object in C++
# Person P = new Person();      // Object in Java
# P = Person()                  // Object in Python


'''class Person():
    def __init__(self,id,n,c):
        self.pid = id
        self.name = n
        self.city = c

    def show(self):
        print("Pid= ",self.pid)
        print("Name = ",self.name)
        print("City = ",self.city)

P = Person(61, "Jayesh", "Pune")
P.show()'''


'''class Person:
    def __init__(self):
        self.pid = None
        self.name = None
        self.city = None

    def inputData(self):
        self.pid = input("Enter Id: ")
        self.name = input("Enter Name: ")
        self.city = input("Enter City: ")

    def show(self):
        print("Pid = ",self.pid)
        print("Name = ",self.name)
        print("City = ",self.city)

P = Person()
P.inputData()
P.show() '''



class Person:
    def __init__(self, id, n, c):
        self.pid = id
        self.name = n
        self.city = c

    def show(self):
        print("Pid = ",self.pid)
        print("Name = ",self.name)
        print("City = ",self.city)

id = input("Enter Id: ")
name = input("Enter Name: ")
city = input("Enter City: ")

P = Person(id, name, city)
P.show()