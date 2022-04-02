
# tk.Label(master, text='Name of Reviewer: ', font=('Arial', 18)).grid(row=1, column=0, sticky=tk.NW)
# tk.Entry(master, textvariable=student_name).grid(row=1, column=0, sticky=tk.N)
# tk.Label(master, text='Task Name: ', font=('Arial', 18)).grid(row=2, column=0, sticky=tk.NW)
# tk.Entry(master, textvariable=task_name).grid(row=2, column=0, sticky=tk.N)
# tk.Label(master, text='Date of Assessment: ', font=('Arial', 18)).grid(row=3, column=0, sticky=tk.NW)
# date = tk.Entry(master, textvariable=date_of_observation)
# date.insert(0, 'mm/dd/yyyy')
# date.grid(row=3, column=0, sticky=tk.N)
#
# built = Image.open(os.path.join(fileDir, './other-images/depart-of-built.png'))
# built = built.resize((140, 100), Image.ANTIALIAS)
# final_pic = ImageTk.PhotoImage(built)
# built_btn = tk.Label(master, image=final_pic)
#
# coll = Image.open(os.path.join(fileDir, './other-images/College-of-tech.png'))
# coll = coll.resize((140, 100), Image.ANTIALIAS)
# final_pic2 = ImageTk.PhotoImage(coll)
# coll_btn = tk.Label(master, image=final_pic2)
#
# rose = Image.open(os.path.join(fileDir, './other-images/rose.png'))
# rose = rose.resize((85, 110), Image.ANTIALIAS)
# final_pic3 = ImageTk.PhotoImage(rose)
# rose_btn = tk.Label(master, image=final_pic3)
#
# built_btn.grid(row=1, column=1, sticky=tk.N)
# coll_btn.grid(row=2, column=1, sticky=tk.N)
# rose_btn.grid(row=3, column=1, sticky=tk.N)
#
# ## move to center
# tk.Button(master, text='BEGIN', bg='#458B00', command=next_page).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
# master.title('RULA / REBA Assessment')
# master.mainloop()

import tkinter as tk
from tkinter import ttk
import StepA1Screen as a1
import StepA2Screen as a2
# import StepA3Screen as a3
# import StepA456Screen as a456
# import StepA7Screen as a7
root = tk.Tk()
root.title("RULA / REBA Assessment")
tabControl = ttk.Notebook(root, width=1000, height=700)

screen_a1 = a1.create_page(tabControl)
# screen_a2 = a2.create_page(tabControl)
# screen_a3 = a3.create_page(tabControl)
# screen_a456 = a456.create_page(tabControl)
# screen_a7 = a7.create_page(tabControl)

tabControl.add(screen_a1, text='Step A1', sticky=tk.NSEW)
# tabControl.add(screen_a2, text='Step A2')
# tabControl.add(screen_a3, text='Step A3')
# tabControl.add(screen_a456, text='Step A456')
# tabControl.add(screen_a7, text='Step A7')
tabControl.pack()
root.mainloop()
