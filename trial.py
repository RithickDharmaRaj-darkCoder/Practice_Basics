# Class And Object ...

class students():

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def info(self):
        print(self.name)
        self.__rollno()
    def __rollno(self):
        print(self.roll)

std1 = students('RDR','007')

