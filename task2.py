class Electricity:
    def __init__(self):
        self.c_id = input("Enter ID: ")
        self.c_name = input("Enter Name: ")
        self.c_unit = int(input("Enter Unit: "))
        self.bill = 0
        self.charges = 0
        self.totalbill = 0

    def Calculate(self):
        # Calculate bill based on the units consumed
        if self.c_unit <= 30:
            self.bill = self.c_unit * 1.50
        elif self.c_unit > 30 and self.c_unit <= 200:
            self.bill = self.c_unit * 3.00
        elif self.c_unit > 200 and self.c_unit <= 300:
            self.bill = self.c_unit * 3.50
        elif self.c_unit > 300:
            self.bill = self.c_unit * 4.25

        # Add additional charges if the bill exceeds 500
        if self.bill > 500:
            self.charges = self.bill * 0.15
            self.totalbill = self.bill + self.charges
        else:
            self.totalbill = self.bill

    def showInfo(self):
        # Display customer information and bill details
        print("Customer ID:", self.c_id)
        print("Customer Name:", self.c_name)
        print("Total Unit Consumed:", self.c_unit)
        print("Additional Charges:", self.charges)
        print("Total Bill Amount:", self.totalbill)

# Create an instance and use the methods
E = Electricity()
E.Calculate()
E.showInfo()
