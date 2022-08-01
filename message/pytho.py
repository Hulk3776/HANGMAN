# import tkinter as tk
# from tkinter import simpledialog

# application_window = tk.Tk()

# answer = simpledialog.askstring("Input", "What is your first name?",
#                                 parent=application_window)

# print(answer)

# from tkinter import * 
        
# def show():
#     p = password.get() #get password from entry
#     print(p)
        
    
# app = Tk()   
# password = StringVar() #Password variable
# passEntry = Entry(app, textvariable=password, show='*')
# submit = Button(app, text='Show Console',command=show)

# passEntry.pack() 
# submit.pack()      

# app.mainloop()

# import tkinter as tk
# from tkinter.simpledialog import askstring
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.withdraw()
# password = askstring('Password', 'Enter password:', show="*")
# showinfo('Show password', 'password input: {}'.format(password))


# from tkinter import Tk
# from tkinter.simpledialog import Dialog


# class MyDialog(Dialog):
#     def __init__(self, parent, title=None, width=300, height=200):
#         # all variables should be initialized before calling 
#         # `super` because it calls .wait_window
#         self.width = width
#         self.height = height
#         super().__init__(parent, title)

#     def body(self, master):
#         self.geometry(f'{self.width}x{self.height}')


# root = Tk()
# root.withdraw()

# MyDialog(root)

from tkinter import *
from tkinter import simpledialog

class MyDialog(simpledialog.Dialog):

    def body(self, master):

        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        return first

root = Tk()
d1 = MyDialog(root)
d1.apply()

