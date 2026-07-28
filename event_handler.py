from tkinter import *
window= Tk()
window.geometry('200x200')
window.title('eventhandler')
def handler(event):
    print(event.char)
window.bind('<Key>',handler)
def handleclick(event):
    print('\nYou clicked the button!')
button= Button(window, text= 'Click me!')
button.pack()
button.bind('<Button-1>',handleclick)
window.mainloop()