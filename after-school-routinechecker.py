import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("400x400")
routine = ["Snack", "Homework", "Play", "Dinner", "Sleep"]
current_index = 0
tk.Label(root, text="Enter your task:", font=("Arial", 12)).pack(pady=10)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)
last_char_label = tk.Label(root, text="Last typed: ")
last_char_label.pack(pady=5)
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)
def show_last_char(event):
    text = task_entry.get()
    if text:
        last_char_label.config(text=f"Last typed: {text[-1]}")
    else:
        last_char_label.config(text="Last typed: ")
task_entry.bind("<KeyRelease>", show_last_char)
def on_click(event):
    result_label.config(text="Routine area clicked!")
routine_frame = tk.Frame(root, bd=2, relief="sunken", width=300, height=80)
routine_frame.pack(pady=10)
routine_frame.bind("<Button-1>", on_click)
def check_task():
    global current_index
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    next_task = routine[current_index]
    result_label.config(text=f"Next task: {next_task}")
    current_index = (current_index + 1) % len(routine)
tk.Button(root, text="Check Routine", command=check_task).pack(pady=10)
root.mainloop()