class Mobile:
    # __init__ is an constructor => init method
    def __init__(self,ram,storage,price):
        # self => parameter which will refer to the object 
        
        # Instance Attributes
        self.ram = ram
        self.storage = storage
        self.cost = price

    def set_price(self,amount):
        if 0<amount<500:
            self.price += amount

# mob1 and mob2 are the reference variables
mob1 = Mobile('2gb','4gb',1000)
mob1.cost +=700

mob2 = Mobile('6gb','64gb',5000)

print(mob1.ram, mob1.storage, mob1.cost)
print(mob2.ram, mob2.storage, mob2.cost)
print(type(mob1))