import tkinter as tk
from tkinter import messagebox
import json

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        
              
        if task.startswith(""):
            task = task[1:]
        else:
            task = "✓ " + task 
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, task)
        save_tasks()       
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(list(tasks), file)


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        for task in tasks:
            task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

window = tk.Tk()
window.title(" Manager App")
window.geometry("400x450")
window.resizable(False, False)

title_label = tk.Label(window, text="To-Do List", font=("Arial", 18,"bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)
task_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

list_frame = tk.Frame(window)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, width=50, height=15,font=("Aril",12), selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)

task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=task_listbox.yview)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

load_tasks()

window.mainloop()
