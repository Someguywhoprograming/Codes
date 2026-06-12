from tkinter import *

root = Tk()

root.geometry("500x500")

title = Label(root, text="Please Login")
    #font="arial 20 bold")
title.pack(padx=10, pady=20)

name_text = Label(root, text="Enter Username")
username = Entry(root, font="arial 20").pack()

pass_text = Label(root, text="Enter Password").pack()
password = Entry(root, font="arial 20").pack()

btn = Button(text="Login", font="arial 15", width=27).pack(pady=20)
root.mainloop()