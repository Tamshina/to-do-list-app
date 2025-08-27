import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("🌸 Pastel To-Do List 🌸")
root.geometry("450x550")
root.config(bg="#fdf6f0")  # creamy pastel background

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, f"✦ {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Write something lovely first ✨")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Oops!", "Select a task to remove 🌷")

# Title Label
title = tk.Label(root, text="My Aesthetic To-Do List", 
                 font=("Segoe Script", 20, "bold"), 
                 bg="#fdf6f0", fg="#d988bc")
title.pack(pady=15)

# Entry box
task_entry = tk.Entry(root, font=("Century Gothic", 14), 
                      bg="#fceef5", fg="#555", 
                      relief="flat", justify="center")
task_entry.pack(pady=10, ipadx=10, ipady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#fdf6f0")
button_frame.pack(pady=10)

# Add Button
add_button = tk.Button(button_frame, text="➕ Add Task", command=add_task,
                       bg="#ffd6e0", fg="#5c4b51", 
                       font=("Century Gothic", 12, "bold"),
                       relief="flat", width=12, height=1)
add_button.grid(row=0, column=0, padx=5)

# Delete Button
delete_button = tk.Button(button_frame, text="❌ Delete Task", command=delete_task,
                          bg="#cdb4db", fg="white", 
                          font=("Century Gothic", 12, "bold"),
                          relief="flat", width=12, height=1)
delete_button.grid(row=0, column=1, padx=5)

# Task Listbox
listbox = tk.Listbox(root, width=40, height=15, 
                     bg="#faf0f4", fg="#4a4a4a",
                     font=("Century Gothic", 12), 
                     selectbackground="#ffc8dd", 
                     relief="flat")
listbox.pack(pady=20)

# Cute footer
footer = tk.Label(root, text="✨ Stay organized, bestie ✨", 
                  font=("Segoe Script", 12), 
                  bg="#fdf6f0", fg="#a68dad")
footer.pack(pady=10)

root.mainloop()
