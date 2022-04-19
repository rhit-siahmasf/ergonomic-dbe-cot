import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    default_font = 'Arial'
    default_font_size = 18
    title_font_size = 22
    a456 = ttk.Frame(master)
    a456.columnconfigure(0, weight=4)
    a456.columnconfigure(1, weight=2)
    a456.rowconfigure(0, weight=2)
    a456.rowconfigure(1, weight=2)
    a456.rowconfigure(2, weight=2)
    a456.rowconfigure(3, weight=2)
    a456.rowconfigure(4, weight=2)
    tk.Label(a456, text='A. ARM & WRIST ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    tk.Label(a456, text='Step 4: Wrist twist.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W, padx=25)
    a4_step_option = sm.ComboBoxWidget(a456, option_type,
                                       ['If wrist is twisted in mid-range: (+1)',
                                        'If wrist is at or near end of range: (+2)'], 0, 0, 40, tk.SW)
    a4_step_option.button.grid(row=a4_step_option.row, column=a4_step_option.column,
                               sticky=a4_step_option.stick, padx=35)
    tk.Label(a456, text='Step 5: Score from table A',
             font=(default_font, default_font_size)).grid(row=1, column=0, sticky=tk.W, padx=25)
    a6_step_options = sm.ComboBoxWidget(a456, option_type,
                                        ['Action repeated occurs 4x/minute?'
                                         ' OR is posture mainly static (i.e held >10 minutes)? (+1)'],
                                        2, 0, 90, tk.S)
    a6_step_options.button.grid(row=a6_step_options.row, column=a6_step_options.column, sticky=a6_step_options.stick)
    tk.Label(a456, text='Step 6: Muscle Use',
             font=(default_font, default_font_size)).grid(row=2, column=0, sticky=tk.W, padx=25)
    return a456
