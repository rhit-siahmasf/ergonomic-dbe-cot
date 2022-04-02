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
    a7 = ttk.Frame(master)
    a7.columnconfigure(0, weight=4)
    a7.columnconfigure(1, weight=2)
    a7.rowconfigure(0, weight=2)
    a7.rowconfigure(1, weight=2)
    a7.rowconfigure(2, weight=2)
    a7.rowconfigure(3, weight=2)
    a7.rowconfigure(4, weight=2)
    tk.Label(a7, text='Select the necessary adjustment.',
             font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
    tk.Label(a7, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
             font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
    tk.Entry(a7, width=entry_width, textvariable=answer).grid(row=3, column=1, sticky=tk.EW)
    tk.Label(a7, text='A. ARM & WRIST ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    tk.Label(a7, text='Step 7: Add Force / Load.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
    a7_step_options = sm.ComboBoxWidget(a7, option_type,
                                        ['If load < 4.4 lbs (intermittent): (+0)',
                                         'If load 4.4 to 22 lbs (intermittent): (+1)',
                                         'If load 4.4 to 22 lbs (static or repeated): (+2)',
                                         'If more than 22lbs OR repeated or shocks: (+3)'], 2, 1, 40, tk.SW)
    a7_step_options.button.grid(row=a7_step_options.row, column=a7_step_options.column, sticky=a7_step_options.stick)
    return a7
