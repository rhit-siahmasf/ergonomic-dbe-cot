import tkinter as tk
from tkinter import ttk

from reportlab.lib.pagesizes import *
from reportlab.pdfgen import canvas


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
    page = canvas.Canvas("Reba Assessment Report.pdf", pagesize=(A4[1], A4[0]))
    page.setFont('Times-Roman', 12)
    spaces = 0
    x_cord = 30
    f = open("reba-output.txt", "r")
    for line in f:
        if line == '\n':
            spaces += 1
        elif spaces > 33:
            x_cord = 380
            spaces = 0
            page.drawString(380, 500 - (spaces*10), line)
        else:
            page.drawString(x_cord, 500 - (spaces * 10), line)
            spaces += 1
    page.save()


create_assessment_report(0, 0, 0)

