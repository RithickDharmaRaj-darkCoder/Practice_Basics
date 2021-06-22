# Class And Object ...

class StudentInfo():
    college = 'vvit'
    def __init__(self,stdname,dept,year,regno):
        self.name = stdname
        self.dept = dept
        self.year = year
        self.rollno = regno
    def stdinclg(self):
        print(self.name,self.dept,self.year,self.rollno)

class StudentInfo(StudentInfo):

    def stdinhome(self):
        print(self.name,self.dept,self.college)

StudentInfo('Mr_17','CSE','Final',6128_17_104_008).stdinclg()
StudentInfo('Mr_17','CSE','Final',00).stdinhome()