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


# ARM & WRIST screens


# NECK, LEG, & TRUNK screens
# b_trunk_title = sm.LabelWidget(master, 'B. NECK, TRUNK, AND LEG ANALYSIS', 0, 0, default_font, 18, tk.W)
# # Step B6 -----------------------------------------------------------------------------------------------
# # -------------------- OPTIONS B6 --------------------------------------------------
# b6_step_options = [sm.CheckButtonWidget(master, option_type, 'If load < 4.4 lbs (intermittent): (+0)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If load 4.4 to 22 lbs (intermittent): (+1)', 1, 1, tk.S),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If load 4.4 to 22 lbs (static or repeated): (+2)', 2, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type,
#                                         'If more than 22lbs OR repeated or shocks: (+3)', 2, 1, tk.S)]
# # --------------------- TITLE B6 ---------------------------------------------------
# b6_title = sm.LabelWidget(master, 'Step 14: Add Force / Load Score', 1, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B6 ---------------------------------------------------
# b6_step_screen = sm.ScreenManager(master, b_trunk_title, b6_title, [], b6_step_options, all_others, None, None)
# # Step B5 -----------------------------------------------------------------------------------------------
# b5_option = [sm.CheckButtonWidget(master, option_type,
#                                   'Action repeated occurs 4x/minute? '
#                                   'OR is posture mainly static (i.e held >10 minutes)? (+1)', 4, 1, tk.N)]
# b5_title = sm.LabelWidget(master, 'Step 13: Add Muscle Score.', 4, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B5 ---------------------------------------------------
# b5_step_screen = sm.ScreenManager(master, '', b5_title, [], b5_option, [], None, b6_step_screen)
# # Step B4-----------------------------------------------------------------------------------------------
# b4_title = sm.LabelWidget(master, 'Step 12: Posture Score from Table.', 3, 1, default_font, default_font_size, tk.W)
# # --------------------- SCREEN MANAGER B4 ---------------------------------------------------
# b4_step_screen = sm.ScreenManager(master, '', b4_title, [], [], [], None, b5_step_screen)
# # Step B3 -----------------------------------------------------------------------------------------------
# b3_step_options = [sm.CheckButtonWidget(master, option_type, 'If legs and feet are supported: (+1)', 1, 1, tk.N),
#                    sm.CheckButtonWidget(master, option_type, 'If NOT supported: (+2)', 1, 1, tk.S)]
# b3_title = sm.LabelWidget(master, 'Step 11: Legs.', 1, 1, default_font, default_font_size, tk.W)
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
# b2_title = sm.LabelWidget(master, 'Step 10: Locate Trunk Position.', 1, 1, default_font, default_font_size, tk.W)
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
# b1_title = sm.LabelWidget(master, 'Step 9: Locate Neck Position.', 1, 1, default_font, default_font_size, tk.W)


def first_screen():
    master.destroy()
    import StepA1Screen


# widgets for image selection
back_button = tk.Button(master, text='BACK', highlightbackground='green',
                        command=lambda: [clear_screen(),
                                         attach_to_main(selection_screen, "Selection Screen")])
upload_your_file_label = tk.Label(master, text='Please upload an image to begin assessment.', font=('Arial', 18))
file_button_uploader = tk.Button(master, text='Upload', highlightbackground='#000fff000',
                                 command=upload_file)
continue_button = tk.Button(master, text='Continue',
                            command=lambda: [first_screen()])
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


def go_back_prev_page(self):
    self.clear_screen()
    self.prev_screen_manager.display_page()


def continue_next_page(self):
    self.clear_screen()
    self.next_screen_manager.display_page()


master.title('RULA / REBA Assessment')
master.mainloop()
