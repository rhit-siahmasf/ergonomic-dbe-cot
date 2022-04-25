import tkinter as tk
from tkinter import ttk

import AssessmentSelectorScreen as select
import RebaStepA1Screen as a1
import RebaStepA2Screen as a2
import RebaStepA3Screen as a3
import RebaStepA45Screen as a45
import RebaStepB1Screen as b1
import RebaStepB2Screen as b2
import RebaStepB3Screen as b3

root = tk.Tk()
root.title('REBA Assessment')
tabControl = ttk.Notebook(root, width=1000, height=700)


# create a ttk.Frame for each screen
selector_screen = select.create_page(tabControl)
screen_a1 = a1.create_page(tabControl).master
screen_a2 = a2.create_page(tabControl).master
screen_a3 = a3.create_page(tabControl).master
screen_a45 = a45.create_page(tabControl).master
screen_b1 = b1.create_page(tabControl).master
screen_b2 = b2.create_page(tabControl).master
screen_b3 = b3.create_page(tabControl).master

# add each ttk.Frame to the Notebook
tabControl.add(selector_screen, text='Select Assessment')
tabControl.add(screen_a1, text='Step A1')
tabControl.add(screen_a2, text='Step A2')
tabControl.add(screen_a3, text='Step A3')
tabControl.add(screen_a45, text='Step A4 & A5')
tabControl.add(screen_b1, text='Step B1')
tabControl.add(screen_b2, text='Step B2')
tabControl.add(screen_b3, text='Step B3')

tabControl.hide(screen_a1)
tabControl.hide(screen_a2)
tabControl.hide(screen_a3)
tabControl.hide(screen_a45)
tabControl.hide(screen_b1)
tabControl.hide(screen_b2)
tabControl.hide(screen_b3)


tk.Button(selector_screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(selector_screen),
                           tabControl.select(screen_a1)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a1, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a1),
                           tabControl.select(screen_a2)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a1),
                           tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a2, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a2),
                           tabControl.select(screen_a3)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a2),
                           tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a3, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a3),
                           tabControl.select(screen_a45)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a3, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a3),
                           tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a45, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a45),
                           tabControl.select(screen_b1)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a45, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a45),
                           tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b1, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_b1),
                           tabControl.select(screen_b2)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b1),
                           tabControl.select(screen_a45)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b2, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_b2),
                           tabControl.select(screen_b3)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b2),
                           tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b3, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b3),
                           tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)

tabControl.pack()
root.mainloop()
