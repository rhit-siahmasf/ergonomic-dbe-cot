import tkinter as tk
from tkinter import ttk

from PIL.ImageChops import screen

import StartUpScreen as sus
import AssessmentSelectorScreen as select
import ImageSelectorScreen as image_select
import RulaStepA1Screen as a1
import RulaStepA2Screen as a2
import RulaStepA3Screen as a3
import RulaStepA456Screen as a456
import RulaStepA7Screen as a7
import RulaStepB1Screen as b1
import RulaStepB2Screen as b2
import RulaStepB345Screen as b345
import RulaStepB6Screen as b6
import FinalScreen as fs

root = tk.Tk()
root.title("RULA / REBA Assessment")
tabControl = ttk.Notebook(root, width=1000, height=700)

## create a ttk.Frame for each screen
start_up_screen = sus.create_page(tabControl)
selector_screen = select.create_page(tabControl)
image_screen = image_select.create_page(tabControl)
screen_a1 = a1.create_page(tabControl).master
screen_a2 = a2.create_page(tabControl).master
screen_a3 = a3.create_page(tabControl).master
screen_a456 = a456.create_page(tabControl).master
screen_a7 = a7.create_page(tabControl).master
screen_b1 = b1.create_page(tabControl).master
screen_b2 = b2.create_page(tabControl).master
screen_b345 = b345.create_page(tabControl).master
screen_b6 = b6.create_page(tabControl).master
screen_final = fs.create_page(tabControl)

# add each ttk.Frame to the Notebook
tabControl.add(start_up_screen, text='Begin Rula Reba')
tabControl.add(selector_screen, text='Assessment Selector')
tabControl.add(image_screen, text='Image Selector')
tabControl.add(screen_a1, text='Step A1')
tabControl.add(screen_a2, text='Step A2')
tabControl.add(screen_a3, text='Step A3')
tabControl.add(screen_a456, text='Step A4, A5, & A6')
tabControl.add(screen_a7, text='Step A7')
tabControl.add(screen_b1, text='Step B1')
tabControl.add(screen_b2, text='Step B2')
tabControl.add(screen_b345, text='Step B3, B4, & B5')
tabControl.add(screen_b6, text='Step B6')
tabControl.add(screen_final, text='Final Screen')

# hide all screens except startup from user view
tabControl.hide(selector_screen)
tabControl.hide(image_screen)
tabControl.hide(screen_a1)
tabControl.hide(screen_a2)
tabControl.hide(screen_a3)
tabControl.hide(screen_a456)
tabControl.hide(screen_a7)
tabControl.hide(screen_b1)
tabControl.hide(screen_b2)
tabControl.hide(screen_b345)
tabControl.hide(screen_b6)
tabControl.hide(screen_final)

# All next and back buttons hide AND select a screen based on the label of the button
tk.Button(start_up_screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(start_up_screen),
                           tabControl.select(selector_screen)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(selector_screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(selector_screen),
                           tabControl.select(image_screen)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(selector_screen, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(selector_screen),
                           tabControl.select(start_up_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(image_screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(image_screen),
                           tabControl.select(screen_a1)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(image_screen, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(image_screen),
                           tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a1),
                           tabControl.select(image_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a1, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a1),
                           tabControl.select(screen_a2)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a2),
                           tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a2, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a2),
                           tabControl.select(screen_a3)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a3, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a3),
                           tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a3, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a3),
                           tabControl.select(screen_a456)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a456, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a456),
                           tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a456, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a456),
                           tabControl.select(screen_a7)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a7, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a7),
                           tabControl.select(screen_a456)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a7, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_a7),
                           tabControl.select(screen_b1)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b1),
                           tabControl.select(screen_a7)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b1, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_b1),
                           tabControl.select(screen_b2)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b2),
                           tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b2, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_b2),
                           tabControl.select(screen_b345)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b345, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b345),
                           tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b345, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen_b345),
                           tabControl.select(screen_b6)]).grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b6, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b6),
                           tabControl.select(screen_b345)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tabControl.pack()
root.mainloop()
