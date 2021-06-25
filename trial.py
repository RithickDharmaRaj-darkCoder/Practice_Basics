# Class And Object ...

class car:
    __speed = 0
    __name = ' '
    def __init__(self):
        self.__speed = 200
        self.__name = "Normal Car"
    def changename(self,name):
        self.__name = name
    def changespeed(self,speed):
        self.__speed = speed
    def carinfo(self):
        print(f'{self.__name}\n{self.__speed}')

tata = car()
tata.changename('TATA')
tata.carinfo()
