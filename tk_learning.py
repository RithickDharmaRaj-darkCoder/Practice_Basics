# Learning Tkinter ...

from tkinter import *
main = Tk()

title = Label(main,text='***  AADHAAR MANAGEMENT  ***')
title.pack()

name = Entry(main)
name.pack()
name.insert(2,'Enter Your Name...')

def clickme():
    label = Label(main,text=f'Hi! {name.get()}, u have successfully submitted ur data.')
    label.pack()
btn1 = Button(main,text='Sumbit',command=clickme)
btn1.pack()


main.mainloop()