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
leg_trunk_screen_A1 = []
leg_trunk_screen_A2 = []
leg_trunk_screen_A3 = []
leg_trunk_screen_A4 = []
leg_trunk_screen_A5 = []
leg_trunk_screen_A6 = []
second_assessments = [leg_trunk_screen_A1, leg_trunk_screen_A2, leg_trunk_screen_A3, leg_trunk_screen_A4,
                      leg_trunk_screen_A5, leg_trunk_screen_A6]
conclusion_screen = []


def check_fields(my_fields):
    for f in my_fields:
        if len(f) == 0:
            return False
    return True


def clear_screen():
    for w in master.winfo_children():
        w.pack_forget()


def attach_to_main(widgets, name):
    for w in widgets:
        w.pack()


def attach_image_main(easel):
    easel.pack()


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


def create_description_checks(options):
    desc_vars = []
    desc_type = tk.StringVar()
    for txt in options:
        chk_button = tk.Checkbutton(master, text=txt, variable=desc_type)
        desc_vars.append(chk_button)
    return desc_vars


def create_image_checks(choices):
    img_type = tk.IntVar()
    for img in choices:
        pic = Image.open(img)
        pic = pic.resize((50, 50), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        final_pic = tk.Checkbutton(master, image=pic, variable=img_type)
        final_pic.image = pic
        final_pic.pack(side=tk.LEFT)


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
# Step A1
a1_step_images = [os.path.join(fileDir, './step1a-rula -images/rula-step1a-1.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-2.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-3.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-4.png'),
                  os.path.join(fileDir, './step1a-rula -images/rula-step1a-5.png')]
a1_step_options = ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                   'Arm supported? (i.e. person leaning?) (-1)']
a1_step_screen = sm.ScreenManager(master, a_arm_title, 'Step 1: Locate upper arm position.', a1_step_images,
                                  [clear_screen(), attach_to_main(arm_wrist_screen_A2)], a1_step_options,
                                  arm_wrist_screen_A1)
arm_wrist_screen_A1.append(selection_step_instruction)
arm_wrist_screen_A1.append(text_step_instruction)
arm_wrist_screen_A1.append(answer_box)
# Step 2A
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
# Step A3
a_step_three_title = tk.Label(master, text='Step 3: Locate wrist position.', font=('Arial', 14))
arm_wrist_screen_A3.append(a_step_three_title)
#            options to select
a3_step_options = ['Adjust if wrist is bent from midline: (+1)']
a3_desc_options = create_description_checks(a3_step_options)
arm_wrist_screen_A3.append(text_step_instruction)
arm_wrist_screen_A3.append(answer_box)
a3_step_images = [os.path.join(fileDir, './step3a-rula-images/rula-step3a-1.png'),
                  os.path.join(fileDir, './step3a-rula-images/rula-step3a-2.png'),
                  os.path.join(fileDir, './step3a-rula-images/rula-step3a-3.png')]
a3_continue_button = tk.Button(master, text='Continue',
                               command=lambda: [clear_screen(),
                                                attach_to_main(arm_wrist_screen_A4, 'Step 4A'),
                                                attach_to_main(arm_wrist_screen_A5, 'Step 5A'),
                                                attach_to_main(arm_wrist_screen_A6, 'Step 6A')])
#   The following steps are on ONE screen
# Step A4
a_step_four_title = tk.Label(master, text='Step 4: Wrist twist.', font=('Arial', 14))
arm_wrist_screen_A4.append(a_step_four_title)
a4_step_options = ['If wrist is twisted in mid-range: (+1)', 'If wrist is at or near end of range: (+2)']
a4_desc_checks = create_description_checks(a4_step_options)
for w in a4_desc_checks:
    arm_wrist_screen_A4.append(w)
# Step A5
a_step_five_title = tk.Label(master, text='Step 5: Score from table A', font=('Arial', 14))
arm_wrist_screen_A5.append(a_step_five_title)
# Step A6
a_step_six_title = tk.Label(master, text='Step 6: Muscle use', font=('Arial', 14))
arm_wrist_screen_A6.append(a_step_six_title)
a6_step_options = ['Action repeated occurs 4x/minute? '
                   'OR is posture mainly static (i.e held >10 minutes)? (+1)']
a6_desc_checks = create_description_checks(a6_step_options)
arm_wrist_screen_A6.append(a6_desc_checks[0])
a6_continue_button = tk.Button(master, text='Continue',
                               command=lambda: [clear_screen(), attach_to_main(arm_wrist_screen_A7, "Step 7A")])
arm_wrist_screen_A6.append(a6_continue_button)
# Step A7
a_step_seven_title = tk.Label(master, text='Step 7: Add force/load', font=('Arial', 14))
arm_wrist_screen_A7.append(a_step_seven_title)
a7_step_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                   'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
a7_desc_checks = create_description_checks(a7_step_options)
for fl in a7_desc_checks:
    arm_wrist_screen_A7.append(fl)
a7_continue_button = tk.Button(master, text='Continue',
                               command=lambda: [clear_screen(), attach_to_main(leg_trunk_screen_A1, 'Step 9B'),
                                                create_image_checks(b9_step_images),
                                                attach_to_main([b9_continue_button], "Continue")])
