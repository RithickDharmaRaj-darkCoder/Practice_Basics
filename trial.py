# practice section...
# Inheritance...

# Declarating Classes...
class sum():
    def __init__(self):
        print("Init 1")
    def add1(self):
        print('Addition 1')
    def add2(self):
        print('Addition 2')

class sub(sum):
    def __init__(self):
        print("Init 2")
    def sub1(self):
        super().add1()
        print('Subtraction 1')
    def subt2(self):
        print('Subtraction 2')

# Oject Declarating...
obj = sub()
obj1 = sub()

# Calling Methods...
obj1.sub1()