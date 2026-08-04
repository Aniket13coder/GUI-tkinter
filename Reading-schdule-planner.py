import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Reading Planner")
root.geometry("300x200")
def open_planner():
    top = tk.Toplevel(root)
    top.title("Reading Schedule")
    top.geometry("350x250")
    tk.Label(top, text="Total Pages:").pack(pady=5)
    total_entry = tk.Entry(top)
    total_entry.pack(pady=5)
    tk.Label(top, text="Pages per Day:").pack(pady=5)
    daily_entry = tk.Entry(top)
    daily_entry.pack(pady=5)
    result_label = tk.Label(top, text="", fg="blue")
    result_label.pack(pady=10)
    def calculate():
        try:
            total = int(total_entry.get())
            daily = int(daily_entry.get())
            if daily <= 0:
                raise ValueError
            days = total // daily
            remaining = total % daily
            result_label.config(
                text=f"Days needed: {days}\nRemaining pages: {remaining}"
            )
        except ValueError:
            messagebox.showerror("Error", "Please enter valid positive numbers!")
    tk.Button(top, text="Calculate", command=calculate).pack(pady=10)
tk.Button(root, text="Open Planner", command=open_planner).pack(pady=50)
root.mainloop()