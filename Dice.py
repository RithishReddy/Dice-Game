import random
from tkinter import *
from tkinter import messagebox

master = Tk()
master.geometry("500x500")
master.title("Roll The Dice")


def clicked():
    var = random.randint(1, 10)
    value = v.get()
    if value == 1:
        if var < 7:
            messagebox.showinfo("Message", "You Won")
        else:
            messagebox.showinfo("Message", "Ooops !  Try again")

    if value == 2:
        if var == 7:
            messagebox.showinfo("Message", "You Won")
        else:
            messagebox.showinfo("Message", "Ooops !  Try again")

    if value == 3:
        if var > 7:
            messagebox.showinfo("Message", "You Won")
        else:
            messagebox.showinfo("Message", "Ooops !  Try again")


heading = Label(master,
                text="Welcome to the Dice game",
                fg="red",
                bg="light green",
                font="Times 25").place(relx = 0.18, rely = 0)
v = IntVar(master, 1)
rad1 = Radiobutton(master, text="Less than 7",
                   background="light blue", indicator=0, variable=v,
                   value=1).place(relx = 0.3, rely = 0.2)
rad2 = Radiobutton(master, text="Equal to 7",
                   background="light blue", indicator=0, variable=v,
                   value=2).place(relx = 0.45, rely = 0.2)
rad3 = Radiobutton(master, text="Greater than 7",
                   background="light blue", indicator=0, variable=v,
                   value=3).place(relx = 0.6, rely = 0.2)

button1 = Button(master, text="Roll", height=2, width=10, bg='#0052cc', fg='#ffffff',
                 command=clicked).place(relx = 0.45, rely = 0.3)

master.mainloop()
