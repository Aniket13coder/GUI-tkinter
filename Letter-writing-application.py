from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
window= Tk()
window.title('Letter writing application')
window.geometry('500x500')
window.rowconfigure(0,minsize= 500,weight= 1)
window.columnconfigure(1,minsize= 500, weight= 1)
def opnfile():
    filepath= askopenfilename(filetypes= [('Text files','*.txt'),('All files', '*.*')])
    if not filepath :
        return 
    text_edit.delete(1.0,END)
    with open(filepath,'r') as input_file:
        text= input_file.read()
        text_edit.insert(END,text)
        input_file.close()
def save():
    filepath= asksaveasfilename(defaultextension= 'txt', filetypes= [('Text files','*.txt'),('All files', '*.*')])
    if not filepath :
        return 
    with open(filepath,'w') as outputfile:
        text= text_edit.get(1.0,END)
        outputfile.write(text)
text_edit= Text(window, bg= "#473523", fg= "#ffbf00")
frame= Frame(window)
hopenbtn= Button(frame, text= 'open', command= opnfile)      
wsavebtn= Button(frame, text= 'save', command= save)
hopenbtn.grid(row= 0, column= 0, sticky= 'ew')
wsavebtn.grid(row= 1, column= 0, sticky= 'ew')
frame.grid(row=0,column=0,sticky='ns')
text_edit.grid(row=0,column= 1,sticky= 'nsew')
window.mainloop()
