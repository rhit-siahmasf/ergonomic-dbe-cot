import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    answer = tk.StringVar()
    default_font = 'Arial'
    text_font_size = 12
    default_font_size = 18
    entry_width = 30

    a2 = ttk.Frame(master, width=1000, height=750)
    a2.columnconfigure(0, weight=4)
    a2.columnconfigure(1, weight=2)
    a2.rowconfigure(0, weight=2)
    a2.rowconfigure(1, weight=2)
    a2.rowconfigure(2, weight=2)
    a2.rowconfigure(3, weight=2)
    a2.rowconfigure(4, weight=2)
    tk.Label(a2, text='Select the necessary adjustment.',
             font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    tk.Label(a2, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
             font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    tk.Entry(a2, textvariable=answer, width=entry_width).grid(row=3, column=1, sticky=tk.W)
    tk.Label(a2, text='A. NECK, TRUNK, AND LEG ANALYSIS',
             font=(default_font, text_font_size)).grid(row=0, column=0, sticky=tk.NW)
    a2_step_images = [sm.ImageWidget(a2, './step2a-reba-images/reba-step2a-1.png', 'C', 1, 1, tk.RIGHT, tk.W),
                      sm.ImageWidget(a2, './step2a-reba-images/reba-step2a-2.png', 'B', 0, 1, tk.RIGHT, tk.NSEW),
                      sm.ImageWidget(a2, './step2a-reba-images/reba-step2a-3.png', 'A', 0, 1, tk.RIGHT, tk.W),
                      sm.ImageWidget(a2, './step2a-reba-images/reba-step2a-4.png', 'D', 1, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(a2, './step2a-reba-images/reba-step2a-5.png', 'E', 1, 1, tk.BOTTOM, tk.E)]
    for img_wig in a2_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    tk.Label(a2, text='Step 2: Locate trunk position.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
    a2_step_options = [sm.ComboBoxWidget(a2, option_type,
                                         ['If trunk is twisted: (+1)', 'If trunk is side bending: (+1)'],
                                         2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(a2, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
    for combo in a2_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)

    return a2



