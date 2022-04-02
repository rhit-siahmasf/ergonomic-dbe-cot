import tkinter as tk
from tkinter import ttk
import ScreenManager as sm

option_type = tk.StringVar()
answer = tk.StringVar()
default_font = 'Arial'
text_font_size = 12
default_font_size = 18
title_font_size = 22
entry_width = 30
my_image = None


def create_objects(master):
    a2 = ttk.Frame(master)
    tk.Label(a2, text='Select the necessary adjustment.',
             font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    tk.Label(a2, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
             font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    tk.Entry(a2, textvariable=answer, width=entry_width).grid(row=3, column=1, sticky=tk.W)
    tk.Label(a2, text='A. ARM & WRIST ANALYSIS',
             font=(default_font, text_font_size)).grid(row=0, column=0, sticky=tk.NW)
    a2_step_images = [sm.ImageWidget(a2, './step2a-rula-images/rula-step2a-3.png', '', 1, 1, tk.RIGHT, tk.W),
                      sm.ImageWidget(a2, './step2a-rula-images/rula-step2a-1.png', 'B', 0, 1, tk.RIGHT, tk.NSEW),
                      sm.ImageWidget(a2, './step2a-rula-images/rula-step2a-2.png', 'A', 0, 1, tk.RIGHT, tk.W)]
    for img_wig in a2_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    tk.Label(a2, text='Step 2: Locate lower arm position.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
    a2_step_options = [sm.ComboBoxWidget(a2, option_type,
                                         ['Adjust if arm is working across midline or outside of body: (+1)'],
                                         2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(a2, option_type, ['A', 'B', 'C'], 2, 1, 40, tk.W)]
    for combo in a2_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
#    tk.Button(master, text='NEXT', bg='#458B00', command=next_page).grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
#    tk.Button(master, text='BACK', bg='#8B2323', command=prev_page).grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

