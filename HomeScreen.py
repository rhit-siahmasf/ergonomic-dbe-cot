import tkinter as tk
from distutils import command
from tkinter import filedialog
import os
import ScreenManager as sm
from PIL import ImageTk, Image

# creating window master :: all methods in one place
from Tools.scripts import highlight

master = tk.Tk()
master.geometry('700x500')
master.columnconfigure(0, weight=4)
master.columnconfigure(1, weight=1)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)
master.rowconfigure(2, weight=1)
master.rowconfigure(3, weight=1)
master.rowconfigure(4, weight=1)

frame = tk.Frame(master, background='white')
# relative file path
fileDir = os.path.dirname(os.path.realpath(__file__))
# util class
arm_wrist_screen_A3 = []
arm_wrist_screen_A4 = []
arm_wrist_screen_A5 = []
arm_wrist_screen_A6 = []
arm_wrist_screen_A7 = []
first_assessments = [arm_wrist_screen_A3, arm_wrist_screen_A4,
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
        w.grid_remove()


def attach_to_main(widgets):
    for w in widgets:
        w.grid()


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
    #   attach_image_main(easel)
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
img_type = tk.IntVar()
option_type = tk.StringVar()
should_clear = True
should_not_clear = False
default_font = 'Arial'
default_font_size = 14
selection_step_instruction = tk.Label(master, text='Select the necessary adjustment.', font=('Arial', 12))
text_step_instruction = tk.Label(master, text='Explain your adjustment selection. '
                                              'Reference the SPECIFIC part of the body.', font=('Arial', 12))
answer_box = tk.Entry(master, textvariable=answer)
all_others = [selection_step_instruction, text_step_instruction, answer_box]
# ARM & WRIST screens
a_arm_title = sm.TitleWidget(master, 'A. ARM & WRIST ANALYSIS', 0, 0, default_font, 18)
#       attach to all appropriate step screens
for assess in first_assessments:
    assess.append(a_arm_title)
# Step A1 -------------------------------------------------------------------------------------------------------------
# -------------------- IMAGES A1 --------------------------------------------------
a1_img_paths = [os.path.join(fileDir, './step1a-rula -images/rula-step1a-1.png'),
                os.path.join(fileDir, './step1a-rula -images/rula-step1a-2.png'),
                os.path.join(fileDir, './step1a-rula -images/rula-step1a-3.png'),
                os.path.join(fileDir, './step1a-rula -images/rula-step1a-4.png'),
                os.path.join(fileDir, './step1a-rula -images/rula-step1a-5.png')]
a1_step_images = []
a1_column_vals = [0, 1, 2, 0, 1]
for i in range(len(a1_img_paths)):
    row = i % 2
    my_image = sm.ImageWidget(master, a1_img_paths[i], img_type, row, a1_column_vals[i])
    a1_step_images.append(my_image)
# -------------------- OPTIONS A1 --------------------------------------------------
a1_options = ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
              'Arm supported? (i.e. person leaning?) (-1)']
a1_step_options = []
row2 = 2
for s in range(len(a1_options)):
    row += 1
    my_step = sm.CheckButtonWidget(master, option_type, a1_options[s], row, 1)
    a1_step_options.append(my_step)
# --------------------- TITLE A1 ---------------------------------------------------
a1_title = sm.TitleWidget(master, 'Step 1: Locate upper arm position.', 1, 0, default_font, default_font_size)
# --------------------- SCREEN MANAGER A1 ---------------------------------------------------
a1_step_screen = sm.ScreenManager(master, a_arm_title, a1_title, a1_step_images, a1_step_options, all_others)
a1_continue_button = tk.Button(master, text='Continue',
                               command=lambda: a2_step_screen.attach_to_main(True))
# Step 2A -------------------------------------------------------------------------------------------------------------
# -------------------- IMAGES A2 --------------------------------------------------
a2_img_paths = [os.path.join(fileDir, './step2a-rula-images/rula-step2a-1.png'),
                os.path.join(fileDir, './step2a-rula-images/rula-step2a-2.png'),
                os.path.join(fileDir, './step2a-rula-images/rula-step2a-3.png')]
print(os.path.join(fileDir, './step2a-rula-images/rula-step2a-4.png'))
a2_step_images = []
for i in range(len(a2_img_paths)):
    my_image = sm.ImageWidget(master, a2_img_paths[i], img_type, 0, 0)
    a2_step_images.append(my_image)
# -------------------- OPTIONS A2 --------------------------------------------------
a2_options = ['Adjust if arm is working across midline or outside of body: (+1)']
a2_step_options = []
for s in range(len(a2_options)):
    my_step = sm.CheckButtonWidget(master, option_type, a2_options[s], 3, 0)
    a2_step_options.append(my_step)
