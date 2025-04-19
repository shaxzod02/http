import tkinter as tk

def calculate():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())

        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")
        return


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x600")

title_label = tk.Label(window, text="Simple Calculator", font=("Arial", 24))
title_label.pack(pady=20)

frame1 = tk.Frame(window)
frame1.pack(pady=10)

num1_label = tk.Label(frame1, text=" First Number:")
num1_label.pack(side=tk.LEFT)

first_number = tk.Entry(frame1, width=10)
first_number.pack()

frame2 = tk.Frame(window)
frame2.pack(pady=10)

num2_label = tk.Label(frame2, text=" Second Number:")
num2_label.pack(side=tk.LEFT)

second_number = tk.Entry(frame2, width=10)
second_number.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=20)

result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=20)

def clear_fields():
    first_number.delete(0, tk.END)
    second_number.delete(0, tk.END)
    result_label.config(text="Result: ")

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=20)

window.mainloop()