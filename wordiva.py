from tkinter import *
import json
from tkinter import messagebox
from difflib import get_close_matches

pg = Tk()
pg.geometry("570x450")
pg.title("Wordiva - English Dictionary")
pg.configure(background='blue')
pg.iconbitmap("word.ico")
userin = " "

elements = json.load(open("wordbook.json"))
userin = " "


def wordm():
    a = elements.keys()
    userin = e1.get()
    if userin.lower() in elements:
        t1.delete("1.0", END)
        s = '\n->'.join(elements[userin.lower()])
        t1.insert(END, s)
    elif userin.upper() in elements:
        t1.delete("1.0", END)
        t = '\n'.join(elements[userin.upper()])
        t1.insert(END, t)

    elif len(get_close_matches(userin, a)) > 0:
        b = get_close_matches(userin, a)[0]
        t1.delete("1.0", END)
        c = "Are you looking for --> %s <-- instead,type(y/n) in 2nd box" % b
        d = "Sorry try another word please"
        e = "Please try again"
        t1.insert(END, c)
        userin1 = e2.get()

        if userin1.lower() == "y":
            t1.delete("1.0", END)
            u = '(Or)'.join(elements[b])
            t1.insert(END, u)
        elif userin1.lower() == "n":
            t1.delete("1.0", END)
            t1.insert(END, d)

    else:
        messagebox.showinfo("Error", "Sorry try another word please")


def reset():
    e1.delete(0, END)
    e2.delete(0, END)


lb1 = Label(pg, text="What word do you want to look up? Type Here ---->",
            background='white', fg='black')
lb1.grid(row=0, column=0, padx=10, pady=10)

entry = StringVar()
e1 = Entry(pg, width=40, textvariable=entry)
e1.grid(row=0, column=1, padx=10, pady=10)

lb2 = Label(pg, text="Type(Y/N)If you mistyped a wrong word--->",
            background='white', fg='black')
lb2.grid(row=2, column=0, padx=10, pady=10)

entry1 = StringVar()
e2 = Entry(pg, width=40, textvariable=entry1)
e2.grid(row=2, column=1, padx=10, pady=10)

lb2 = Label(pg, text="---->                          <-----",
            background='white', fg='black')
lb2.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(pg, text="Submit", background="light green",
            fg="blue", command=wordm)
b1.grid(row=3, column=0, ipadx=5, ipady=5)

lb3 = Label(pg, text="---->                          <-----",
            background='white', fg='black')
lb3.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(pg, text="Clear", background="Red", fg="white", command=reset)
b2.grid(row=3, column=1, ipadx=5, ipady=5)

t1 = Text(pg, height=11, width=36, font="tahoma 20", fg="#120E43")
t1.grid(row=5, column=0, columnspan=2)


pg.mainloop()
