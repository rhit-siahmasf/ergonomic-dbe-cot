import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image

fileDir = os.path.dirname(os.path.realpath(__file__))


def create_page(master):
    global name_entry, task_entry, date

    login = ttk.Frame(master, width=1100, height=750)
    login.columnconfigure(0, weight=4)
    login.columnconfigure(1, weight=2)
    login.rowconfigure(0, weight=2)
    login.rowconfigure(1, weight=2)
    login.rowconfigure(2, weight=2)
    login.rowconfigure(3, weight=2)
    login.rowconfigure(4, weight=2)
    tk.Label(login, text='Name of Reviewer: ', font=('Arial', 18)).grid(row=1, column=0, sticky=tk.NW)
    name_entry = tk.Text(login, width=30, height=3)
    name_entry.grid(row=1, column=0, sticky=tk.N)
    tk.Label(login, text='Task Name: ', font=('Arial', 18)).grid(row=2, column=0, sticky=tk.NW)
    task_entry = tk.Text(login, width=30, height=3)
    task_entry.grid(row=2, column=0, sticky=tk.N)
    tk.Label(login, text='Date of Assessment: ', font=('Arial', 18)).grid(row=3, column=0, sticky=tk.NW)
    date = tk.Text(login, width=30, height=3)
    date.insert('1.0', 'mm/dd/yyyy')
    date.grid(row=3, column=0, sticky=tk.N)

    built = Image.open(os.path.join(fileDir, 'other-images\\depart-of-built.png'))
    built = built.resize((140, 100), Image.ANTIALIAS)
    final_pic = ImageTk.PhotoImage(built)
    built_btn = tk.Label(login, image=final_pic)
    built_btn.image = final_pic

    coll = Image.open(os.path.join(fileDir, 'other-images\\College-of-tech.png'))
    coll = coll.resize((140, 100), Image.ANTIALIAS)
    final_pic2 = ImageTk.PhotoImage(coll)
    coll_btn = tk.Label(login, image=final_pic2)
    coll_btn.image = final_pic2

    rose = Image.open(os.path.join(fileDir, 'other-images\\rose.png'))
    rose = rose.resize((85, 110), Image.ANTIALIAS)
    final_pic3 = ImageTk.PhotoImage(rose)
    rose_btn = tk.Label(login, image=final_pic3)
    rose_btn.image = final_pic3

    built_btn.grid(row=1, column=1, sticky=tk.N)
    coll_btn.grid(row=2, column=1, sticky=tk.N)
    rose_btn.grid(row=3, column=1, sticky=tk.N)

    return login


def get_user_info():
    info = [name_entry.get('1.0', 'end'),
            task_entry.get('1.0', 'end'),
            date.get('1.0', 'end')]
    return info

