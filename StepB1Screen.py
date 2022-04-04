import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    default_font = 'Arial'
    text_font_size = 12
    default_font_size = 18
    title_font_size = 22
    b1 = ttk.Frame(master, width=1000, height=750)
    b1.columnconfigure(0, weight=4)
    b1.columnconfigure(1, weight=2)
    b1.rowconfigure(0, weight=2)
    b1.rowconfigure(1, weight=2)
    b1.rowconfigure(2, weight=2)
    b1.rowconfigure(3, weight=2)
    b1.rowconfigure(4, weight=2)
    ttk.Label(b1, text='Explain your adjustment selection. '
                       'Reference the SPECIFIC part of the body.',
              font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    ttk.Label(b1, text='Select the necessary adjustment.',
              font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    b1_step_images = [sm.ImageWidget(b1, './step9b-rula-images/rula-step9b-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(b1, './step9b-rula-images/rula-step9b-2.png', 'C', 0, 1, tk.BOTTOM, tk.E),
                      sm.ImageWidget(b1, './step9b-rula-images/rula-step9b-3.png', 'A', 0, 1, tk.BOTTOM, tk.W),
                      sm.ImageWidget(b1, './step9b-rula-images/rula-step9b-4.png', 'D', 1, 1, tk.BOTTOM, tk.NSEW)]
    b1_step_options = [sm.ComboBoxWidget(b1, option_type,
                                         ['Adjust if neck is twisted: (+1)',
                                          'Adjust if neck is side bending: (+1)'], 2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(b1, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
    for combo in b1_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    for img_wig in b1_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    ttk.Label(b1, text='Step 9: Locate Neck Position.',
              font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.S)
    ttk.Label(b1, text='B. NECK, TRUNK, AND LEG ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    return b1
