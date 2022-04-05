import tkinter as tk
from tkinter import ttk
from fpdf import FPDF
import ScreenManager as sm


def create_page(master):
    final = ttk.Frame(master, width=1000, height=750)
    final.columnconfigure(0, weight=2)
    final.columnconfigure(1, weight=2)
    final.columnconfigure(2, weight=2)
    final.rowconfigure(0, weight=2)
    final.rowconfigure(1, weight=2)
    final.rowconfigure(2, weight=2)
    tk.Button(final, text='Save as PDF', bg='#8B2323',
              command=None).grid(row=0, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(final, text='Restart', bg='#8B2323', command=None).grid(row=0, column=0, sticky=tk.E, padx=15, ipadx=15)

