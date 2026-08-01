from tkinter import *
from datetime import date
window = Tk()
window.title('Workshop Participant Greeting')
window.geometry('500x500')
lbl = Label(text="Hi!", bg="#2E4158",)
name_lbl = Label(text="Full Name", bg="#3895D3")
n_entry = Entry()
def display():
	name = n_entry.get() 
	global message
	message = "Welcome to the Workshop! \nToday's date is: "
	greet = "Hello "+name+"\n"
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())
text_box = Text(height=30)
btn = Button(text="Check In", command=display, bg="#6E0523", fg="#ff5353")
lbl.pack()
name_lbl.pack()
n_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()