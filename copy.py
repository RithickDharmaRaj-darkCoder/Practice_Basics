# 11'O Clock Study ...

#


class calci:
    def __init__(self,a,b):
        self.num = a
        self.b = b
        print(a*b)

    def add(self):
        print(self.num + self.b)

    def sub(self):
        print(self.num - self.b)

cal1 = calci(10,20)
cal2 = calci(2,5)


cal1.add()
cal2.sub()