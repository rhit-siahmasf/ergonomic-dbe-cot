import tkinter as tk
from tkinter import ttk
import ScreenManager as sm


def create_page(master):
    assess = ttk.Frame(master, width=1000, height=750)
    assess.columnconfigure(0, weight=4)
    assess.columnconfigure(1, weight=2)
    assess.rowconfigure(0, weight=2)
    assess.rowconfigure(1, weight=2)
    assess.rowconfigure(2, weight=2)
    assess.rowconfigure(3, weight=2)
    assess.rowconfigure(4, weight=2)
    option_type = tk.StringVar()
    default_font_size = 18
    assessment_option = sm.ComboBoxWidget(assess, option_type, ['RULA', 'REBA', 'Open Existing...'], 1, 0, 40, tk.N)
    assessment_option.button.grid(row=assessment_option.row,
                                  column=assessment_option.column, sticky=assessment_option.stick)
    tk.Label(assess, text='Select an option to continue.',
             font=('Arial', default_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
    return assess


