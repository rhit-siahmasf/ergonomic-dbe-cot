import tkinter as tk
import ScreenManager as sm

master = tk.Tk()
master.geometry('1000x750')
master.columnconfigure(0, weight=4)
master.columnconfigure(1, weight=2)
master.rowconfigure(0, weight=2)
master.rowconfigure(1, weight=2)
master.rowconfigure(2, weight=2)
master.rowconfigure(3, weight=2)
master.rowconfigure(4, weight=2)
option_type = tk.StringVar()
answer = tk.StringVar()
default_font = 'Arial'
text_font_size = 12
default_font_size = 18
title_font_size = 22
entry_width = 30
my_image = None


def next_page():
    master.destroy()
    import StepA2Screen


# def prev_page():
#     ws.destroy()
#     import ImagePickerScreen


def attach_buttons():
    cont_btn = tk.Button(master, text='NEXT', bg='#458B00',
                         command=next_page)
    back_button = tk.Button(master, text='BACK', bg='#8B2323')
    back_button.grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)
    cont_btn.grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)


selection_step_instruction = sm.LabelWidget(master, 'Select the necessary adjustment.', 2, 1, default_font,
                                            text_font_size, tk.NW)
text_step_instruction = sm.LabelWidget(master, 'Explain your adjustment selection. '
                                               'Reference the SPECIFIC part of the body.', 3, 1, default_font,
                                       text_font_size, tk.NW)
answer_box = sm.EntryWidget(master, answer, 3, 1, entry_width, tk.EW)
instrc_items = [selection_step_instruction, text_step_instruction]

a_arm_title = sm.LabelWidget(master, 'A. ARM & WRIST ANALYSIS', 0, 0, default_font, title_font_size, tk.NW)
a1_step_images = [sm.ImageWidget(master, './step1a-rula -images/rula-step1a-1.png', 'C', 0, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-2.png', 'B', 0, 1, tk.RIGHT, tk.E),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-3.png', 'A', 0, 1, tk.RIGHT, tk.W),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-4.png', 'D', 1, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-5.png', 'E', 1, 1, tk.RIGHT, tk.E)]
a1_step_options = [sm.ComboBoxWidget(master, option_type,
                                     ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                                      'Arm supported? (i.e. person leaning?) (-1)'], 2, 1, 40, tk.SW),
                   sm.ComboBoxWidget(master, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
a1_title = sm.LabelWidget(master, 'Step 1: Locate upper arm position.', 0, 0, default_font, default_font_size, tk.W)
screen1 = sm.ScreenManager(master, a_arm_title, a1_title, a1_step_images,
                           a1_step_options, instrc_items, answer_box, my_image)
screen1.display_page()
attach_buttons()

master.mainloop()
