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
    import StepA7Screen


def prev_page():
    master.destroy()
    import StepA3Screen


tk.Label(master, text='Select the necessary adjustment.',
         font=(default_font, text_font_size)).grid(row=2, column=1, sticky=tk.NW)
tk.Label(master, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
         font=(default_font, text_font_size)).grid(row=3, column=1, sticky=tk.NW)
tk.Entry(master, width=entry_width, textvariable=answer).grid(row=3, column=1, sticky=tk.EW)
tk.Label(master, text='A. ARM & WRIST ANALYSIS',
         font=(default_font, title_font_size)).grid(row=0, column=0, sticky=tk.NW)
tk.Label(master, text='Step 4: Wrist twist.',
         font=(default_font, default_font_size)).grid(row=0, column=0, sticky=tk.W)
a4_step_option = sm.ComboBoxWidget(master, option_type,
                                   ['If wrist is twisted in mid-range: (+1)',
                                    'If wrist is at or near end of range: (+2)'], 2, 1, 40, tk.SW)
a4_step_option.button.grid(row=a4_step_option.row, column=a4_step_option.column, sticky=a4_step_option.stick)
tk.Label(master, text='Step 5: Score from table A',
         font=(default_font, default_font_size)).grid(row=1, column=0, sticky=tk.W)
a6_step_options = sm.ComboBoxWidget(master, option_type,
                                    ['Action repeated occurs 4x/minute?'
                                     ' OR is posture mainly static (i.e held >10 minutes)? (+1)'],
                                    2, 1, 40, tk.W)
a6_step_options.button.grid(row=a6_step_options.row, column=a6_step_options.column, sticky=a6_step_options.stick)
tk.Label(master, text='Step 6: Muscle Use', font=(default_font, default_font_size)).grid(row=2, column=0, sticky=tk.W)
tk.Button(master, text='NEXT', bg='#458B00', command=next_page).grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
tk.Button(master, text='BACK', bg='#8B2323', command=prev_page).grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

master.mainloop()
