class Team:
    def __init__(self,cn, pn, m, a, ba, bo):
        self.country_name = cn
        self.nameofPlayer = pn
        self.no_of_matches = m
        self.age = a
        self.batting_avg = ba
        self.balling_avg = bo

    def show(self):
        print(self.country_name,"\t\t\t\t",self.nameofPlayer,"\t\t\t\t",self.no_of_matches,"\t\t\t\t",self.age,
              "\t\t\t\t",self.batting_avg,"\t\t\t\t",self.balling_avg)
        
print("Country Name","\t\t","Name of Player","\t\t","No of Matches","\t\t","Age","\t\t","Batting Average","\t\t","Balling Average")

T1 = Team("India", "Sachin", 295, 30, 45.51, 53.00)
T2 = Team("Australia", "Ricky",  160, 28, 41.00, 67.00)
T3 = Team("India", "Saurav", 230, 31, 40.95, 30.00)

T1.show()
T2.show()
T3.show()