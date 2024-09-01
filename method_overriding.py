class Ambani:
    def __init__(self):
        print("Init")

    def properties(self):
        print("Properties")

    def bike(self):
        print("Splender")

class Child(Ambani):

    def bike(self):
        print("Bullet")

C = Child()
C.properties()
C.bike()