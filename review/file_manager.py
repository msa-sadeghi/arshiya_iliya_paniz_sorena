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


def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo('موفق', 'فایل با موفقیت حذف گردید')
    except:
        messagebox.showinfo('ناموفق', 'خطا رخ داده است')

def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extension = os.path.splitext(file)[1]
        new_name = input("enter the new name:> ")
        path2 = os.path.join(path1, new_name+ extension)
        os.rename(file, path2)
    except:
        messagebox.showinfo('ناموفق', 'خطا رخ داده است')


window = Tk()
window.title("برنامه من")
window.configure(bg="black")
window.geometry("300x380")
Label(window, text="چه کاری می خواهید انجام دهید؟").pack()
Button(window, text='بازکردن فایل', command=open_file).pack()
Button(window, text='کپی فایل', command=copy_file).pack()
Button(window, text='حذف فایل', command=delete_file).pack()
Button(window, text='تغییر نام فایل', command=rename_file).pack()

window.mainloop()