# --------------------- TITLE A2 ---------------------------------------------------
a2_title = sm.TitleWidget(master, 'Step 2: Locate lower arm position.', 1, 0, default_font, default_font_size)
# --------------------- SCREEN MANAGER A2 ---------------------------------------------------
a2_step_screen = sm.ScreenManager(master, a_arm_title, a2_title, a2_step_images, a2_step_options, all_others)
a2_continue_button = tk.Button(master, text='Continue',
                               command=lambda: a3_step_screen.attach_to_main(True))
# Step 3A -------------------------------------------------------------------------------------------------------------
# -------------------- IMAGES A3 --------------------------------------------------
a3_img_paths = [os.path.join(fileDir, './step3a-rula-images/rula-step3a-1.png'),
                os.path.join(fileDir, './step3a-rula-images/rula-step3a-2.png'),
                os.path.join(fileDir, './step3a-rula-images/rula-step3a-3.png')]
a3_step_images = []
a3_column_vals = [1, 2, 3]
for i in range(len(a3_img_paths)):
    my_image = sm.ImageWidget(master, a3_img_paths[i], img_type, 0, a3_column_vals[i])
    a3_step_images.append(my_image)
# -------------------- OPTIONS A3 --------------------------------------------------
a3_options = ['Adjust if wrist is bent from midline: (+1)']
a3_step_options = []
for s in range(len(a3_options)):
    my_step = sm.CheckButtonWidget(master, option_type, a3_options[s], 3, 1)
    a3_step_options.append(my_step)
