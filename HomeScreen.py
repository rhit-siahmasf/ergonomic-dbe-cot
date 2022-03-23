import tkinter as tk
from tkinter import filedialog
import os
import ScreenManager as sm
from PIL import ImageTk, Image

# creating window master :: all methods in one place
from Tools.scripts import highlight

master = tk.Tk()
master.geometry('1000x750')
master.columnconfigure(0, weight=4)
master.columnconfigure(1, weight=2)
master.rowconfigure(0, weight=2)
master.rowconfigure(1, weight=2)
master.rowconfigure(2, weight=2)
master.rowconfigure(3, weight=2)
master.rowconfigure(4, weight=2)
my_image = None
frame = tk.Frame(master, background='white')
# relative file path
fileDir = os.path.dirname(os.path.realpath(__file__))
# util class
forward_list = []
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
    global my_image
    name = filedialog.askopenfilename()
    my_image = sm.ImageWidget(master, name, '', 1, 0, 0, tk.NSEW)


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
entry_height = 40
entry_width = 30
selection_step_instruction = sm.LabelWidget(master, 'Select the necessary adjustment.', 2, 1, default_font,
                                            12, tk.NW)
text_step_instruction = sm.LabelWidget(master, 'Explain your adjustment selection. '
                                               'Reference the SPECIFIC part of the body.', 3, 1, default_font,
                                       12, tk.NW)
