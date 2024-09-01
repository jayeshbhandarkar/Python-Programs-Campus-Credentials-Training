class Employee:
    def __init__(self, no, name, sal):
        self.eno = no
        self.ename = name
        self.esal = sal

    def showDetails(self):
        print("\n")
        print("Employee No : ",self.eno)
        print("Employee Name : ",self.ename)
        print("Employee Salary : ",self.esal)

class Test:
    def update(Employee):
        Employee.esal = Employee.esal + 8000
        print("\n")
        print("Your Salaray is Updated")
        Employee.showDetails()

E = Employee(721, "Jayesh", 20000)
E.showDetails()
Test.update(E)