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


# def next_page():
#     master.destroy()
#     import StepB1Screen


def prev_page():
    master.destroy()
    import StepA456Screen


tk.Label(master, text='Select the necessary adjustment.',
         font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
tk.Label(master, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
         font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
tk.Entry(master, width=entry_width, textvariable=answer).grid(row=3, column=1, sticky=tk.EW)
tk.Label(master, text='A. ARM & WRIST ANALYSIS',
         font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
tk.Label(master, text='Step 7: Add Force / Load.',
         font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
a7_step_options = sm.ComboBoxWidget(master, option_type,
                                    ['If load < 4.4 lbs (intermittent): (+0)',
                                     'If load 4.4 to 22 lbs (intermittent): (+1)',
                                     'If load 4.4 to 22 lbs (static or repeated): (+2)',
                                     'If more than 22lbs OR repeated or shocks: (+3)'], 2, 1, 40, tk.SW)
a7_step_options.button.grid(row=a7_step_options.row, column=a7_step_options.column, sticky=a7_step_options.stick)
tk.Button(master, text='NEXT', bg='#458B00').grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
tk.Button(master, text='BACK', bg='#8B2323', command=prev_page).grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

master.mainloop()
