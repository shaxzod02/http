import tkinter as tk
from tkinter import colorchooser

currext_x, current_y = 0, 0
color = "black"
pen_size = 5

def start_position(event):
    global currext_x, current_y
    currext_x, current_y = event.x, event.y

def draw_line(event):
    global currext_x, current_y
    canvas.create_line(currext_x, current_y, event.x, event.y, fill=color, width=pen_size, capstyle=tk.ROUND, smooth=True)
    currext_x, current_y = event.x, event.y

def change_color():
    global color
    new_color = colorchooser.askcolor(color)[1]
    if new_color:
        color = new_color
        color_button.config(bg=color)


def clear_canvas():
    canvas.delete("all")
    

def change_pen_size(new_size):
    global pen_size
    pen_size = new_size

def set_small_pen():
    change_pen_size(2)

def set_medium_pen():
    change_pen_size(5)

def set_large_pen():
    change_pen_size(10)

window = tk.Tk()
window.title("Drawing App")
window.geometry("800x600")

title_label = tk.Label(window, text="Drawing App", font=("Arial", 24))
title_label.pack(pady=10)

toolbar = tk.Frame(window)
toolbar.pack(fill=tk.X,padx=5)

color_button = tk.Button(toolbar, text="Color", command=change_color)
color_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(toolbar, text="Clear", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5)

size_frame = tk.Frame(toolbar)
size_frame.pack(side=tk.LEFT, padx=5)

size_label = tk.Label(size_frame, text="Pen Size:")
size_label.pack(side=tk.LEFT)

small_button = tk.Button(size_frame, text="Small", command=set_small_pen)
small_button.pack(side=tk.LEFT, padx=5)

medium_button = tk.Button(size_frame, text="Medium", command=set_medium_pen)
medium_button.pack(side=tk.LEFT, padx=5)

large_button = tk.Button(size_frame, text="Large", command=set_large_pen)
large_button.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

canvas.bind("<Button-1>", start_position)
canvas.bind("<B1-Motion>", draw_line)

instruction_label = tk.Label(window, text="Click and drag to draw. font=('Arial', 12)")
instruction_label.pack(pady=10)

window.mainloop()