import tkinter as tk
import FinalScreen as fs
import ScreenManager as sm

text_boxes = []
adjustment_selections = []
image_selections = []


def start_rula_assessment(tabControl, selector_screen, information, easel):
    screens = []

    a1 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 1: Locate upper arm position.',
                          ['image_10', 'image_11'], ['A: +1', 'B: +2', 'C: +2', 'D: +3', 'E: +4'],
                          ['Shoulder raised?: +1', 'Upper arm abducted?: +1',
                           'Arm supported? (i.e. person leaning?): -1', 'None: +0'])
    a2 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 2: Locate lower arm position.',
                          ['image_12'], ['A: +1', 'B: +2'],
                          ['Adjust if arm is working across midline or outside of body: +1', 'None: +0'])
    a3 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 3: Locate wrist position.',
                          ['image_13'], ['A: +1', 'B: +2', 'C: +3'], ['If wrist is bent from midline: +1', 'None: +0'])
    a456 = sm.ScreenManager('A. ARM & WRIST ANALYSIS',
                            ['Step 4: Wrist twist.', 'Step 5: Score from table A', 'Step 6: Muscle Use'], None,
                            ['If wrist is twisted in mid-range: +1', 'If wrist is at or near end of range: +2',
                             'None: +0'],
                            ['Action repeated occurs 4x/minute? OR is posture mainly static (i.e held longer than ten '
                             'minutes)?: +1', 'None: +0'])
    a7 = sm.ScreenManager('A. ARM & WRIST ANALYSIS', 'Step 7: Add Force / Load.', None,
                          ['If load less than 4.4 lbs (intermittent): +0', 'If load 4.4 to 22 lbs (intermittent): +1',
                           'If load 4.4 to 22 lbs (static or repeated): +2',
                           'If more than 22lbs OR repeated or shocks: +3', 'None: +0'], None)
    b1 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 9: Locate Neck Position.',
                          ['image_14'], ['A: +1', 'B: +2', 'C: +3', 'D: +4'],
                          ['Adjust if neck is twisted: +1', 'Adjust if neck is side bending: +1', 'None: +0'])
    b2 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 10: Locate Trunk Position.',
                          ['image_15', 'image_16'], ['A: +1', 'B: +2', 'C: +3', 'D: +4'],
                          ['Adjust if trunk is twisted: +1', 'Adjust if trunk is side bending: +1', 'None: +0'])
    b345 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS',
                            ['Step 11: Legs.', 'Step 12: Posture Score from Table.', 'Step 13: Add Muscle Score.'],
                            None, ['If legs and feet are supported: +1', 'If NOT supported: +2'],
                            ['Action repeated occurs four times per minute? OR is posture mainly static'
                             ' (i.e held longer than ten minutes)?: +1',
                             'None: +0'])
    b6 = sm.ScreenManager('B. NECK, TRUNK, AND LEG ANALYSIS', 'Step 14: Add Force / Load Score', None,
                          ['If load < 4.4 lbs (intermittent): +0', 'If load 4.4 to 22 lbs (intermittent): +1',
                           'If load 4.4 to 22 lbs (static or repeated): +2',
                           'If more than 22lbs OR repeated or shocks: +3'], None)

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
                               tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15,
                                                                         ipadx=15)
    next_a1 = tk.Button(screen_a1, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a1), tabControl.hide(screen_a1), tabControl.select(screen_a2)])
    next_a1.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a2),
                               tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a2 = tk.Button(screen_a2, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a2), tabControl.hide(screen_a2), tabControl.select(screen_a3)])
    next_a2.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a3, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a3),
                               tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a3 = tk.Button(screen_a3, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a3), tabControl.hide(screen_a3), tabControl.select(screen_a456)])
    next_a3.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a456, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a456),
                               tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a456 = tk.Button(screen_a456, state=tk.DISABLED, text='NEXT', bg='#458B00',
                          command=lambda: [get_all_info(a456), tabControl.hide(screen_a456),
                                           tabControl.select(screen_a7)])
    next_a456.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a7, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a7),
                               tabControl.select(screen_a456)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a7 = tk.Button(screen_a7, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a7), tabControl.hide(screen_a7), tabControl.select(screen_b1)])
    next_a7.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b1, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b1),
                               tabControl.select(screen_a7)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b1 = tk.Button(screen_b1, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b1), tabControl.hide(screen_b1), tabControl.select(screen_b2)])
    next_b1.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b2),
                               tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b2 = tk.Button(screen_b2, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b2), tabControl.hide(screen_b2), tabControl.select(screen_b345)])
    next_b2.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b345, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b345),
                               tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b345 = tk.Button(screen_b345, state=tk.DISABLED, text='NEXT', bg='#458B00',
                          command=lambda: [get_all_info(b345), tabControl.hide(screen_b345),
                                           tabControl.select(screen_b6)])
    next_b345.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b6, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b6),
                               tabControl.select(screen_b345)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b6 = tk.Button(screen_b6, state=tk.DISABLED, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b6), tabControl.hide(screen_b6), tabControl.select(screen_final)])
    next_b6.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_final, text='Save as PDF', bg='#A7B0AF',
              command=lambda: fs.create_rula_assessment_report(get_completed_info(information)))\
        .grid(row=1, column=0, sticky=tk.W, padx=15, ipadx=15)

    tk.Button(screen_a1, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a1, a1))\
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a2, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a2, a2)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a3, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a3, a3)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a456, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a456, a456)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a7, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a7, a7)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b1, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b1, b1)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b2, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b2, b2)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b345, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b345, b345)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b6, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b6, b6)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)

    for scream in screens:
        u_photo = tk.Label(scream.get_tab_master(), image=easel)
        u_photo.image = easel
        u_photo.grid(row=3, column=0, sticky=tk.W, padx=40)


def enable_next(btn, screen_manager):
    if btn['state'] != tk.NORMAL and screen_manager.check_completion():
        btn['state'] = tk.NORMAL
    else:
        btn['state'] = tk.DISABLED


def get_all_info(screen_manager):
    get_curr_img(screen_manager)
    get_curr_adj(screen_manager)
    get_text_entry(screen_manager)


def get_curr_img(screen_manager):
    image_selections.append(screen_manager.get_image_selection())


def get_curr_adj(screen_manager):
    adjustment_selections.append(screen_manager.get_adjustment_checks())


def get_text_entry(screen_manager):
    text_boxes.append(screen_manager.get_user_entry())


def get_completed_info(user_input):
    return [user_input, image_selections, adjustment_selections, text_boxes]
