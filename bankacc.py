import sys
class BankAccount:
    def __init__(self):
        self.name=None
        self.accno=None
        self.balance=None

    def inputData(self):
        self.name = input("Enter Name: ")
        self.accno = input("Enter Account No: ")
        self.balance = int(input("Enter Balance: "))

    def showInfo(self):
        print("Name of Account Holder: ",self.name)
        print("Account No: ",self.accno)
        print("Balance: ",self.balance)

    def deposit(self):
        amt = int(input("Enter Amount: "))
        self.balance+=amt

    def withdraw(self):
        amt = int(input("Enter Amount: "))
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")

class SavingAccount(BankAccount):
    def withdraw(self):
        amt = int(input("Enter Amount: "))
        if self.balance-amt < 1000:
            print("Can't withdraw Money")
        else:
            self.balance -= amt

bank = SavingAccount()

while True:
    print("\n")
    print("1. Input Data")
    print("2. Display Data")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    print("\n")
    ch = int(input("Enter Any Choice: "))
    if ch==1:
        bank.inputData()

    elif ch==2:
        bank.showInfo()

    elif ch==3:
        bank.deposit()

    elif ch==4:
        bank.withdraw()

    elif ch==5:
        sys.exit()

    else:
        print("Invalid Input")
