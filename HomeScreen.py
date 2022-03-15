import tkinter as tk
from tkinter import filedialog
import os
import ScreenManager as sm
from PIL import ImageTk, Image

# creating window master :: all methods in one place
from Tools.scripts import highlight

master = tk.Tk()
master.geometry('700x500')
frame = tk.Frame(master, background='white')
# relative file path
fileDir = os.path.dirname(os.path.realpath(__file__))
frame.pack()
arm_wrist_screen_A1 = []
arm_wrist_screen_A2 = []
arm_wrist_screen_A3 = []
arm_wrist_screen_A4 = []
arm_wrist_screen_A5 = []
arm_wrist_screen_A6 = []
arm_wrist_screen_A7 = []
first_assessments = [arm_wrist_screen_A1, arm_wrist_screen_A2, arm_wrist_screen_A3, arm_wrist_screen_A4,
                     arm_wrist_screen_A5, arm_wrist_screen_A7]
leg_trunk_screen_B1 = []
leg_trunk_screen_B2 = []
leg_trunk_screen_B3 = []
leg_trunk_screen_B4 = []
leg_trunk_screen_B5 = []
leg_trunk_screen_B6 = []
second_assessments = [leg_trunk_screen_B1, leg_trunk_screen_B2, leg_trunk_screen_B3, leg_trunk_screen_B4,
                      leg_trunk_screen_B5, leg_trunk_screen_B6]
conclusion_screen = []


def clear_screen():
    for w in master.winfo_children():
        w.pack_forget()


def attach_to_main(widgets, name):
    for w in widgets:
        w.pack()
    print('On screen ', name)


def attach_image_main(el):
    el.pack()


def set_selection():
    int_def = option.get()
    if int_def == 1:
        type_of_assessment.set("reba")
    elif int_def == 2:
        type_of_assessment.set("rula")
    else:
        # create popup error for users
        print('Error: no assessment selected.')

    print(type_of_assessment.get())


def upload_file():
    global easel
    filename = filedialog.askopenfilename()
#    print('FileName:' + filename)
    img = Image.open(filename)
    img = img.resize((175, 175), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    easel = tk.Label(master, image=img)
    easel.image = img
    attach_image_main(easel)
    for a in first_assessments:
        a.append(easel)
    for b in second_assessments:
        b.append(easel)


# creating window objects for certain "interesting" steps
student_name = tk.StringVar()
task_name = tk.StringVar()
date_of_observation = tk.StringVar()
type_of_assessment = tk.StringVar()
answer = tk.StringVar()
selection_step_instruction = tk.Label(master, text='Select the necessary adjustment.', font=('Arial', 12))
text_step_instruction = tk.Label(master, text='Explain your adjustment selection. '
                                              'Reference the SPECIFIC part of the body.', font=('Arial', 12))
answer_box = tk.Entry(master, textvariable=answer)

# ARM & WRIST screens
a_arm_title = tk.Label(master, text='A. ARM & WRIST ANALYSIS', font=('Arial', 18))
#       attach to all appropriate step screens
for assess in first_assessments:
    assess.append(a_arm_title)
# Step A1 -------------------------------------------------------------------------------------------------------------
a1_step_images = [os.path.join(fileDir, './step1a-rula -images/rula-step1a-1.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-2.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-3.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-4.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-5.png')]
a1_step_options = ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                   'Arm supported? (i.e. person leaning?) (-1)']
a1_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 1: Locate upper arm position.', a1_step_images,
                                  [clear_screen(), attach_to_main(arm_wrist_screen_A2, 'Step 2A')], a1_step_options,
                                  arm_wrist_screen_A1)
arm_wrist_screen_A1.append(selection_step_instruction)
arm_wrist_screen_A1.append(text_step_instruction)
arm_wrist_screen_A1.append(answer_box)
# Step 2A -------------------------------------------------------------------------------------------------------------
a2_step_images = [os.path.join(fileDir, './step2a-rula-images/rula-step2a-1.png'),
                  os.path.join(fileDir, './step2a-rula-images/rula-step2a-2.png'),
                  os.path.join(fileDir, './step2a-rula-images/rula-step2a-3.png')]
