import tkinter as tk
from tkinter import filedialog
import os
import ScreenManager as sm
from PIL import ImageTk, Image

master = tk.Tk()
master.geometry('1000x750')
master.columnconfigure(0, weight=4)
master.columnconfigure(1, weight=2)
master.rowconfigure(0, weight=2)
master.rowconfigure(1, weight=2)
master.rowconfigure(2, weight=2)
master.rowconfigure(3, weight=2)
master.rowconfigure(4, weight=2)
my_image = None
frame = tk.Frame(master, background='white')
# relative file path
fileDir = os.path.dirname(os.path.realpath(__file__))

# creating window objects for certain "interesting" steps
student_name = tk.StringVar()
task_name = tk.StringVar()
date_of_observation = tk.StringVar()
type_of_assessment = tk.StringVar()
answer = tk.StringVar()
img_type = tk.IntVar()
option_type = tk.StringVar()
should_clear = True
should_not_clear = False
default_font = 'Arial'
default_font_size = 14
entry_height = 40


def next_page():
    master.destroy()
    import AssessmentSelectorScreen


tk.Label(master, text='Name of Reviewer: ').grid(row=1, column=0, sticky=tk.NW)
tk.Entry(master, textvariable=student_name).grid(row=1, column=0, sticky=tk.N)
tk.Label(master, text='Task Name: ').grid(row=2, column=0, sticky=tk.NW)
tk.Entry(master, textvariable=task_name).grid(row=2, column=0, sticky=tk.N)
tk.Label(master, text='Date of Assessment: ').grid(row=3, column=0, sticky=tk.NW)
date = tk.Entry(master, textvariable=date_of_observation)
date.insert(0, 'mm/dd/yyyy')
date.grid(row=3, column=0, sticky=tk.N)

built = Image.open(os.path.join(fileDir, './other-images/depart-of-built.png'))
built = built.resize((140, 100), Image.ANTIALIAS)
final_pic = ImageTk.PhotoImage(built)
built_btn = tk.Label(master, image=final_pic)

coll = Image.open(os.path.join(fileDir, './other-images/College-of-tech.png'))
coll = coll.resize((140, 100), Image.ANTIALIAS)
final_pic2 = ImageTk.PhotoImage(coll)
coll_btn = tk.Label(master, image=final_pic2)

rose = Image.open(os.path.join(fileDir, './other-images/rose.png'))
rose = rose.resize((85, 110), Image.ANTIALIAS)
final_pic3 = ImageTk.PhotoImage(rose)
rose_btn = tk.Label(master, image=final_pic3)

built_btn.grid(row=1, column=1, sticky=tk.N)
coll_btn.grid(row=2, column=1, sticky=tk.N)
rose_btn.grid(row=3, column=1, sticky=tk.N)

tk.Button(master, text='BEGIN', bg='#458B00', command=next_page).grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
master.title('RULA / REBA Assessment')
master.mainloop()
