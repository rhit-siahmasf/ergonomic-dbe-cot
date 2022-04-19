import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    default_font = 'Arial'
    default_font_size = 18
    title_font_size = 22
    b345 = ttk.Frame(master)
    b345.columnconfigure(0, weight=4)
    b345.columnconfigure(1, weight=2)
    b345.rowconfigure(0, weight=2)
    b345.rowconfigure(1, weight=2)
    b345.rowconfigure(2, weight=2)
    b345.rowconfigure(3, weight=2)
    b345.rowconfigure(4, weight=2)
    tk.Label(b345, text='B. NECK, TRUNK, AND LEG ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    tk.Label(b345, text='Step 11: Legs.',
             font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W, padx=25)
    b3_step_option = sm.ComboBoxWidget(b345, option_type,
                                       ['If legs and feet are supported: (+1)',
                                        'If NOT supported: (+2)'], 0, 0, 40, tk.SW)
    b3_step_option.button.grid(row=b3_step_option.row, column=b3_step_option.column,
                               sticky=b3_step_option.stick, padx=35)
    tk.Label(b345, text='Step 12: Posture Score from Table.',
             font=(default_font, default_font_size)).grid(row=1, column=0, sticky=tk.W, padx=25)
    b5_step_options = sm.ComboBoxWidget(b345, option_type,
                                        ['Action repeated occurs 4x/minute?'
                                         ' OR is posture mainly static (i.e held >10 minutes)? (+1)'],
                                        2, 0, 90, tk.S)
    b5_step_options.button.grid(row=b5_step_options.row, column=b5_step_options.column, sticky=b5_step_options.stick)
    tk.Label(b345, text='Step 13: Add Muscle Score.',
             font=(default_font, default_font_size)).grid(row=2, column=0, sticky=tk.W, padx=25)
    return b345
