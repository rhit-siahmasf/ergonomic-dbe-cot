import os
import tkinter as tk
import FinalScreen as fs
import ScreenManager as sm
from PIL import ImageTk, Image


def start_rula_assessment(tabControl, selector_screen, information, easel):
    screens = []

    a1 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 1: Locate upper arm position.',
                          ['rula-images\\A1.png', 'rula-images\\A1-2.png'], ['A', 'B', 'C', 'D', 'E'],
                          ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                           'Arm supported? (i.e. person leaning?) (-1)'])
    a2 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 2: Locate lower arm position.',
                          ['rula-images\\A2.png'], ['A', 'B', 'C'],
                          ['Adjust if arm is working across midline or outside of body: (+1)'])
    a3 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 3: Locate wrist position.',
                          ['rula-images\\A3.png'], ['A', 'B', 'C'], None)
    a456 = sm.ScreenManager('A. ARM & WRIST ANALYSIS',
                            ['Step 4: Wrist twist.', 'Step 5: Score from table A', 'Step 6: Muscle Use'], None,
                            ['If wrist is twisted in mid-range: (+1)', 'If wrist is at or near end of range: (+2)'],
                            ['Action repeated occurs 4x/minute? OR is posture mainly static (i.e held >10 '
                                'minutes)? (+1)'])
    a7 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 7: Add Force / Load.', None,
                          ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                           'If load 4.4 to 22 lbs (static or repeated): (+2)',
                           'If more than 22lbs OR repeated or shocks: (+3)'], None)
    b1 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 9: Locate Neck Position.',
                          ['rula-images\\B1.png', 'rula-images\\B1-2.png'], ['A', 'B', 'C', 'D'],
                          ['Adjust if neck is twisted: (+1)', 'Adjust if neck is side bending: (+1)'])
    b2 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 10: Locate Trunk Position.',
                          ['rula-images\\B2.png', 'rula-images\\B2-2.png'], ['A', 'B', 'C', 'D'],
                          ['Adjust if trunk is twisted: (+1)', 'Adjust if trunk is side bending: (+1)'])
    b345 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS',
                            ['Step 11: Legs.', 'Step 12: Posture Score from Table.', 'Step 13: Add Muscle Score.'],
                            None, ['If legs and feet are supported: (+1)', 'If NOT supported: (+2)'],
                            ['Action repeated occurs 4x/minute? OR is posture mainly static (i.e held >10 minutes)? (+1)'])
    b6 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 14: Add Force / Load Score', None,
                          ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                           'If load 4.4 to 22 lbs (static or repeated): (+2)',
                           'If more than 22lbs OR repeated or shocks: (+3)'], None)

    screens.append(a1)
    screens.append(a2)
    screens.append(a3)
    screens.append(a456)
    screens.append(a7)
    screens.append(b1)
    screens.append(b2)
    screens.append(b345)
    screens.append(b6)

    screen_a1 = a1.create_page(tabControl, True)
    screen_a2 = a2.create_page(tabControl, True)
    screen_a3 = a3.create_page(tabControl, True)
    screen_a456 = a456.create_page(tabControl, False)
    screen_a7 = a7.create_page(tabControl, True)
    screen_b1 = b1.create_page(tabControl, True)
    screen_b2 = b2.create_page(tabControl, True)
    screen_b345 = b345.create_page(tabControl, False)
    screen_b6 = b6.create_page(tabControl, True)
    screen_final = fs.create_page(tabControl)

    # # add each ttk.Frame to the Notebook
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

    # # hide all screens except startup from user view
    tabControl.hide(selector_screen)
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
    tk.Button(screen_a1, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a1),
                               tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_a1, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(a1), tabControl.hide(screen_a1), tabControl.select(screen_a2)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a2),
                               tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_a2, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(a2), tabControl.hide(screen_a2), tabControl.select(screen_a3)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a3, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a3),
                               tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_a3, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(a3), tabControl.hide(screen_a3), tabControl.select(screen_a456)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a456, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a456),
                               tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_a456, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(a456), tabControl.hide(screen_a456), tabControl.select(screen_a7)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a7, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a7),
                               tabControl.select(screen_a456)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_a7, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(a7), tabControl.hide(screen_a7), tabControl.select(screen_b1)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b1, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b1),
                               tabControl.select(screen_a7)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_b1, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(b1), tabControl.hide(screen_b1), tabControl.select(screen_b2)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b2),
                               tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_b2, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(b2), tabControl.hide(screen_b2), tabControl.select(screen_b345)]) \
        .grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b345, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b345),
                               tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(screen_b345, text='NEXT', bg='#458B00',
              command=lambda: [get_all_info(b345), tabControl.hide(screen_b345), tabControl.select(screen_b6)]).grid(
        row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b6, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b6),
                               tabControl.select(screen_b345)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)

    for scream in screens:
        u_photo = tk.Label(scream.get_tab_master(), image=easel)
        u_photo.image = easel
        u_photo.grid(row=3, column=0, sticky=tk.W, padx=40)


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
