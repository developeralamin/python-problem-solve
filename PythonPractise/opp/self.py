class ATM:
    def booth(self,name):
        self.name = name
        print("Booth name is",name)

data = ATM()
data.booth("Pallabi")
# print(dir(data.booth("d")))