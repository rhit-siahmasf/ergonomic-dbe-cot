import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    answer = tk.StringVar()
    default_font = 'Arial'
    text_font_size = 12
    num_lines = 3
    default_font_size = 16
    title_font_size = 18
    entry_width = 30
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
    entry_box = tk.Text(b2, width=entry_width, height=num_lines)
    entry_box.grid(row=3, column=1, sticky=tk.W)
    ttk.Label(b2, text='B. ARM & WRIST ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    b2_step_images = [sm.ImageWidget(b2, './step1a-reba-images/reba-step1a-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(b2, './step1a-reba-images/reba-step1a-2.png', 'C', 0, 1, tk.BOTTOM, tk.E),
                      sm.ImageWidget(b2, './step1a-reba-images/reba-step1a-3.png', 'A', 0, 1, tk.BOTTOM, tk.W)]
    for img_wig in b2_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    b2_step_options = [sm.ComboBoxWidget(b2, option_type,
                                         ['If neck is twisted: (+1)', 'If neck is side bending: (+1)'], 2, 1, 40, tk.SW),
                       sm.ComboBoxWidget(b2, option_type, ['A', 'B', 'C'], 2, 1, 40, tk.W)]
    for combo in b2_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    sub_title = ttk.Label(b2, text='Step 8: Locate Lower Arm Position.', font=(default_font, default_font_size))
    sub_title.grid(row=0, column=0, sticky=tk.S)
    b2_manager = sm.ScreenManager(b2, sub_title, b2_step_options[1], b2_step_options[0], entry_box)
    return b2_manager

## add margins to both ends of frame
## make tk.Entry two/three lines (height)
## change compound image text bold & size
