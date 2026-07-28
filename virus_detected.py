from tkinter import *
from tkinter import messagebox
window= Tk()
window.geometry('500x500')
window.title('Virus detecter')
def msg():
    messagebox.showwarning('Alert','Just kidding!!!')
button= Button(window, text= 'Scan for virus', command= msg)
label= Label(text= 'Welcome to the virus detecter!!!')
label.pack()
button.pack()
window.mainloop()