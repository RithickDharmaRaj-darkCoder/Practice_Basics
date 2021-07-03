# Learning Tkinter ...
from tkinter import *
import random
aadhaarno = random.randint(1000_0000_0000_0000,9999_9999_9999_9999)
def create_btn():
    name_iputinfo = name.get()
    age_iput = age.get()
    mobile_info = mobile.get()
    print(f"Created Aadhaar Successfully!\n{name_iputinfo}\n{age_iput}\n{mobile_info}")
    aadhaarno1 = str(aadhaarno)
    print(f'{aadhaarno1[0:4]} {aadhaarno1[4:8]} {aadhaarno1[8:12]} {aadhaarno1[12:]}')

screen = Tk()
screen.title('Aadhaar Management System')
screen.geometry('500x600')

# Label Section ...
heading = Label(text = ' AADHAAR  MANAGEMENT  SYSTEM ',bg='navyblue',fg='white',height=3,width=500)
heading.pack()
name = Label(text='Enter Your Name ',fg='blue')
name.place(x=20,y=100)
age = Label(text='Enter Your Age ',fg='blue')
age.place(x=20,y=150)
mobilNo = Label(text='Enter Your Mobile.No ',fg='blue')
mobilNo.place(x=20,y=200)

# Datatype section ...
name = StringVar()
age = IntVar()
mobile = IntVar()

# Input Entry Section ...
name_iput = Entry(textvariable=name)
name_iput.place(x=170,y=100,width=200)
age_iput = Entry(textvariable=age)
age_iput.place(x=170,y=150,width=200)
mobile_iput = Entry(textvariable=mobile)
mobile_iput.place(x=170,y=200,width=200)

# Button Section ...
submit = Button(text='CREATE',bg='green',fg='White',borderwidth=3,command=create_btn)
submit.place(x=270,y=250,width=100)





screen.mainloop()