a2_step_options = ['Adjust if arm is worrking across midline or outside of body: (+1)']
a2_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 2: Locate lower arm position.', a2_step_images,
                                  [clear_screen(), attach_to_main(arm_wrist_screen_A3, 'Step 3A')], a2_step_options,
                                  arm_wrist_screen_A2)
arm_wrist_screen_A2.append(selection_step_instruction)
arm_wrist_screen_A2.append(text_step_instruction)
arm_wrist_screen_A2.append(answer_box)
# Step 3A -------------------------------------------------------------------------------------------------------------
a3_step_images = [os.path.join(fileDir, './step3a-rula-images/rula-step3a-1.png'),
                  os.path.join(fileDir, './step3a-rula-images/rula-step3a-2.png'),
                  os.path.join(fileDir, './step3a-rula-images/rula-step3a-3.png')]
a3_step_options = ['Adjust if wrist is bent from midline: (+1)']
a3_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 3: Locate wrist position.', a3_step_images,
                                  [clear_screen(), attach_to_main(arm_wrist_screen_A4, 'Step 4A'),
                                   attach_to_main(arm_wrist_screen_A5, 'Step 5A'),
                                   attach_to_main(arm_wrist_screen_A6, 'Step 6A')], a3_step_options,
                                  arm_wrist_screen_A3)
arm_wrist_screen_A3.append(selection_step_instruction)
arm_wrist_screen_A3.append(text_step_instruction)
arm_wrist_screen_A3.append(answer_box)
#   The following steps are on ONE screen
# Step A4 -------------------------------------------------------------------------------------------------------------
a4_step_options = ['If wrist is twisted in mid-range: (+1)', 'If wrist is at or near end of range: (+2)']
a4_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 4: Wrist twist.', [], [], a4_step_options,
                                  arm_wrist_screen_A4)
# Step A5
a_step_five_title = tk.Label(master, text='Step 5: Score from table A', font=('Arial', 14))
arm_wrist_screen_A5.append(a_step_five_title)
# Step A6
a6_step_options = ['Action repeated occurs 4x/minute? '
                   'OR is posture mainly static (i.e held >10 minutes)? (+1)']
a6_step_screen = sm.ScreenManager(master, '', 'Step 6: Muscle use', [],
                                  [clear_screen(), attach_to_main(arm_wrist_screen_A7, 'Step 7A')],
                                  a6_step_options, arm_wrist_screen_A6)
# Step A7 -------------------------------------------------------------------------------------------------------------
a7_step_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                   'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
a7_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 7: Add force/load', [],
                                  [clear_screen(), attach_to_main(leg_trunk_screen_B1, 'Step 9B')],
                                  a7_step_options, arm_wrist_screen_A7)

# NECK, LEG, & TRUNK screens
b_trunk_title = tk.Label(master, text='B. NECK, TRUNK, AND LEG ANALYSIS', font=('Arial', 18))
#       attach to all appropriate step screens
for assess in second_assessments:
    assess.append(b_trunk_title)
# Step B1 -----------------------------------------------------------------------------------------------
b1_step_images = [os.path.join(fileDir, './step9b-rula-images/rula-step9b-1.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-2.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-3.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-4.png')]
b1_step_options = ['Adjust if neck is twisted: (+1)', 'Adjust if neck is side bending: (+1)']
b1_step_screen = sm.ScreenManager(master, b_trunk_title, 'Step 9: Locate Neck Position.', b1_step_images,
                                  [clear_screen(), attach_to_main(leg_trunk_screen_B2, 'Step 10B')], b1_step_options,
                                  leg_trunk_screen_B1)
leg_trunk_screen_B1.append(selection_step_instruction)
leg_trunk_screen_B1.append(text_step_instruction)
leg_trunk_screen_B1.append(answer_box)
# Step B2 -----------------------------------------------------------------------------------------------
b2_step_images = [os.path.join(fileDir, './step10b-rula-images/rula-step10b-1.png'),
                  os.path.join(fileDir, './step10b-rula-images/rula-step10b-2.png'),
                  os.path.join(fileDir, './step10b-rula-images/rula-step10b-3.png'),
                  os.path.join(fileDir, './step10b-rula-images/rula-step10b-4.png')]
