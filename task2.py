class Electricity:
    def __init__(self):
        self.c_id = input("Enter ID: ")
        self.c_name = input("Enter Name: ")
        self.c_unit = int(input("Enter Unit: "))
        self.bill = 0
        self.charges = 0
        self.totalbill = 0

    def Calculate(self):
        bill = 0

        if self.unit <= 30:
            self.bill = self.unit*1.50

        elif self.unit>30 and self.unit<=200:
            self.bill = self.unit*3.00

        elif self.unit>200 and self.unit<=300:
            self.bill = self.unit*3.50

        elif self.unit>300:
            self.bill = self.unit*4.25

        if bill>500:
            self.charges = self.bill*0.15
            self.totalbill = self.charges+self.bill

    def showInfo(self):
        print("Customer ID",self.c_id)
        print("Customer Name",self.c_name)
        print("Total Unit",self.c_unit)
        print("Add Charges",self.charges)
        print("Gross Bill",self.totalbill)

E = Electricity()
E.inputData()
E.showInfo()