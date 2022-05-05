import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


def create_page(master):
    default_font_size = 18
    global im_selector
    im_selector = ttk.Frame(master, width=1000, height=750)
    im_selector.columnconfigure(0, weight=4)
    im_selector.columnconfigure(1, weight=2)
    im_selector.rowconfigure(0, weight=2)
    im_selector.rowconfigure(1, weight=2)
    im_selector.rowconfigure(2, weight=2)
    im_selector.rowconfigure(3, weight=2)
    im_selector.rowconfigure(4, weight=2)

    tk.Label(im_selector, text='Please upload an image to begin assessment.',
             font=('Arial', default_font_size)).grid(row=0, column=0, sticky=tk.E)
    tk.Button(im_selector, text='Upload', bg='#000fff000',
              command=upload_image).grid(row=1, column=0, sticky=tk.N, padx=15, ipadx=15)
    return im_selector


def upload_image():
    global easel
    filename = filedialog.askopenfilename()
    #    print('FileName:' + filename)
    img = Image.open(filename)
    img = img.resize((175, 175), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    easel = tk.Label(im_selector, image=img)
    easel.image = img
    easel.grid(row=2, column=0, sticky=tk.W, padx=85)