b2_step_options = ['Adjust if trunk is twisted: (+1)', 'Adjust if trunk is side bending: (+1)']
b2_step_screen = sm.ScreenManager(master, b_trunk_title, 'Step 10: Locate Trunk Position.', b2_step_images,
                                  [clear_screen(), attach_to_main(leg_trunk_screen_B3, 'Step 11B'),
                                   attach_to_main(leg_trunk_screen_B4, 'Step 12B'),
                                   attach_to_main(leg_trunk_screen_B5, 'Step 13B')],
                                  b2_step_options, leg_trunk_screen_B2)
leg_trunk_screen_B2.append(text_step_instruction)
leg_trunk_screen_B2.append(answer_box)
#   The following steps are on ONE screen
# Step B3 -----------------------------------------------------------------------------------------------
b3_step_options = ['If legs and feet are supported: (+1)', 'If NOT supported: (+2)']
b3_step_screen = sm.ScreenManager(master, b_trunk_title, 'Step 11: Legs.', [], [],
                                  b3_step_options, leg_trunk_screen_B3)
# Step B4
b4_step_title = tk.Label(master, text='Step 12: Posture Score from Table.', font=('Arial', 14))
leg_trunk_screen_B4.append(b4_step_title)
# Step B5
b5_step_options = ['Action repeated occurs 4x/minute? '
                   'OR is posture mainly static (i.e held >10 minutes)? (+1)']
b5_step_screen = sm.ScreenManager(master, '', 'Step 13: Add Muscle Score.', [],
                                  [clear_screen(), attach_to_main(leg_trunk_screen_B6, 'Step 14B')], b5_step_options,
                                  leg_trunk_screen_B5)
# Step B14 -----------------------------------------------------------------------------------------------
b6_step_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                   'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
b6_step_screen = sm.ScreenManager(master, b_trunk_title, 'Step 14: Add Force / Load Score', [],
                                  [clear_screen(), attach_to_main(conclusion_screen, 'Final Screen')],
                                  b6_step_options, leg_trunk_screen_B6)
leg_trunk_screen_B6.append(text_step_instruction)
leg_trunk_screen_B6.append(answer_box)
#----------------------------------------------------------------------------------------------------------------------
# widgets for image selection
back_button = tk.Button(master, text='BACK', highlightbackground='green',
                        command=lambda: [clear_screen(), attach_to_main(selection_screen, "Selection Screen")])
upload_your_file_label = tk.Label(master, text='Please upload an image to begin assessment.', font=('Arial', 18))
file_button_uploader = tk.Button(master, text='Upload', highlightbackground='#000fff000',
                                 command=lambda: [upload_file()])
continue_button = tk.Button(master, text='Contiue', command=lambda: [clear_screen(),
                                                                     attach_to_main(arm_wrist_screen_A1, "Screen A1")])
image_selection = [back_button, upload_your_file_label, file_button_uploader, continue_button]


# widgets for selection screen
option = tk.IntVar()
reba = tk.Radiobutton(master, text='REBA', var=option, value=1)
rula = tk.Radiobutton(master, text='RULA', var=option, value=2)
existing = tk.Radiobutton(master, text='Open existing assessment', var=option, value=3)
start_selection = tk.Button(master, text='NEXT', highlightbackground='#000fff000',
                            command=lambda: [clear_screen(), set_selection(), attach_to_main(image_selection, "Image Selector")])
selection_screen = [reba, rula, existing, start_selection]

# widgets for home screen
reviewer_name_label = tk.Label(master, text='Name of Reviewer: ')
reviewer_name_entry = tk.Entry(master, textvariable=student_name)
task_name_label = tk.Label(master, text='Task Name: ')
task_name_entry = tk.Entry(master, textvariable=task_name)
date_label = tk.Label(master, text='Date of Assessment: ')
date = tk.Entry(master, textvariable=date_of_observation)
date.insert(0, 'mm/dd/yyyy')
begin_assessment_btn = tk.Button(master, text='START',
                                 highlightbackground='#000fff000',
                                 command=lambda: [clear_screen(), attach_to_main(selection_screen, "Selection Screen")])
home_screen = [reviewer_name_label, reviewer_name_entry, task_name_label,
               task_name_entry, date_label, date, begin_assessment_btn]
attach_to_main(home_screen, "Home Screen")

master.title('RULA / REBA Assessment')
master.mainloop()
