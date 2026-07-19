from tkinter import *
from datetime import date
window= Tk()
window.geometry('500x500')
window.title('testing widgets!')
labl= Label(text= 'Hey there!',fg= "#E70505",bg= "#f68181")
nlabel= Label(text= 'Full name', fg= "#09ff4e",bg= "#8eff98")
nentry= Entry()
def display():
    name= nentry.get()
    global message
    message= 'Hello welcome to my first window!\nTodays date is: '
    greet= f'Hi! {name}\n'
    tbox.insert(END,greet)
    tbox.insert(END,message)
    tbox.insert(END,date.today())
tbox= Text(height= 9)
btn= Button(text= 'Begin',command= display,height= 2,fg= "#00fbff",bg= "#0050b1")
labl.pack()
nlabel.pack()
nentry.pack()
btn.pack()
tbox.pack()
window.mainloop()