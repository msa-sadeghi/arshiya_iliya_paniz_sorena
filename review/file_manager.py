# tkinter
# shutil
# os
# easygui
from tkinter import *
import shutil
import os
from tkinter import messagebox, filedialog
import easygui


def file_open_box():
    path = easygui.fileopenbox()
    return path


def directory_open_box():
    path = filedialog.askdirectory()
    return path


def open_file():
    path = file_open_box()
    os.startfile(path)


def copy_file():
    path1 = file_open_box()
    path2 = directory_open_box()
    try:
        shutil.copy(path1, path2)
        messagebox.showinfo('موفق', 'فایل با موفقیت کپی شد')
    except:
        messagebox.showinfo('خطا', 'فایل با موفقیت کپی نشد')


window = Tk()
window.title("برنامه من")
window.configure(bg="black")
window.geometry("300x380")
Label(window, text="چه کاری می خواهید انجام دهید؟").pack()
Button(window, text='بازکردن فایل', command=open_file).pack()
Button(window, text='کپی فایل', command=copy_file).pack()

window.mainloop()
