from tkinter import *

window = Tk()
window.title("My Profile Card")
window.geometry("600x400")

label = Label(window, text = "My Profile Card", bg = "#AB27D0", fg = "#000000")
label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

name = Label(window, text = "Name", bg = "#CD6DE8", fg = "#000000")
name.grid(row = 1, column = 0, padx = 10, pady = 10)

name_entry = Entry(window, bg = "#D557FF", fg  ="#000000")
name_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

hobby = Label(window, text = "Hobby", bg = "#CD6DE8", fg = "#000000")
hobby.grid(row = 2, column = 0, padx = 10, pady = 10)

hobby_entry = Entry(window, bg = "#D557FF", fg = "#000000")
hobby_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

frame = Frame(window, bg = "#AB27D0", height = 5)
frame.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)

about_label = Label(frame, text = "About Me:", bg = "#AB27D0", fg = "#000000")
about_label.pack(side = TOP)

about_text = Text(frame, bg = "#DCB5EE", fg = "#000000", height = 2)
about_text.pack()

def display():
    n = name_entry.get()
    h = hobby_entry.get()

    details = f"Hi! My name is {n}.\nMy hobby is {h}."

    about_text.delete(1.0, END)
    about_text.insert(END, details)

button = Button(window, text = "View My Profile", command = display, bg = "#9900FF", fg = "#000000")
button.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

window.mainloop()