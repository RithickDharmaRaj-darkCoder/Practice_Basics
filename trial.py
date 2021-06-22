# Class And Object ...

class StudentInfo:
    def __init__(self,stdname,dept,year,regno):
        self.name = stdname
        self.dept = dept
        self.year = year
        self.rollno = regno
        print('Data Saved Successfully!',end=" ")
    def display(self):
        print(f'Hi, i\'m {self.name} studying {self.year} year-{self.dept} and my register number is {self.rollno}.')

StudentInfo('Rithick Dharma Raj','CSE','Final',regno=6128_17_104_008)
StudentInfo('Rithick Dharma Raj','CSE','Final',regno=6128_17_104_008).display()

std1 = StudentInfo('Rithick Dharma Raj','CSE','Final',regno=6128_17_104_008)
std1.display()
std2 = StudentInfo('Dharma Raj','ECE','Final',regno=6128_17_106_000).display()