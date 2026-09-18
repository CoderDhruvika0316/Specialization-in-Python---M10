from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Introduction")
window.geometry("500x500")
window.configure(bg = "lavender")

image = Image.open("DC Picture.jpg")
image = image.resize((300, 300))

photo = ImageTk.PhotoImage(image)
photograph = Label(window, image = photo)
photograph.pack()

greeting = Label(window, text = "Hey there!\nWelcome to the Denomination Calculator Application!", font = ("Garamond", 15), fg = "black")
greeting.pack()

def message():
    confirm = messagebox.showinfo("Confirmation", "Are you sure you want to start your work with the Denomination Calculator?")

    if confirm == "ok":
        top_window()

start = Button(window, text = "Ready to Start?", command = message, bg = "pink", fg = "black", width = 30)
start.pack()

def top_window():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("600x600")
    top.configure(bg="pink")

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)

    heading = Label( top, text="DENOMINATION CALCULATOR", font=("ALGERIAN", 15), fg="black", bg="purple", width=40)
    heading.grid( row=0, column=0, columnspan=2, padx=5, pady=20)

    amount_label = Label( top, text="Enter your amount:", font=("Garamond", 18), bg="pink")
    amount_label.grid( row=2, column=0, padx=5, pady=5)

    amount = Entry(top)
    amount.grid( row=2, column=1, padx=5, pady=5)

    note_1 = Label(top,text="Notes of 500",font=("Garamond", 15),bg="pink")
    note_1.grid(row=3,column=0,padx=5,pady=5)

    note_2 = Label(top,text="Notes of 200",font=("Garamond", 15),bg="pink")
    note_2.grid(row=4,column=0,padx=5,pady=5)

    note_3 = Label(top,text="Notes of 100",font=("Garamond", 15),bg="pink")
    note_3.grid(row=5,column=0,padx=5,pady=5)

    note_1_entry = Entry(top)
    note_1_entry.grid(row=3,column=1,padx=5,pady=5)

    note_2_entry = Entry(top)
    note_2_entry.grid(row=4,column=1,padx=5,pady=5)

    note_3_entry = Entry(top)
    note_3_entry.grid(row=5,column=1,padx=5,pady=5)

    def calculation():
        try:
            money = int(amount.get())

            note_500 = money // 500
            money %= 500

            note_200 = money // 200
            money %= 200

            note_100 = money // 100

            note_1_entry.delete(0, END)
            note_2_entry.delete(0, END)
            note_3_entry.delete(0, END)

            note_1_entry.insert(END, str(note_500))
            note_2_entry.insert(END, str(note_200))
            note_3_entry.insert(END, str(note_100))

        except ValueError:
            messagebox.showerror("Alert","Kindly enter a valid value.")

    calculate = Button(top,text="Calculate",command=calculation,bg="purple",fg="black")

    calculate.grid(row=1,column=0,columnspan=2,padx=5,pady=10)



    top.mainloop()

window.mainloop()