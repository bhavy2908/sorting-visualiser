from tkinter import *
from tkinter import ttk
from bubble_sort import *
from quick_sort import *
from insertion_sort import *
from selection_sort import *
from merge_sort import *
from counting_sort import *
from radix_sort import *
import random


# Functions

# This function displays the array
def draw_data(current_data, digit=-1, optional_color='cyan', end=-1, digit2=999, var1=-999, var2=-999):
    canvas.delete('all')
    color = DEFAULT_COLOR
    count = 0
    C_HEIGHT = 700
    C_WIDTH = 1500
    x_width = C_WIDTH / (len(current_data))
    offset = 10
    spacing = 5
    normalized_data = [i / max(current_data) for i in current_data]
    for i, height in enumerate(normalized_data):
        # upper left
        x0 = i * x_width + offset + spacing
        y0 = C_HEIGHT - height * 680
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = C_HEIGHT
        if count == 2:
            color = DEFAULT_COLOR
        if digit != -1 and count < 2:
            if i == digit or i == digit + 1:
                color = optional_color
                count += 1
        if algMenu.get() == 'Bubble Sort':
            if (i > end) and (end != -1):
                color = '#FF6A00'
        if algMenu.get() == 'Selection Sort':
            if i <= end:
                color = '#FF6A00'
            elif i > end and (i == digit or i == digit2):
                color = optional_color
            else:
                color = DEFAULT_COLOR
        if algMenu.get() == 'Insertion Sort':
            if i == digit or i == digit2:
                color = optional_color
            elif i <= end:
                color = '#FF6A00'
            else:
                color = DEFAULT_COLOR
        if algMenu.get() == "Quick Sort":
            if i == digit or i == digit2:
                color = optional_color
            elif var1 <= i <= var2:
                color = '#FF6A00'
            else:
                color = DEFAULT_COLOR

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update_idletasks()


# This function is called when SORT button is pressed
def start():
    print('Sorting...')
    global data
    if not data:
        return

    # These if else statements call the function of the selected algorithm
    if algMenu.get() == 'Quick Sort':
        quick_sort(data, draw_data, speedScale.get())
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, speedScale.get())
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, draw_data, speedScale.get())
    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, draw_data, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, draw_data, speedScale.get())
    elif algMenu.get() == 'Counting Sort':
        count_sort(data, draw_data, speedScale.get())
    elif algMenu.get() == 'Radix Sort':
        radix_sort(data, draw_data, speedScale.get())


# This function is called when NEW ARRAY button is pressed
def generate():
    global data
    print('Algo: ' + selected_alg.get())
    try:
        min_val = int(minEntry.get())
    except EXCEPTION:
        min_val = 10
    try:
        max_val = int(maxEntry.get())
    except EXCEPTION:
        max_val = 10
    try:
        size = int(sizeEntry.get())
    except EXCEPTION:
        size = 10
    data = []
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    if max_val == 0:
        max_val = 100
    if (algMenu.get() == 'Counting Sort') and (max_val > size):
        max_val = size - 1
    if (algMenu.get() == 'Counting Sort') and (min_val > size):
        min_val = 0
    data = []
    for _ in range(size):
        data.append(random.randrange(min_val, max_val + 1))
    draw_data(data)


# Global declarations
DEFAULT_COLOR = '#00FDFD'
root = Tk()
root.title('Sorting Visualiser')
root.maxsize(1920, 1080)
root.config(bg='white')

# Variables
selected_alg = StringVar()
data = []

# User Interface

# Body
UI_frame = Frame(root, width=1500, height=200, bg='white')
UI_frame.grid(row=0, column=0)
canvas = Canvas(root, width=1500, height=700, bg='black')
canvas.grid(row=1, column=0)

# Elements

# Dropdown box for algorithms
Label(UI_frame, text='Algorithm:', bg='white').grid(row=0, column=0, padx=0, pady=0)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg,
                       values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort',
                               'Counting Sort', 'Radix Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

# Delay slider
speedScale = Scale(UI_frame, from_=0.01, to=2.0, length=200, digits=2, resolution=0.02, orient=HORIZONTAL,
                   label='Delay', activebackground='#00FDFD', troughcolor='black')
speedScale.grid(row=0, column=5, padx=5, pady=5)

# Sort Button
sort_btn = PhotoImage(file=r"image assets/sort.png")
Button(UI_frame, command=start, image=sort_btn).grid(row=0, column=7, padx=5, pady=5, sticky=E)

# Size of array slider
sizeEntry = Scale(UI_frame, from_=3, to=100, length=200, resolution=1, orient=HORIZONTAL,
                  label='Size', activebackground='#00FDFD', troughcolor='black')
sizeEntry.grid(row=0, column=2, padx=5, pady=5)

# Minimum Value slider
minEntry = Scale(UI_frame, from_=0, to=1000, length=200, resolution=1, orient=HORIZONTAL,
                 label='Min Value', activebackground='#00FDFD', troughcolor='black')
minEntry.grid(row=0, column=3, padx=5, pady=5)

# Maximum Value slider
maxEntry = Scale(UI_frame, from_=0, to=1000, length=200, resolution=1, orient=HORIZONTAL,
                 label='Max Value', activebackground='#00FDFD', troughcolor='black')
maxEntry.grid(row=0, column=4, padx=5, pady=5)

# New Array Button
na_btn = PhotoImage(file=r"image assets/newarray.png")
Button(UI_frame, command=generate, image=na_btn).grid(row=0, column=6, padx=5, pady=5)

# Exit Button
exit_btn = PhotoImage(file=r"image assets/exit.png")
Button(UI_frame, command=root.destroy, image=exit_btn).grid(row=0, column=8, padx=5, pady=5)

root.mainloop()
