class Mobile:
    def __init__(self):
        self.ram = None
        self.storage = None
        self.__price = None

    def set_price(self,amount):
        if 0<amount<500:
            self.__price = amount

    def get_price(self):
        return self.__price

# mob1 and mob2 are the reference variables
mob1 = Mobile()
mob1.ram = "2gb"
mob1.storage = "4gb"
mob1.__price = 300

print(mob1.ram, mob1.storage, mob1.__price)
