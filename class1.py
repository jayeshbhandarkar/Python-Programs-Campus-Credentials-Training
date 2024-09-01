class Mobile:
    def __init__(self,ram,storage,price):
        self.ram = ram
        self.storage = storage
        self.__price = 100

    def set_price(self,amount):
        if 0<amount<500:
            self.__price += amount

    def get_price(self):
        return self.__price

# mob1 and mob2 are the reference variables
mob1 = Mobile('2gb','4gb',1000)
mob1.set_price(400)

print(mob1.ram, mob1.storage, mob1.get_price())
