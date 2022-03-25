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


def set_image(img):
    global my_image
    my_image = img


def next_page():
    master.destroy()
    import StepA2Screen

# def prev_page():
#     ws.destroy()
#     import ImagePickerScreen


tk.Label(master, text='Explain your adjustment selection. '
                      'Reference the SPECIFIC part of the body.',
         font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
tk.Label(master, text='Select the necessary adjustment.',
         font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
tk.Entry(master, width=entry_width, textvariable=answer).grid(row=3, column=1, sticky=tk.EW)
tk.Label(master, text='A. ARM & WRIST ANALYSIS',
         font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
a1_step_images = [sm.ImageWidget(master, './step1a-rula -images/rula-step1a-1.png', 'B', 0, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-2.png', 'C', 0, 1, tk.RIGHT, tk.E),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-3.png', 'A', 0, 1, tk.RIGHT, tk.W),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-4.png', 'D', 1, 1, tk.RIGHT, tk.NSEW),
                  sm.ImageWidget(master, './step1a-rula -images/rula-step1a-5.png', 'E', 1, 1, tk.RIGHT, tk.E)]
for img_wig in a1_step_images:
    img_wig.create_image()
    img_wig.label.grid(row=img_wig.row, column=img_wig.column, sticky=img_wig.stick)
a1_step_options = [sm.ComboBoxWidget(master, option_type,
                                     ['Shoulder raised? (+1)', 'Upper arm abducted? (+1)',
                                      'Arm supported? (i.e. person leaning?) (-1)'], 2, 1, 40, tk.SW),
                   sm.ComboBoxWidget(master, option_type, ['A', 'B', 'C', 'D', 'E'], 2, 1, 40, tk.W)]
for combo in a1_step_options:
    combo.button.grid(row=combo.row, column=combo.column, sticky=combo.stick)
tk.Label(master, text='Step 1: Locate upper arm position.',
         font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
tk.Button(master, text='NEXT', bg='#458B00', command=next_page).grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
tk.Button(master, text='BACK', bg='#8B2323').grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

master.mainloop()
