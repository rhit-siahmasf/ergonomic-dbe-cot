import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup as BS
import json


def create_page(master):
    global final
    final = ttk.Frame(master, width=1000, height=750)
    final.columnconfigure(0, weight=2)
    final.columnconfigure(1, weight=2)
    final.columnconfigure(2, weight=2)
    final.rowconfigure(0, weight=2)
    final.rowconfigure(1, weight=2)
    final.rowconfigure(2, weight=2)
    tk.Button(final, text='Save as PDF', bg='#A7B0AF',
              command=None).grid(row=1, column=0, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(final, text='Restart', bg='#8B2323', command=None).grid(row=2, column=0, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(final, text='EXIT', bg='#8B2323',
              command=popup_check).grid(row=2, column=2, sticky=tk.E, padx=15, ipadx=15)
    return final


def popup_check():
    pop = tk.Toplevel()
    pop.wm_title("Exit: Warning.")
    msg = tk.Label(pop, text='Are you sure you want to exit? No progress will manually be saved for this assessment.')
    msg.grid(row=0, column=0, sticky=tk.E, columnspan=2)
    yes_btn = tk.Button(pop, text='YES', bg='light green', command=lambda: [pop.destroy(), final.destroy()])
    yes_btn.grid(row=1, column=0, sticky=tk.E, padx=15)
    no_btn = tk.Button(pop, text='NO', bg='red', command=pop.destroy)
    no_btn.grid(row=1, column=1, sticky=tk.W)


def create_assessment_report(images, adjustments, text_boxes):
    with open('./data/reba-assessment.json') as f:
        data = json.load(f)

    with open('templates/reba-assessment-report.html') as h:
        soup = BS(h, 'html.parser')
        hot_soup = soup.prettify()

    print(hot_soup)


# create_assessment_report(0, 0, 0)