answer_box = sm.EntryWidget(master, answer, 3, 1, entry_width, tk.EW)
instrc_items = [selection_step_instruction, text_step_instruction]
# ARM & WRIST screens
a_arm_title = sm.LabelWidget(master, 'A. ARM & WRIST ANALYSIS', 0, 0, default_font, 22, tk.NW)
# NECK, LEG, & TRUNK screens
# b_trunk_title = sm.TitleWidget(master, 'B. NECK, TRUNK, AND LEG ANALYSIS', 0, 0, default_font, 18, tk.W)
# # Step B6 -----------------------------------------------------------------------------------------------
# # -------------------- OPTIONS B6 --------------------------------------------------
# b6_step_options = [sm.CheckButtonWidget(master, option_type, 'If load < 4.4 lbs (intermittent): (+0)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If load 4.4 to 22 lbs (intermittent): (+1)', 1, 1, tk.S),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If load 4.4 to 22 lbs (static or repeated): (+2)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If more than 22lbs OR repeated or shocks: (+3)', 2, 1, tk.S)]
# # --------------------- TITLE B6 ---------------------------------------------------
# b6_title = sm.TitleWidget(master, 'Step 14: Add Force / Load Score', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B6 ---------------------------------------------------
# b6_step_screen = sm.ScreenManager(master, b_trunk_title, b6_title, [], b6_step_options, all_others, None, None)
# # Step B5 -----------------------------------------------------------------------------------------------
# b5_option = [sm.CheckButtonWidget(master, option_type,
#                                   'Action repeated occurs 4x/minute? '
#                                   'OR is posture mainly static (i.e held >10 minutes)? (+1)', 4, 1, tk.N)]
# b5_title = sm.TitleWidget(master, 'Step 13: Add Muscle Score.', 4, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B5 ---------------------------------------------------
# b5_step_screen = sm.ScreenManager(master, '', b5_title, [], b5_option, [], None, b6_step_screen)
# # Step B4-----------------------------------------------------------------------------------------------
# b4_title = sm.TitleWidget(master, 'Step 12: Posture Score from Table.', 3, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B4 ---------------------------------------------------
# b4_step_screen = sm.ScreenManager(master, '', b4_title, [], [], [], None, b5_step_screen)
# # Step B3 -----------------------------------------------------------------------------------------------
# b3_step_options = [sm.CheckButtonWidget(master, option_type, 'If legs and feet are supported: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If NOT supported: (+2)', 1, 1, tk.S)]
# b3_title = sm.TitleWidget(master, 'Step 11: Legs.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B3 ---------------------------------------------------
# b3_step_screen = sm.ScreenManager(master, b_trunk_title, b3_title, [], b3_step_options, [], None, b4_step_screen)
# # Step B2 -----------------------------------------------------------------------------------------------
# # -------------------- IMAGES B2 --------------------------------------------------
# b2_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-3.png'),
#                                  img_type, 0, 1, tk.E),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step10b-rula-images/rula-step10b-4.png'),
#                                  img_type, 1, 1, tk.W)]
# # -------------------- OPTIONS B2 --------------------------------------------------
# b2_step_options = [sm.CheckButtonWidget(master, option_type, 'Adjust if trunk is twisted: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'Adjust if trunk is side bending: (+1)', 1, 1, tk.S)]
# # --------------------- TITLE B2 ---------------------------------------------------
# b2_title = sm.TitleWidget(master, 'Step 10: Locate Trunk Position.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B2 ---------------------------------------------------
# b2_step_screen = sm.ScreenManager(master, b_trunk_title, b2_title, b2_step_images,
#                                   b2_step_options, all_others, None, b3_step_screen)
# # Step B1 -----------------------------------------------------------------------------------------------
# # -------------------- IMAGES B1 --------------------------------------------------
# b1_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-3.png'),
#                                  img_type, 0, 1, tk.E),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step9b-rula-images/rula-step9b-4.png'),
#                                  img_type, 1, 1, tk.W)]
# # -------------------- OPTIONS B1 --------------------------------------------------
# b1_step_options = [sm.CheckButtonWidget(master, option_type, 'Adjust if neck is twisted: (+1)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'Adjust if neck is side bending: (+1)', 2, 1, tk.S)]
# # --------------------- TITLE B1 ---------------------------------------------------
# b1_title = sm.TitleWidget(master, 'Step 9: Locate Neck Position.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B1 ---------------------------------------------------
# b1_step_screen = sm.ScreenManager(master, b_trunk_title, b1_title, b1_step_images,
#                                   b1_step_options, all_others, None, b2_step_screen)
# # Step A7 -------------------------------------------------------------------------------------------------------------
# a7_step_options = [sm.CheckButtonWidget(master, option_type, 'If load < 4.4 lbs (intermittent): (+0)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If load 4.4 to 22 lbs (intermittent): (+1)', 1, 1, tk.S),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If load 4.4 to 22 lbs (static or repeated): (+2)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If more than 22lbs OR repeated or shocks: (+3)', 2, 1, tk.S)]
# a7_title = sm.TitleWidget(master, 'Step 7: Add Force / Load.', 1, 1, default_font, default_font_size, tk.W)
# a7_step_screen = sm.ScreenManager(master, a_arm_title, a7_title, [], a7_step_options, all_others, None, b1_step_screen)
# #   The following steps are on ONE screen
# # Step A6
# a6_step_options = [sm.CheckButtonWidget(master, option_type,
#                                         'Action repeated occurs 4x/minute?'
#                                         ' OR is posture mainly static (i.e held >10 minutes)? (+1)', 3, 1, tk.N)]
# a6_title = sm.TitleWidget(master, 'Step 6: Muscle Use', 4, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER A6 ---------------------------------------------------
# a6_step_screen = sm.ScreenManager(master, '', a6_title, [], a6_step_options, [], None, a7_step_screen)
# # Step A5
# # INSERT LABEL FOR SCORE VALUE HERE @ row=2, column=1
# # --------------------- TITLE A5---------------------------------------------------
# a5_title = sm.TitleWidget(master, 'Step 5: Score from table A', 3, 0, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER A5 ---------------------------------------------------
# a5_step_screen = sm.ScreenManager(master, '', a5_title, [], [], [], None, a6_step_screen)
# # Step A4 -------------------------------------------------------------------------------------------------------------
# a4_step_options = [sm.CheckButtonWidget(master, option_type, 'If wrist is twisted in mid-range: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If wrist is at or near end of range: (+2)', 1, 1,
#                                         tk.NSEW)]
# # --------------------- TITLE A4 ---------------------------------------------------
# a4_title = sm.TitleWidget(master, 'Step 4: Wrist twist.', 1, 0, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER A4 ---------------------------------------------------
# a4_step_screen = sm.ScreenManager(master, a_arm_title, a4_title, [], a4_step_options, [], None, a5_step_screen)
# # Step 3A -------------------------------------------------------------------------------------------------------------
# # -------------------- IMAGES A3 --------------------------------------------------
# a3_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step3a-rula-images/rula-step3a-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step3a-rula-images/rula-step3a-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step3a-rula-images/rula-step3a-3.png'),
#                                  img_type, 0, 1, tk.E)]
# # -------------------- OPTIONS A3 --------------------------------------------------
# a3_step_options = [sm.CheckButtonWidget(master, option_type,
#                                         'Adjust if wrist is bent from midline: (+1)', 2, 1, tk.N)]
# # --------------------- TITLE A3 ---------------------------------------------------
# a3_title = sm.TitleWidget(master, 'Step 3: Locate wrist position.', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER A3 ---------------------------------------------------
# a3_step_screen = sm.ScreenManager(master, a_arm_title, a3_title, a3_step_images, a3_step_options,
#                                   all_others, None, a4_step_screen)
# # Step 2A -------------------------------------------------------------------------------------------------------------
# # -------------------- IMAGES A2 --------------------------------------------------
# a2_step_images = [sm.ImageWidget(master, os.path.join(fileDir, './step1a-rula -images/rula-step2a-1.png'),
#                                  img_type, 0, 1, tk.W),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step1a-rula -images/rula-step2a-2.png'),
#                                  img_type, 0, 1, tk.NSEW),
#                   sm.ImageWidget(master, os.path.join(fileDir, './step1a-rula -images/rula-step2a-3.png'),
#                                  img_type, 0, 1, tk.E)]
# # -------------------- OPTIONS A2 --------------------------------------------------
# a2_step_options = [sm.CheckButtonWidget(master, option_type,
#                                         'Adjust if arm is working across midline or outside of body: (+1)', 2, 1, tk.N)]
# # --------------------- TITLE A2 ---------------------------------------------------
# a2_title = sm.TitleWidget(master, 'Step 2: Locate lower arm position.', 1, 0, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER A2 ---------------------------------------------------
# a2_step_screen = sm.ScreenManager(master, a_arm_title, a2_title, a2_step_images, a2_step_options,
#                                   all_others, None, a3_step_screen)
# Step A1 -------------------------------------------------------------------------------------------------------------
# -------------------- IMAGES A1 --------------------------------------------------
a1_step_images = [sm.ImageWidget(master, './step1a-rula -images/rula-step1a-1.png',
                                 'C', 0, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-2.png',
                                 'B', 0, 1, tk.RIGHT, tk.E),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-3.png',
                                 'A', 0, 1, tk.RIGHT, tk.W),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-4.png',
                                 'D', 1, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-5.png',
                                 'E', 1, 1, tk.RIGHT, tk.E)]
