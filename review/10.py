from tkinter import *

root = Tk()

main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
root.config(menu=main_menu)
root.mainloop()