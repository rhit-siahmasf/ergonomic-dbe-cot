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

    b1 = ttk.Frame(master, width=1000, height=750)
    b1.columnconfigure(0, weight=4)
    b1.columnconfigure(1, weight=2)
    b1.rowconfigure(0, weight=2)
    b1.rowconfigure(1, weight=2)
    b1.rowconfigure(2, weight=2)
    b1.rowconfigure(3, weight=2)
    b1.rowconfigure(4, weight=2)
    tk.Label(b1, text='Select the necessary adjustment.',
             font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    tk.Label(b1, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
             font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    entry_box = tk.Entry(b1, textvariable=answer, width=entry_width)
    entry_box.grid(row=3, column=1, sticky=tk.W)
    tk.Label(b1, text='B. ARM & WRIST ANALYSIS',
             font=(default_font, text_font_size)).grid(row=0, column=0, sticky=tk.NW)
    b1_step_images = [sm.ImageWidget(b1, './step7b-reba-images/reba-step7b-1.png', 'C', 1, 1, tk.RIGHT, tk.W),
                      sm.ImageWidget(b1, './step7b-reba-images/reba-step7b-2.png', 'B', 0, 1, tk.RIGHT, tk.NSEW),
                      sm.ImageWidget(b1, './step7b-reba-images/reba-step7b-3.png', 'A', 0, 1, tk.RIGHT, tk.W),
                      sm.ImageWidget(b1, './step7b-reba-images/reba-step7b-4.png', 'D', 1, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(b1, './step7b-reba-images/reba-step7b-5.png', 'E', 1, 1, tk.BOTTOM, tk.E)]
    for img_wig in b1_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    sub_title = tk.Label(b1, text='Step 1: Locate Upper Arm Position.', font=(default_font, default_font_size))
    sub_title.grid(row=0, column=0, sticky=tk.W)
    b1_step_options = [sm.ComboBoxWidget(b1, option_type,
                                         ['If shoulder raised: (+1)', 'If upper arm is abducted: (+1)',
                                          'If arm is supported or person is leaning: (-1)'],
                                         2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(b1, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
    for combo in b1_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    b1_manager = sm.ScreenManager(b1, sub_title, b1_step_options[1], b1_step_options[0], entry_box)
    return b1_manager



