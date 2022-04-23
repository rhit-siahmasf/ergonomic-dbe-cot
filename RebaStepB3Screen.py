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
    b3 = ttk.Frame(master, width=1000, height=750)
    b3.columnconfigure(0, weight=4)
    b3.columnconfigure(1, weight=2)
    b3.rowconfigure(0, weight=2)
    b3.rowconfigure(1, weight=2)
    b3.rowconfigure(2, weight=2)
    b3.rowconfigure(3, weight=2)
    b3.rowconfigure(4, weight=2)
    ttk.Label(b3, text='Explain your adjustment selection. '
                       'Reference the SPECIFIC part of the body.',
              font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    ttk.Label(b3, text='Select the necessary adjustment.',
              font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    entry_box = ttk.Entry(b3, width=entry_width, textvariable=answer)
    entry_box.grid(row=3, column=1, sticky=tk.EW)
    ttk.Label(b3, text='B. ARM & WRIST ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    b3_step_images = [sm.ImageWidget(b3, './step8b-reba-images/reba-step8b-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(b3, './step8b-reba-images/reba-step8b-2.png', 'A', 0, 1, tk.BOTTOM, tk.W)]
    for img_wig in b3_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    b3_step_options = [sm.ComboBoxWidget(b3, option_type,
                                         ['If wrist is bent from midline or twisted (+1)'], 2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(b3, option_type, ['A', 'B', 'C'], 2, 1, 40, tk.W)]
    for combo in b3_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    sub_title = ttk.Label(b3, text='Step 8: Locate Lower Arm Position.', font=(default_font, default_font_size))
    sub_title.grid(row=0, column=0, sticky=tk.S)
    b3_manager = sm.ScreenManager(b3, sub_title, b3_step_options[1], b3_step_options[0], entry_box)
    return b3_manager
