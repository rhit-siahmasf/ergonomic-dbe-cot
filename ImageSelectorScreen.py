import tkinter as tk
import ScreenManager as sm
from tkinter import filedialog

master = tk.Tk()
master.geometry('1000x750')
master.columnconfigure(0, weight=4)
master.columnconfigure(1, weight=2)
master.rowconfigure(0, weight=2)
master.rowconfigure(1, weight=2)
master.rowconfigure(2, weight=2)
master.rowconfigure(3, weight=2)
master.rowconfigure(4, weight=2)
option_type = tk.StringVar()
answer = tk.StringVar()
default_font = 'Arial'
text_font_size = 12
default_font_size = 18
title_font_size = 22
entry_width = 30
my_image = None


def next_page():
    master.destroy()
    import StepA1Screen


def prev_page():
    master.destroy()
    # import StepA1Screen


def upload_image():
    global my_image
    name = filedialog.askopenfilename()
    my_image = sm.ImageWidget(master, name, '', 1, 0, 0, tk.NSEW)

## move buttons to center

tk.Button(master, text='BACK', bg='#8B2323',
          command=prev_page).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Label(master, text='Please upload an image to begin assessment.',
         font=('Arial', default_font_size)).grid(row=0, column=0, sticky=tk.E)
tk.Button(master, text='Upload', bg='#000fff000',
          command=upload_image).grid(row=1, column=0, sticky=tk.N, padx=15, ipadx=15)
tk.Button(master, text='NEXT', bg='#458B00',
          command=next_page).grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

master.title('RULA / REBA Assessment')
master.mainloop()