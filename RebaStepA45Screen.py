import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    option_type = tk.StringVar()
    default_font = 'Arial'
    default_font_size = 18
    title_font_size = 22
    a45 = ttk.Frame(master)
    a45.columnconfigure(0, weight=4)
    a45.columnconfigure(1, weight=2)
    a45.rowconfigure(0, weight=2)
    a45.rowconfigure(1, weight=2)
    a45.rowconfigure(2, weight=2)
    a45.rowconfigure(3, weight=2)
    a45.rowconfigure(4, weight=2)
    tk.Label(a45, text='A. NECK, TRUNK, AND LEG ANALYSIS',
             font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
    tk.Label(a45, text='Step 4: Posture Score in Table A.', font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W, padx=25)
    a5_step_option = sm.ComboBoxWidget(a45, option_type,
                                       ['If load < 11lbs: (+0)', 'If load 11 to 22lbs: (+1)',
                                        'If load > 22lbs: (+2)', 'If shock or rapid build up of force: (+1)'],
                                       0, 0, 40, tk.SW)
    sub_title = tk.Label(a45, text='Step 5: Add Force/Load Score', font=(default_font, default_font_size))
    sub_title.grid(row=1, column=0, sticky=tk.W, padx=25)
    a5_step_option.button.grid(row=a5_step_option.row, column=a5_step_option.column, sticky=a5_step_option.stick)
    a45_manager = sm.ScreenManager(a45, sub_title, a5_step_option, None, None)
    return a45_manager
