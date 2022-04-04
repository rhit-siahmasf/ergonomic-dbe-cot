import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    default_font = 'Arial'
    text_font_size = 12
    default_font_size = 18
    title_font_size = 22
    b2 = ttk.Frame(master, width=1000, height=750)
    b2.columnconfigure(0, weight=4)
    b2.columnconfigure(1, weight=2)
    b2.rowconfigure(0, weight=2)
    b2.rowconfigure(1, weight=2)
    b2.rowconfigure(2, weight=2)
    b2.rowconfigure(3, weight=2)
    b2.rowconfigure(4, weight=2)
    ttk.Label(b2, text='Explain your adjustment selection. '
                       'Reference the SPECIFIC part of the body.',
              font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    ttk.Label(b2, text='Select the necessary adjustment.',
              font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    b2_step_images = [sm.ImageWidget(b2, './step10b-rula-images/rula-step10b-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(b2, './step10b-rula-images/rula-step10b-2.png', 'C', 0, 1, tk.BOTTOM, tk.E),
                      sm.ImageWidget(b2, './step10b-rula-images/rula-step10b-3.png', 'A', 0, 1, tk.BOTTOM, tk.W),
                      sm.ImageWidget(b2, './step10b-rula-images/rula-step10b-4.png', 'D', 1, 1, tk.BOTTOM, tk.NSEW)]
    b2_step_options = [sm.ComboBoxWidget(b2, option_type,
                                         ['Adjust if trunk is twisted: (+1)',
                                          'Adjust if trunk is side bending: (+1)'], 2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(b2, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
    for combo in b2_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    for img_wig in b2_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    ttk.Label(b2, text='Step 10: Locate Trunk Position.',
              font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.S)
    ttk.Label(b2, text='B. NECK, TRUNK, AND LEG ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    return b2