# -------------------- OPTIONS A1 --------------------------------------------------
a1_step_options = [sm.ComboBoxWidget(master, option_type,
                                     ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                                      'Arm supported? (i.e. person leaning?) (-1)'], 2, 1, 40, tk.SW),
                   sm.ComboBoxWidget(master, option_type,
                                     ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
# --------------------- TITLE A1 ---------------------------------------------------
a1_title = sm.LabelWidget(master, 'Step 1: Locate upper arm position.', 0, 0, default_font, 18, tk.W)

def create_all_screens():
    global a1_step_screen
    a1_step_screen = sm.ScreenManager(master, a_arm_title, a1_title, a1_step_images,
                                      a1_step_options, instrc_items, answer_box, my_image, None, None)


# widgets for image selection
back_button = tk.Button(master, text='BACK', highlightbackground='green',
                        command=lambda: [clear_screen(),
                                         attach_to_main(selection_screen, "Selection Screen")])
upload_your_file_label = tk.Label(master, text='Please upload an image to begin assessment.', font=('Arial', 18))
file_button_uploader = tk.Button(master, text='Upload', highlightbackground='#000fff000',
                                 command=upload_file)
continue_button = tk.Button(master, text='Continue',
                            command=lambda: [create_all_screens(), a1_step_screen.display_page(True)])
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
built_btn = tk.Label(master, image=final_pic)

coll = Image.open(os.path.join(fileDir, './other-images/College-of-tech.png'))
coll = coll.resize((140, 100), Image.ANTIALIAS)
final_pic2 = ImageTk.PhotoImage(coll)
coll_btn = tk.Label(master, image=final_pic2)

rose = Image.open(os.path.join(fileDir, './other-images/rose.png'))
rose = rose.resize((85, 110), Image.ANTIALIAS)
final_pic3 = ImageTk.PhotoImage(rose)
rose_btn = tk.Label(master, image=final_pic3)

reviewer_name_label.grid(row=1, column=0, sticky=tk.NW)
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