arm_wrist_screen_A7.append(a7_continue_button)

# NECK, LEG, & TRUNK screens
b_trunk_title = tk.Label(master, text='B. NECK, TRUNK, AND LEG'
                                      ' ANALYSIS', font=('Arial', 18))
#       attach to all appropriate step screens
for assess in second_assessments:
    assess.append(b_trunk_title)
# Step B9 -----------------------------------------------------------------------------------------------
b_step_nine_title = tk.Label(master, text='Step 9: Locate Neck Position.', font=('Arial', 14))
leg_trunk_screen_A1.append(b_step_nine_title)
b1_step_options = ['Adjust if neck is twisted: (+1)', 'Adjust if neck is side bending: (+1)']
b1_desc_checks = create_description_checks(b1_step_options)
for d in b1_desc_checks:
    leg_trunk_screen_A1.append(d)
b9_step_images = [os.path.join(fileDir, './step9b-rula-images/rula-step9b-1.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-2.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-3.png'),
                  os.path.join(fileDir, './step9b-rula-images/rula-step9b-4.png')]
leg_trunk_screen_A1.append(text_step_instruction)
leg_trunk_screen_A1.append(answer_box)
b9_continue_button = tk.Button(master, text='Continue',
                               command=lambda: [clear_screen(), attach_to_main(leg_trunk_screen_A2, 'Step 10B'),
                                                create_image_checks(b10_step_images)])
leg_trunk_screen_A1.append(b9_continue_button)
# Step B10 -----------------------------------------------------------------------------------------------
b_step_ten_title = tk.Label(master, text='Step 10: Locate Trunk Position.', font=('Arial', 14))
leg_trunk_screen_A2.append(b_step_ten_title)
b2_step_options = ['Adjust if trunk is twisted: (+1)', 'Adjust if trunk is side bending: (+1)']
b2_desc_checks = create_description_checks(b2_step_options)
for t in b2_desc_checks:
    leg_trunk_screen_A2.append(t)
b10_step_images = [os.path.join(fileDir, './step10b-rula-images/rula-step10b-1.png'),
                   os.path.join(fileDir, './step10b-rula-images/rula-step10b-2.png'),
                   os.path.join(fileDir, './step10b-rula-images/rula-step10b-3.png'),
                   os.path.join(fileDir, './step10b-rula-images/rula-step10b-4.png')]
leg_trunk_screen_A2.append(text_step_instruction)
leg_trunk_screen_A2.append(answer_box)
b10_continue_button = tk.Button(master, text='Continue',
                                command=lambda: [clear_screen(), attach_to_main(leg_trunk_screen_A3, 'Step 11B'),
                                                 attach_to_main(leg_trunk_screen_A4, 'Step 12B'),
                                                 attach_to_main(leg_trunk_screen_A5, 'Step 13B')])
leg_trunk_screen_A2.append(b10_continue_button)
# Step B11 -----------------------------------------------------------------------------------------------
b_step_eleven_title = tk.Label(master, text='Step 11: Legs.', font=('Arial', 14))
leg_trunk_screen_A3.append(b_step_eleven_title)
b3_step_options = ['If legs and feet are supported: (+1)', 'If NOT supported: (+2)']
b3_desc_checks = create_description_checks(b3_step_options)
for y in b3_desc_checks:
    leg_trunk_screen_A3.append(y)
# Step B12 -----------------------------------------------------------------------------------------------
b_step_twelve_title = tk.Label(master, text='Step 12: Posture Score from Table', font=('Arial', 14))
leg_trunk_screen_A4.append(b_step_twelve_title)
# Step B13 -----------------------------------------------------------------------------------------------
b_step_thirt_title = tk.Label(master, text='Step 13: Add Muscle Score', font=('Arial', 14))
leg_trunk_screen_A5.append(b_step_thirt_title)
b5_step_options = ['Action repeated occurs 4x/minute? '
                   'OR is posture mainly static (i.e held >10 minutes)? (+1)']
b5_desc_checks = create_description_checks(b5_step_options)
for c in b5_desc_checks:
    leg_trunk_screen_A5.append(c)
b13_continue_button = tk.Button(master, text='Continue',
                                command=lambda: [clear_screen(), attach_to_main(leg_trunk_screen_A6, 'Step 14B')])
leg_trunk_screen_A5.append(b13_continue_button)
# Step B14 -----------------------------------------------------------------------------------------------
b_step_fourteen_title = tk.Label(master, text='Step 14: Add Force / Load Score', font=('Arial', 14))
leg_trunk_screen_A6.append(b_step_fourteen_title)
b6_step_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
                   'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
b6_desc_checks = create_description_checks(b6_step_options)
for b in b6_desc_checks:
    leg_trunk_screen_A6.append(b)
leg_trunk_screen_A6.append(text_step_instruction)
leg_trunk_screen_A6.append(answer_box)
b14_continue_button = tk.Button(master, text='Continue',
                                command=lambda: [clear_screen(), attach_to_main(conclusion_screen, 'Final Screen')])
leg_trunk_screen_A6.append(b14_continue_button)
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
