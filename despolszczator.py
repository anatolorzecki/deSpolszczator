# deSpolszczator 1.0

import os
from tkinter import *
import unicodedata

window = Tk()
window.title("deSpolszczator 1.0")
window.resizable(width=False, height=False)


def swapper():
    file_names = os.listdir(file_path.get())
    print(file_path.get())
    letter_swap(file_names)


def letter_swap(names):
    path = file_path.get()
    for name in names:
        old_name = name
        if name[:1] == '.':
            continue
        else:
            nfkd_form = unicodedata.normalize('NFKD', name).replace(u'ł', 'l').replace(u' ', '_')
            wo_pl_letters = nfkd_form.encode('utf-8', 'ignore').decode('ASCII', 'ignore')
            print(wo_pl_letters)
            os.rename(path+'\\'+old_name, path+'\\'+str(wo_pl_letters))

l1 = Label(window, text="Path to execute:")
l1.grid(row=0, column=0)

file_path = StringVar()
e1 = Entry(window, textvariable=file_path)
e1.grid(row=0, column=1, columnspan=5)
file_path.set("")

b1 = Button(window, text="Clean", command=swapper)
b1.grid(row=0, column=6)

window.mainloop()
