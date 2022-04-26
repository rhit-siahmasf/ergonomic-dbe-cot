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
    a3 = ttk.Frame(master, width=1000, height=750)
    a3.columnconfigure(0, weight=4)
    a3.columnconfigure(1, weight=2)
    a3.rowconfigure(0, weight=2)
    a3.rowconfigure(1, weight=2)
    a3.rowconfigure(2, weight=2)
    a3.rowconfigure(3, weight=2)
    a3.rowconfigure(4, weight=2)
    ttk.Label(a3, text='Explain your adjustment selection. '
                       'Reference the SPECIFIC part of the body.',
              font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    ttk.Label(a3, text='Select the necessary adjustment.',
              font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    entry_box = tk.Text(a3, width=entry_width, height=num_lines)
    entry_box.grid(row=3, column=1, sticky=tk.W)
    ttk.Label(a3, text='A. NECK, TRUNK, AND LEG ANALYSIS',
              font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    a1_step_images = [sm.ImageWidget(a3, './step3a-reba-images/reba-step3a-1.png', 'B', 0, 1, tk.BOTTOM, tk.NSEW),
                      sm.ImageWidget(a3, './step3a-reba-images/reba-step3a-2.png', 'C', 0, 1, tk.BOTTOM, tk.E),
                      sm.ImageWidget(a3, './step3a-reba-images/reba-step3a-3.png', 'A', 0, 1, tk.BOTTOM, tk.W),
                      sm.ImageWidget(a3, './step3a-reba-images/reba-step3a-4.png', 'D', 1, 1, tk.BOTTOM, tk.NSEW)]
    for img_wig in a1_step_images:
        img_wig.create_image()
        img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
    a1_step_options = [sm.ComboBoxWidget(a3, option_type, ['A', 'B', 'C', 'D'], 2, 1, 40, tk.W)]
    for combo in a1_step_options:
        combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
    sub_title = ttk.Label(a3, text='Step 3: Legs', font=(default_font, default_font_size))
    sub_title.grid(row=0, column=0, sticky=tk.S)
    a3_manager = sm.ScreenManager(a3, sub_title, a1_step_images, a1_step_options[0], None, entry_box)
    return a3_manager

## add margins to both ends of frame
## make tk.Entry two/three lines (height)
## change compound image text bold & size
