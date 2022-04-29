import tkinter as tk
from tkinter import ttk

import ScreenManager as sm
import AssessmentSelectorScreen as select

root = tk.Tk()
root.title('REBA Assessment')
tabControl = ttk.Notebook(root, width=1000, height=700)

a1 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 1: Locate Neck Position.',
                      [['step1a-reba-images', 'reba-step1a-1.png'], ['step1a-reba-images', 'reba-step1a-2.png'],
                       ['step1a-reba-images', 'reba-step1a-3.png']], ['A', 'B', 'C'],
                      ['If neck is twisted: (+1)', 'If neck is side bending: (+1)'])
a2 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 2: Locate trunk position.',
                      [['step2a-reba-images', 'reba-step2a-1.png'], ['step2a-reba-images', 'reba-step2a-2.png'],
                       ['step2a-reba-images', 'reba-step2a-3.png'], ['step2a-reba-images', 'reba-step2a-4.png'],
                       ['step2a-reba-images', 'reba-step2a-5.png']], ['A', 'B', 'C', 'D', 'E'],
                      ['If trunk is twisted: (+1)', 'If trunk is side bending: (+1)'])
a3 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 3: Legs',
                      [['step3a-reba-images', 'reba-step3a-1.png'], ['step3a-reba-images', 'reba-step3a-2.png'],
                       ['step3a-reba-images', 'reba-step3a-3.png'], ['step3a-reba-images', 'reba-step3a-4.png']],
                      ['A', 'B', 'C', 'D'], None)
a45 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS',
                       ['Step 4: Posture Score in Table A.', 'Step 5: Add Force/Load Score'], None, None,
                       ['If load < 11lbs: (+0)', 'If load 11 to 22lbs: (+1)',
                        'If load > 22lbs: (+2)', 'If shock or rapid build up of force: (+1)'])
b1 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 7: Locate Upper Arm Position.',
                      [['step7b-reba-images', 'reba-step7b-1.png'], ['step7b-reba-images', 'reba-step7b-2.png'],
                       ['step7b-reba-images', 'reba-step7b-3.png'], ['step7b-reba-images', 'reba-step7b-4.png'],
                       ['step7b-reba-images', 'reba-step7b-5.png']], ['A', 'B', 'C', 'D', 'E'],
                      ['If shoulder raised: (+1)', 'If upper arm is abducted: (+1)',
                       'If arm is supported or person is leaning: (-1)'])
b2 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 8: Locate Lower Arm Position.',
                      [['step1a-reba-images', 'reba-step1a-1.png'], ['step1a-reba-images', 'reba-step1a-2.png'],
                       ['step1a-reba-images', 'reba-step1a-3.png']], ['A', 'B', 'C'],
                      ['If neck is twisted: (+1)', 'If neck is side bending: (+1)'])
b3 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 9: Locate Wrist Position.',
                      [['step8b-reba-images', 'reba-step8b-1.png'], ['step8b-reba-images', 'reba-step8b-2.png']],
                      ['A', 'B'], ['If wrist is bent from midline or twisted (+1)'])

# create a ttk.Frame for each screen
selector_screen = select.create_page(tabControl)
screen_a1 = a1.create_page(tabControl, True)
screen_a2 = a2.create_page(tabControl, True)
screen_a3 = a3.create_page(tabControl, True)
screen_a45 = a45.create_page(tabControl, False)
screen_b1 = b1.create_page(tabControl, True)
screen_b2 = b2.create_page(tabControl, True)
screen_b3 = b3.create_page(tabControl, True)

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
          command=lambda: [get_all_info(a1), tabControl.hide(screen_a1), tabControl.select(screen_a2)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a1),
                           tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a2, text='NEXT', bg='#458B00',
          command=lambda: [get_all_info(a2), tabControl.hide(screen_a2), tabControl.select(screen_a3)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a2),
                           tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a3, text='NEXT', bg='#458B00',
          command=lambda: [get_all_info(a3), tabControl.hide(screen_a3), tabControl.select(screen_a45)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a3, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a3),
                           tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_a45, text='NEXT', bg='#458B00',
          command=lambda: [get_all_info(a45), tabControl.hide(screen_a45), tabControl.select(screen_b1)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_a45, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_a45),
                           tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b1, text='NEXT', bg='#458B00',
          command=lambda: [get_all_info(b1), tabControl.hide(screen_b1), tabControl.select(screen_b2)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b1, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b1),
                           tabControl.select(screen_a45)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b2, text='NEXT', bg='#458B00',
          command=lambda: [get_all_info(b2), tabControl.hide(screen_b2), tabControl.select(screen_b3)])\
    .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
tk.Button(screen_b2, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b2),
                           tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
tk.Button(screen_b3, text='BACK', bg='#8B2323',
          command=lambda: [tabControl.hide(screen_b3),
                           tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)


def get_all_info(screen_manager):
    get_curr_img(screen_manager)
    get_curr_adj(screen_manager)
    get_text_entry(screen_manager)


def get_curr_img(screen_manager):
    print(screen_manager.get_subtitle() + " " + screen_manager.get_image_selection())


def get_curr_adj(screen_manager):
    print(screen_manager.get_subtitle() + " " + screen_manager.get_adjustment_checks())


def get_text_entry(screen_manager):
    print(screen_manager.get_subtitle() + " " + screen_manager.get_user_entry())


tabControl.pack()
root.mainloop()
