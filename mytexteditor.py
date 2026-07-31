from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
window= Tk()
window.title('My text editor')
window.geometry('600x600')
window.rowconfigure(0,minsize= 600,weight= 1)
window.columnconfigure(1,minsize= 600, weight= 1)
def openfile():
    file_path= askopenfilename(filetypes= [('Text files','*.txt'),('All files', '*.*')])
    if not file_path :
        return 
    text_edit.delete(1.0,END)
    with open(file_path,'r') as input_file:
        text= input_file.read()
        text_edit.insert(END,text)
        input_file.close()
def save():
    file_path= asksaveasfilename(defaultextension= 'txt', filetypes= [('Text files','*.txt'),('All files', '*.*')])
    if not file_path :
        return 
    with open(file_path,'w') as output_file:
        text= text_edit.get(1.0,END)
        output_file.write(text)
text_edit= Text(window, bg= "#66082b", fg= "#ff6060")
frame= Frame(window)
openbtn= Button(frame, text= 'Open', command= openfile)      
savebtn= Button(frame, text= 'save', command= save)
openbtn.grid(row= 0, column= 0, sticky= 'ew')
savebtn.grid(row= 1, column= 0, sticky= 'ew')
frame.grid(row=0,column=0,sticky='ns')
text_edit.grid(row=0,column= 1,sticky= 'nsew')
window.mainloop()