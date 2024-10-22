from tkinter import *

root = Tk()

selected_value = IntVar()

r1 = Radiobutton(root, value="football", text="football", variable=selected_value)
r1.pack(anchor="w")
r1 = Radiobutton(root, value="basketball", text="basketball", variable=selected_value)
r1.pack(anchor="w")
r1 = Radiobutton(root, value="baseball", text="baseball", variable=selected_value)
r1.pack(anchor="w")


root.mainloop()