# --------------------- TITLE A3 ---------------------------------------------------
a3_title = sm.TitleWidget(master, 'Step 3: Locate wrist position.', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER A3 ---------------------------------------------------
a3_step_screen = sm.ScreenManager(master, a_arm_title, a3_title, a3_step_images, a3_step_options, all_others)
a3_continue_button = tk.Button(master, text='Continue',
                               command=lambda: a4_step_screen.attach_to_main(True))
#   The following steps are on ONE screen
# Step A4 -------------------------------------------------------------------------------------------------------------
a4_options = ['If wrist is twisted in mid-range: (+1)', 'If wrist is at or near end of range: (+2)']
a4_step_options = []
for a in range(len(a4_options)):
    my_step = sm.CheckButtonWidget(master, option_type, a4_options[a], 2, 1)
    a4_step_options.append(my_step)
# --------------------- TITLE A4 ---------------------------------------------------
a4_title = sm.TitleWidget(master, 'Step 4: Wrist twist.', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER A4 ---------------------------------------------------
a4_step_screen = sm.ScreenManager(master, a_arm_title, a4_title, [], a4_step_options, [])
a4_continue_button = tk.Button(master, text='Continue',
                               command=lambda: a5_step_screen.attach_to_main(False))
# Step A5
# --------------------- TITLE A5---------------------------------------------------
a5_title = sm.TitleWidget(master, 'Step 5: Score from table A', 3, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER A5 ---------------------------------------------------
a5_step_screen = sm.ScreenManager(master, '', a5_title, [], [], [])
a5_continue_button = tk.Button(master, text='Continue', command=lambda: a6_step_screen.attach_to_main(False))
# Step A6
a6_option = [sm.CheckButtonWidget(master, option_type, 'Action repeated occurs 4x/minute? '
                                                       'OR is posture mainly static (i.e held >10 minutes)? (+1)', 5,
                                  1)]
# --------------------- TITLE A6 ---------------------------------------------------
a6_title = sm.TitleWidget(master, 'Step 6: Muscle Use', 4, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER A6 ---------------------------------------------------
a6_step_screen = sm.ScreenManager(master, '', a6_title, [], a6_option, [])
a6_continue_button = tk.Button(master, text='Continue', command=lambda: a7_step_screen.attach_to_main(True))
# Step A7 -------------------------------------------------------------------------------------------------------------
a7_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
              'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
a7_step_options = []
for s in range(len(a7_options)):
    my_step = sm.CheckButtonWidget(master, option_type, a7_options[s], 3, 1)
    a7_step_options.append(my_step)
a7_title = sm.TitleWidget(master, 'Step 7: Add Force / Load.', 1, 1, default_font, default_font_size)
a7_step_screen = sm.ScreenManager(master, a_arm_title, a7_title, [], a7_step_options, all_others)
a3_continue_button = tk.Button(master, text='Continue',
                               command=lambda: b1_step_screen.attach_to_main(True))

# NECK, LEG, & TRUNK screens
b_trunk_title = tk.Label(master, text='B. NECK, TRUNK, AND LEG ANALYSIS', font=('Arial', 18))
#       attach to all appropriate step screens
# Step B1 -----------------------------------------------------------------------------------------------
# -------------------- IMAGES B1 --------------------------------------------------
b1_img_paths = [os.path.join(fileDir, './step9b-rula-images/rula-step9b-1.png'),
                os.path.join(fileDir, './step9b-rula-images/rula-step9b-2.png'),
                os.path.join(fileDir, './step9b-rula-images/rula-step9b-3.png'),
                os.path.join(fileDir, './step9b-rula-images/rula-step9b-4.png')]
b1_step_images = []
b1_column_vals = [1, 2, 3, 1]
for i in range(len(b1_img_paths)):
    my_image = sm.ImageWidget(master, b1_img_paths[i], img_type, 0, b1_column_vals[i])
    b1_step_images.append(my_image)
# -------------------- OPTIONS B1 --------------------------------------------------
b1_options = ['Adjust if neck is twisted: (+1)', 'Adjust if neck is side bending: (+1)']
b1_step_options = []
for a in range(len(b1_options)):
    my_step = sm.CheckButtonWidget(master, option_type, b1_options[a], 1, 2)
    b1_step_options.append(my_step)
# --------------------- TITLE B1 ---------------------------------------------------
b1_title = sm.TitleWidget(master, 'Step 9: Locate Neck Position.', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B1 ---------------------------------------------------
b1_step_screen = sm.ScreenManager(master, b_trunk_title, b1_title, b1_step_images, b1_step_options, all_others)
b1_continue_button = tk.Button(master, text='Continue',
                               command=lambda: b2_step_screen.attach_to_main(True))
# Step B2 -----------------------------------------------------------------------------------------------
# -------------------- IMAGES B2 --------------------------------------------------
b2_img_paths = [os.path.join(fileDir, './step10b-rula-images/rula-step10b-1.png'),
                os.path.join(fileDir, './step10b-rula-images/rula-step10b-2.png'),
                os.path.join(fileDir, './step10b-rula-images/rula-step10b-3.png'),
                os.path.join(fileDir, './step10b-rula-images/rula-step10b-4.png')]
b2_step_images = []
b2_column_vals = [1, 2, 3, 1]
for i in range(len(b2_img_paths)):
    my_image = sm.ImageWidget(master, b2_img_paths[i], img_type, 0, b2_column_vals[i])
    b2_step_images.append(my_image)
# -------------------- OPTIONS B1 --------------------------------------------------
b2_options = ['Adjust if trunk is twisted: (+1)', 'Adjust if trunk is side bending: (+1)']
b2_step_options = []
for a in range(len(b2_options)):
    my_step = sm.CheckButtonWidget(master, option_type, b2_options[a], 1, 2)
    b2_step_options.append(my_step)
# --------------------- TITLE B2 ---------------------------------------------------
b2_title = sm.TitleWidget(master, 'Step 10: Locate Trunk Position.', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B2 ---------------------------------------------------
b2_step_screen = sm.ScreenManager(master, b_trunk_title, b2_title, b2_step_images, b2_step_options, all_others)
b2_continue_button = tk.Button(master, text='Continue',
                               command=lambda: b3_step_screen.attach_to_main(True))
#   The following steps are on ONE screen
# Step B3 -----------------------------------------------------------------------------------------------
b3_options = ['If legs and feet are supported: (+1)', 'If NOT supported: (+2)']
b3_step_options = []
for a in range(len(b3_options)):
    my_step = sm.CheckButtonWidget(master, option_type, b3_options[a], 2, 1)
    b3_step_options.append(my_step)
b3_title = sm.TitleWidget(master, 'Step 11: Legs.', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B3 ---------------------------------------------------
b3_step_screen = sm.ScreenManager(master, b_trunk_title, b3_title, [], b3_step_options, [])
b3_continue_button = tk.Button(master, text='Continue',
                               command=lambda: b4_step_screen.attach_to_main(False))
# Step B4
b4_title = sm.TitleWidget(master, 'Step 12: Posture Score from Table.', 3, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B4 ---------------------------------------------------
b4_step_screen = sm.ScreenManager(master, '', b4_title, [], [], [])
b4_continue_button = tk.Button(master, text='Continue', command=lambda: b5_step_screen.attach_to_main(False))
# Step B5
b5_option = [sm.CheckButtonWidget(master, option_type, 'Action repeated occurs 4x/minute? '
                                                       'OR is posture mainly static (i.e held >10 minutes)? (+1)', 4,
                                  1)]
b5_title = sm.TitleWidget(master, 'Step 13: Add Muscle Score.', 4, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B5 ---------------------------------------------------
b5_step_screen = sm.ScreenManager(master, '', b5_title, [], b5_option, [])
b5_continue_button = tk.Button(master, text='Continue', command=lambda: b6_step_screen.attach_to_main(True))
# Step B14 -----------------------------------------------------------------------------------------------
# -------------------- OPTIONS B6 --------------------------------------------------
b6_options = ['If load < 4.4 lbs (intermittent): (+0)', 'If load 4.4 to 22 lbs (intermittent): (+1)',
              'If load 4.4 to 22 lbs (static or repeated): (+2)', 'If more than 22lbs OR repeated or shocks: (+3)']
b6_step_options = []
for s in range(len(b6_options)):
    my_step = sm.CheckButtonWidget(master, option_type, b6_options[s], 3, 1)
    b6_step_options.append(my_step)
# --------------------- TITLE B6 ---------------------------------------------------
b6_title = sm.TitleWidget(master, 'Step 14: Add Force / Load Score', 1, 1, default_font, default_font_size)
# --------------------- SCREEN MANAGER B6 ---------------------------------------------------
b6_step_screen = sm.ScreenManager(master, b_trunk_title, b6_title, [], b6_step_options, all_others)
b6_continue_button = tk.Button(master, text='Continue',
                               command=lambda: b1_step_screen.attach_to_main(True))
# ----------------------------------------------------------------------------------------------------------------------
# widgets for image selection
back_button = tk.Button(master, text='BACK', highlightbackground='green',
                        command=lambda: [clear_screen(),
                                         attach_to_main(selection_screen, "Selection Screen")])
upload_your_file_label = tk.Label(master, text='Please upload an image to begin assessment.', font=('Arial', 18))
file_button_uploader = tk.Button(master, text='Upload', highlightbackground='#000fff000',
                                 command=lambda: [upload_file()])
continue_button = tk.Button(master, text='Continue',
                            command=lambda: a1_step_screen.attach_to_main(True))
image_selection = [back_button, upload_your_file_label, file_button_uploader, continue_button]

# widgets for selection screen
option = tk.IntVar()
reba = tk.Radiobutton(master, text='REBA', var=option, value=1)
rula = tk.Radiobutton(master, text='RULA', var=option, value=2)
existing = tk.Radiobutton(master, text='Open existing assessment', var=option, value=3)
start_selection = tk.Button(master, text='NEXT', highlightbackground='#000fff000',
                            command=lambda: [clear_screen(), set_selection(),
                                             attach_to_main(image_selection)])
selection_screen = [reba, rula, existing, start_selection]

# widgets for home screen
reviewer_name_label = tk.Label(master, text='Name of Reviewer: ')
reviewer_name_entry = tk.Entry(master, textvariable=student_name)
task_name_label = tk.Label(master, text='Task Name: ')
task_name_entry = tk.Entry(master, textvariable=task_name)
date_label = tk.Label(master, text='Date of Assessment: ')
date = tk.Entry(master, textvariable=date_of_observation)
date.insert(0, 'mm/dd/yyyy')

built = Image.open(os.path.join(fileDir, './other-images/depart-of-built.png'))
built = built.resize((140, 100), Image.ANTIALIAS)
final_pic = ImageTk.PhotoImage(built)
final_pic.image = built
built_btn = tk.Label(master, image=final_pic)

coll = Image.open(os.path.join(fileDir, './other-images/College-of-tech.png'))
coll = coll.resize((140, 100), Image.ANTIALIAS)
final_pic2 = ImageTk.PhotoImage(coll)
final_pic2.image = coll
coll_btn = tk.Label(master, image=final_pic2)

rose = Image.open(os.path.join(fileDir, './other-images/rose.png'))
rose = rose.resize((85, 110), Image.ANTIALIAS)
final_pic3 = ImageTk.PhotoImage(rose)
final_pic3.image = rose
rose_btn = tk.Label(master, image=final_pic3)

reviewer_name_label.grid(row=1, column=0,  sticky=tk.NW)
reviewer_name_entry.grid(row=1, column=0, sticky=tk.N)
task_name_label.grid(row=1, column=0, sticky=tk.W)
task_name_entry.grid(row=1, column=0)
date_label.grid(row=1, column=0, sticky=tk.SW)
date.grid(row=1, column=0, sticky=tk.S)
built_btn.grid(row=1, column=1, sticky=tk.N)
coll_btn.grid(row=2, column=1, sticky=tk.N)
rose_btn.grid(row=3, column=1, sticky=tk.N)
begin_assessment_btn = tk.Button(master, text='START',
                                 highlightbackground='#000fff000',
                                 command=lambda: [clear_screen(),
                                                  attach_to_main(selection_screen)])
begin_assessment_btn.grid(row=2, column=0)

master.title('RULA / REBA Assessment')
master.mainloop()
