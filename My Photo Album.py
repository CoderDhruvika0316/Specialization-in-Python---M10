from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Photo Album")
window.geometry("400x500")

title = Label(window, text = "My Photo Album", bg = "pink", fg = "black", width = 40)
title.pack(side = TOP)

image = Image.open("MPA Picture.png")
image = image.resize((350, 350))

photo = ImageTk.PhotoImage(image)

photgraph = Label(window, image = photo)
photgraph.pack(side = TOP)

def message():
    messagebox.showinfo("Reaction", "Great! You clicked on the button to react!!")

reaction = Button(window, text = "Click to React", command = message, bg = "purple", fg = "black")
reaction.pack(side = TOP)

def display():
    top = Toplevel()
    top.title("Information")
    top.geometry("400x100")

    label = Label(top, text = "Picture Person: My pet cat Lili")
    label_2 = Label(top, text = "Picture Location: My garden")
    label_3 = Label(top, text = "Picture Person Age: 5 years old")

    label.pack()
    label_2.pack()
    label_3.pack()

    top.mainloop()

info = Button(window, text = "See Information", command = display, bg = "#FF0062", fg = "#000000")
info.pack(side = TOP)

window.mainloop()
