import ScreenManager as sm
import StartUpScreen as sus
import RebaMain as rm
import RulaMain as rum
import SelectorScreen as img
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("RULA / REBA Assessment")
tabControl = ttk.Notebook(root, width=1100, height=750)


# creating pages
select = sm.ScreenManager('Select an option to continue.', None, None, None, ['RULA', 'REBA', 'Open Existing...'])

start_screen = sus.create_page(tabControl)
img_screen = img.create_page(tabControl)
screen = select.create_page(tabControl, False)

# adding to Notebook (tab containers)
tabControl.add(start_screen, text='REBA / RULA Assessment Screen')
tabControl.add(screen, text='Select Assessment Type')
tabControl.add(img_screen, text='Upload Image')

tabControl.hide(screen)
tabControl.hide(img_screen)

# add button with on-click method
tk.Button(start_screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(start_screen), tabControl.select(screen)]) \
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen, text='NEXT', bg='#458B00',
          command=lambda: [tabControl.hide(screen), tabControl.select(img_screen)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen),
                           tabControl.select(start_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(img_screen, text='NEXT', bg='#458B00', command=lambda: get_assessment_selection()) \
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(img_screen, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(img_screen),
                           tabControl.select(screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)


def get_assessment_selection():
    information = select.get_adjustment_checks()
    if information == 'REBA':
        rm.start_reba_assessment(tabControl, img_screen, information)
    elif information == 'RULA':
        rum.start_rula_assessment(tabControl, img_screen, information)
    else:
        return "Cannot currently upload previous assessments"


tabControl.pack()
root.mainloop()
