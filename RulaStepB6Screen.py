import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    answer = tk.StringVar()
    default_font = 'Arial'
    default_font_size = 18
    title_font_size = 22
    entry_width = 30
    b6 = ttk.Frame(master)
    b6.columnconfigure(0, weight=4)
    b6.columnconfigure(1, weight=2)
    b6.rowconfigure(0, weight=2)
    b6.rowconfigure(1, weight=2)
    b6.rowconfigure(2, weight=2)
    b6.rowconfigure(3, weight=2)
    b6.rowconfigure(4, weight=2)
    entry_box = tk.Entry(b6, width=entry_width, textvariable=answer)
    entry_box.grid(row=3, column=1, sticky=tk.EW)
    tk.Label(b6, text='B. NECK, TRUNK, AND LEG ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    sub_title = tk.Label(b6, text='Step 14: Add Force / Load Score', font=(default_font, default_font_size))
    sub_title.grid(row=0, column=0, sticky=tk.W)
    b6_step_options = sm.ComboBoxWidget(b6, option_type,
                                        ['If load < 4.4 lbs (intermittent): (+0)',
                                         'If load 4.4 to 22 lbs (intermittent): (+1)',
                                         'If load 4.4 to 22 lbs (static or repeated): (+2)',
                                         'If more than 22lbs OR repeated or shocks: (+3)'], 2, 1, 40, tk.SW)
    b6_step_options.button.grid(row=b6_step_options.row, column=b6_step_options.column, sticky=b6_step_options.stick)
    b6_manager = sm.ScreenManager(b6, sub_title, b6_step_options, None, entry_box)
    return b6_manager
