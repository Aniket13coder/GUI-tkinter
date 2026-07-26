from tkinter import *
window= Tk()
window.title('Number pad')
window.geometry('500x500')
num= [[9,8,7],[6,5,4],[3,2,1],['*',0,'#']]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize= 70)
    window.rowconfigure(i,weight= 1,minsize= 50)
    for j in range(3):
        frame= Frame(master= window, relief= RAISED,borderwidth= 2)
        frame.grid(row=i,column=j)
        hwlabel= Label(master= frame, text= num[i][j])
        hwlabel.pack()
window.mainloop()