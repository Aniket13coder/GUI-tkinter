from tkinter import *
window= Tk()
window.geometry('500x500')
window.title('Main window')
    
def topwin():
    top= Toplevel()
    top.geometry('300x300')
    top.title('Top window')
    lbl= Label(top, text= 'This is the top window!!')
    lbl.pack()
    def secret():
        lb= Label(top, text= 'Hello world')
        lb.pack()
    Btn= Button(top, text= 'click for secret message', command= secret)
    Btn.pack()
    top.mainloop()
whylbl= Label(window, text= 'Hi this is the main window press the button below!', bg= "#0014c7", fg= "#009dff")
btn1= Button(window, text= 'click for new window', command= topwin,bg= "#067070", fg= "#00ffd5")
whylbl.pack()
btn1.pack()
window.mainloop()

