# Class And Object ...

class StudentInfo:
    def __init__(self,stdname,dept,year,regno):
        self.name = stdname
        self.dept = dept
        self.year = year
        self.rollno = regno
    def display(self):
        print(f'Hi, i\'m {self.name} studying {self.year} year-{self.dept} and my register number is {self.rollno}.')

totalstd = int(input('Total no.of Students : '))
for i in range(totalstd):
    std = StudentInfo(input(f'Student{i+1} Name : '),
                input('Department : '),
                input('Year : '),
                input('Register No. : '))
print("Data Saved!")

std.display()