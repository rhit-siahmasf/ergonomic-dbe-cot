import tkinter as tk
import ScreenManager as sm
import FinalScreen as fs

text_boxes = []
adjustment_selections = []
image_selections = []


def start_reba_assessment(tabControl, selector_screen, information, easel):
    screens = []

    a1 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 1: Locate Neck Position.',
                          ['image_1'], ['A: +1', 'B: +2', 'C: +2'],
                          ['If neck is twisted: +1', 'If neck is side bending: +1', 'None: +0'])
    a2 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 2: Locate trunk position.',
                          ['image_2', 'image_3'], ['A: +1', 'B: +2', 'C: +2', 'D: +3', 'E: +4'],
                          ['If trunk is twisted: +1', 'If trunk is side bending: +1', 'None: +0'])
    a3 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS', 'Step 3: Legs',
                          ['image_4', 'image_5'], ['A: +1', 'B: +1'], ['Adjust 30-60: +1', '>60: +2', 'None: +0'])
    a45 = sm.ScreenManager('A. NECK, TRUNK, AND LEG ANALYSIS',
                           ['Step 4: Posture Score in Table A.', 'Step 5: Add Force/Load Score'], None, None,
                           ['If load less than 11lbs: +0', 'If load 11 to 22lbs: +1',
                            'If load greater than 22lbs: +2', 'If shock or rapid build up of force: +1'])
    b1 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 7: Locate Upper Arm Position.',
                          ['image_6', 'image_7'], ['A: +1', 'B: +2', 'C: +2', 'D: +3', 'E: +4'],
                          ['If shoulder raised: +1', 'If upper arm is abducted: +1',
                           'If arm is supported or person is leaning: -1', 'None: +0'])
    b2 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 8: Locate Lower Arm Position.',
                          ['image_8'], ['A: +1', 'B: +2'], None)
    b3 = sm.ScreenManager('B. ARM & WRIST ANALYSIS', 'Step 9: Locate Wrist Position.',
                          ['image_9'], ['A: +1', 'B: +2'], ['If wrist is bent from midline or twisted: +1', 'None: +0'])
    b45 = sm.ScreenManager('B. ARM & WRIST ANALYSIS',
                           ['Step 10: Look Up Posture Score in Table B:', 'Step 11: Add Coupling Score'],
                           None, None, ['Well fitting handle and mid-range power grip (good): +0',
                                        'Acceptable but not ideal hand hold or coupling acceptable with another'
                                        ' body part (fair): +1', 'Hand hold not acceptable but possible (poor): +2',
                                        'No handles, awkward, unsage with any body part (unacceptable): +3'])
    b6 = sm.ScreenManager('B.ARM & WRIST ANALYSIS', 'Step 13: Activity Score', None, None,
                          ['One or more body parts are held for longer than one static: +1',
                           'Repeated small range actions; more than four times per minutes: +1',
                           'Action causes rapid large range changes in posture or unstable base: +1',
                           'None: +0'])

    screens.append(a1)
    screens.append(a2)
    screens.append(a3)
    screens.append(a45)
    screens.append(b1)
    screens.append(b2)
    screens.append(b3)
    screens.append(b45)
    screens.append(b6)

    # create a ttk.Frame for each screen
    screen_a1 = a1.create_page(tabControl, True)
    screen_a2 = a2.create_page(tabControl, True)
    screen_a3 = a3.create_page(tabControl, True)
    screen_a45 = a45.create_page(tabControl, False)
    screen_b1 = b1.create_page(tabControl, True)
    screen_b2 = b2.create_page(tabControl, True)
    screen_b3 = b3.create_page(tabControl, True)
    screen_b45 = b45.create_page(tabControl, False)
    screen_b6 = b6.create_page(tabControl, False)
    final = fs.create_page(tabControl)

    # add each ttk.Frame to the Notebook
    tabControl.add(screen_a1, text='Step A1')
    tabControl.add(screen_a2, text='Step A2')
    tabControl.add(screen_a3, text='Step A3')
    tabControl.add(screen_a45, text='Step A4 & A5')
    tabControl.add(screen_b1, text='Step B1')
    tabControl.add(screen_b2, text='Step B2')
    tabControl.add(screen_b3, text='Step B3')
    tabControl.add(screen_b45, text='Step B4 & B5')
    tabControl.add(screen_b6, text='Step B6')
    tabControl.add(final, text='Final Screen')

    tabControl.hide(selector_screen)
    tabControl.hide(screen_a2)
    tabControl.hide(screen_a3)
    tabControl.hide(screen_a45)
    tabControl.hide(screen_b1)
    tabControl.hide(screen_b2)
    tabControl.hide(screen_b3)
    tabControl.hide(screen_b45)
    tabControl.hide(screen_b6)
    tabControl.hide(final)

    next_a1 = tk.Button(screen_a1, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a1), tabControl.hide(screen_a1), tabControl.select(screen_a2)])
    next_a1.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a1, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a1),
                               tabControl.select(selector_screen)]).grid(row=4, column=0, sticky=tk.E, padx=15,
                                                                         ipadx=15)
    next_a2 = tk.Button(screen_a2, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a2), tabControl.hide(screen_a2), tabControl.select(screen_a3)])
    next_a2.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a2),
                               tabControl.select(screen_a1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a3 = tk.Button(screen_a3, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a3), tabControl.hide(screen_a3), tabControl.select(screen_a45)])
    next_a3.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a3, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a3),
                               tabControl.select(screen_a2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_a4 = tk.Button(screen_a45, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(a45), tabControl.hide(screen_a45), tabControl.select(screen_b1)])
    next_a4.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_a45, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_a45),
                               tabControl.select(screen_a3)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b1 = tk.Button(screen_b1, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b1), tabControl.hide(screen_b1), tabControl.select(screen_b2)])
    next_b1.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b1, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b1),
                               tabControl.select(screen_a45)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b2 = tk.Button(screen_b2, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b2), tabControl.hide(screen_b2), tabControl.select(screen_b3)])
    next_b2.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b2, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b2),
                               tabControl.select(screen_b1)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b3 = tk.Button(screen_b3, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b3), tabControl.hide(screen_b3), tabControl.select(screen_b45)])
    next_b3.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b3, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b3),
                               tabControl.select(screen_b2)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b45 = tk.Button(screen_b45, text='NEXT', bg='#458B00',
                         command=lambda: [get_all_info(b45), tabControl.hide(screen_b45), tabControl.select(screen_b6)])
    next_b45.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b45, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b45),
                               tabControl.select(screen_b6)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    next_b6 = tk.Button(screen_b6, text='NEXT', bg='#458B00',
                        command=lambda: [get_all_info(b6), tabControl.hide(screen_b6), tabControl.select(final)])
    next_b6.grid(row=4, column=1, sticky=tk.W, padx=15, ipadx=15)
    tk.Button(screen_b6, text='BACK', bg='#8B2323',
              command=lambda: [tabControl.hide(screen_b6),
                               tabControl.select(screen_b45)]).grid(row=4, column=0, sticky=tk.E, padx=15, ipadx=15)
    tk.Button(final, text='Save as PDF', bg='#A7B0AF',
              command=lambda: fs.create_reba_assessment_report(get_completed_info(information))) \
        .grid(row=1, column=0, sticky=tk.W, padx=15, ipadx=15)

    tk.Button(screen_a1, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a1, a1)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a2, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a2, a2)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a3, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a3, a3)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_a45, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_a4, a45)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b1, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b1, b1)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b2, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b2, b2)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b3, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b3, b3)) \
        .grid(row=3, column=1, sticky=tk.E, padx=200, ipadx=15)
    tk.Button(screen_b45, text='Save Answer', bg='#0675BB', command=lambda: enable_next(next_b45, b45)) \
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
