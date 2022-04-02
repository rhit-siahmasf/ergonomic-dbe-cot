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
    a3 = ttk.Frame(master)
    a3.columnconfigure(0, weight=4)
    a3.columnconfigure(1, weight=2)
    a3.rowconfigure(0, weight=2)
    a3.rowconfigure(1, weight=2)
    a3.rowconfigure(2, weight=2)
    a3.rowconfigure(3, weight=2)
    a3.rowconfigure(4, weight=2)
    tk.Label(a3, text='Select the necessary adjustment.',
             font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    tk.Label(a3, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
             font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    tk.Entry(a3, textvariable=answer, width=entry_width).grid(row=3, column=1, sticky=tk.EW)
    tk.Label(a3, text='A. ARM & WRIST ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    a3_step_images = [sm.ImageWidget(a3, './step3a-rula-images/rula-step3a-2.png', 'B', 0, 1, tk.RIGHT, tk.NSEW),
                      sm.ImageWidget(a3, './step3a-rula-images/rula-step3a-3.png', 'C', 0, 1, tk.RIGHT, tk.E),
                      sm.ImageWidget(a3, './step3a-rula-images/rula-step3a-1.png', 'A', 0, 1, tk.RIGHT, tk.W)]
    for img_wig in a3_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    a3_step_options = [sm.ComboBoxWidget(a3, option_type, ['Adjust if wrist is bent from midline: (+1)'],
                                         2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(a3, option_type, ['A', 'B', 'C'], 2, 1, 40, tk.W)]
    for combo in a3_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    tk.Label(a3, text='Step 3: Locate wrist position.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)

    return a3
