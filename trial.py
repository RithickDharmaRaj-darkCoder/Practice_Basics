# Python Learning Field ...

# Creating Class in Advance ...

# creating Attributes to the class ...
def init(self,num1,num2):
    self.a = num1
    self.b = num2
    addition(self)
    subtraction(self)

def addition(self):
    print(f'Addition : {self.a + self.b}')

def subtraction(self):
    print(f'Subtraction : {self.a - self.b}')

# Creating class by using type() method ...
calci = type('Calci',(),{'__init__':init,'add':addition,'sub':subtraction})

# Creating objects to the class ...
task1 = calci(3,5)
print(type(calci))