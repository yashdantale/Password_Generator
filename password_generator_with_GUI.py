from tkinter import *
import string
from secrets import choice
import random

root = Tk()
root.geometry("400x200")
root.title("Password Generator")
root.attributes("-toolwindow", 1)
root.resizable(width=FALSE, height=FALSE)

# pass length information
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

# pass length number
val = IntVar()
spinlength = Spinbox(root, from_=6, to_=32, textvariable=val, width=13).pack()

# passprint
def callback():
    lsum.config(text=passgen())

# clickable button
passgenButton = Button(root, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
elements = string.digits + string.ascii_letters + string.punctuation
password = "".join(choice(elements)for x in range(0,32))

def passgen():
        return "".join(random.sample(elements, val.get()))

root.mainloop()