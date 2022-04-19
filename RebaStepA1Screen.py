import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    answer = tk.StringVar()
    default_font = 'Arial'
    text_font_size = 12
    default_font_size = 18
    title_font_size = 22
    entry_width = 30
    a1 = ttk.Frame(master, width=1000, height=750)
    a1.columnconfigure(0, weight=4)
    a1.columnconfigure(1, weight=2)
    a1.rowconfigure(0, weight=2)
    a1.rowconfigure(1, weight=2)
    a1.rowconfigure(2, weight=2)
    a1.rowconfigure(3, weight=2)
    a1.rowconfigure(4, weight=2)
    ttk.Label(a1, text='Explain your adjustment selection. '
                       'Reference the SPECIFIC part of the body.',
              font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    ttk.Label(a1, text='Select the necessary adjustment.',
              font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    ttk.Entry(a1, width=entry_width, textvariable=answer).grid(row=3, column=1, sticky=tk.EW)
    ttk.Label(a1, text='A. NECK, TRUNK, AND LEG ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    a1_step_images = [sm.ImageWidget(a1, './step1a-reba-images/reba-step1a-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(a1, './step1a-reba-images/reba-step1a-2.png', 'C', 0, 1, tk.BOTTOM, tk.E),
                      sm.ImageWidget(a1, './step1a-reba-images/reba-step1a-3.png', 'A', 0, 1, tk.BOTTOM, tk.W)]
    for img_wig in a1_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    a1_step_options = [sm.ComboBoxWidget(a1, option_type,
                                         ['If neck is twisted: (+1)', 'If neck is side bending: (+1)'], 2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(a1, option_type, ['A', 'B', 'C'], 2, 1, 40, tk.W)]
    for combo in a1_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    ttk.Label(a1, text='Step 1: Locate Neck Position.',
              font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.S)
    return a1

## add margins to both ends of frame
## make tk.Entry two/three lines (height)
## change compound image text bold & size
