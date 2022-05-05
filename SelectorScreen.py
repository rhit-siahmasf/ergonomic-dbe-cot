import tkinter as tk
from tkinter import ttk


def create_page(master):
    default_font_size = 18
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
    return im_selector




