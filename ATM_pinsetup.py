import tkinter as tk
root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("400x500")
account_frame = tk.Frame(root, bd=4, relief="raised", bg="#e6f2ff")
account_frame.place(x=20, y=20, width=360, height=180)
tk.Label(account_frame, text="ATM PIN Setup", font=("Arial", 14, "bold"), bg="#e6f2ff").place(x=90, y=10)
tk.Label(account_frame, text="Name:", bg="#e6f2ff").place(x=20, y=50)
name_entry = tk.Entry(account_frame)
name_entry.place(x=120, y=50)
tk.Label(account_frame, text="Account No:", bg="#e6f2ff").place(x=20, y=80)
acc_entry = tk.Entry(account_frame)
acc_entry.place(x=120, y=80)
tk.Label(account_frame, text="PIN:", bg="#e6f2ff").place(x=20, y=110)
pin_entry = tk.Entry(account_frame, show="*")
pin_entry.place(x=120, y=110)
keypad_frame = tk.Frame(root, bd=4, relief="sunken")
keypad_frame.place(x=100, y=240)
def insert_number(num):
    pin_entry.insert(tk.END, str(num))
def make_cmd(x):
    return lambda: insert_number(x)
buttons = [
    ('1',0,0), ('2',0,1), ('3',0,2),
    ('4',1,0), ('5',1,1), ('6',1,2),
    ('7',2,0), ('8',2,1), ('9',2,2),
    ('0',3,1)
]
for text, row, col in buttons:
    tk.Button(
        keypad_frame,
        text=text,
        width=5,
        height=2,
        command=make_cmd(text)
    ).grid(row=row, column=col, padx=5, pady=5)
output = tk.Text(root, height=5, width=40)
output.place(x=40, y=400)
def submit():
    name = name_entry.get()
    acc = acc_entry.get()
    pin = pin_entry.get()
    output.delete("1.0", tk.END)
    output.insert(tk.END,
        f"Name: {name}\nAccount: {acc}\nPIN Set Successfully!"
    )
tk.Button(root, text="Set PIN", command=submit, bg="green", fg="white").place(x=160, y=390)
root.mainloop()