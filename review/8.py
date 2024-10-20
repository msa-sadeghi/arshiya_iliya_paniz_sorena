# sports = {"arshia":"football", "paniz":"tennis", "ayrana":"basketball"}
# for i in range(2):
#     name = input("enter a name:> ")
#     s = input("enter a sport name:> ")
#     sports[name] = s

# print(sports)

# import turtle

# sc = turtle.Screen()
# name = turtle.textinput("student info", "enter a name: ")
# turtle.write(name, align="center", font=("arial", 28))
# turtle.ht()
# turtle.done()

import tkinter
from tkinter import Label, Entry, Button

def my_function():
    output.configure(text=name_entry.get())

root = tkinter.Tk()
root.geometry("250x100")
name_label = Label(root, text="نام  ")
name_label.pack(side="left")

name_entry = Entry(root)
name_entry.pack(side="left")

my_button = Button(root, text="تایید", command=my_function)
my_button.pack(side="left")

output = Label(root)
output.pack(side="left")
root.mainloop()