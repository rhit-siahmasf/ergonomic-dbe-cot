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
option = tk.IntVar()
answer = tk.StringVar()
default_font = 'Arial'
text_font_size = 12
default_font_size = 18
title_font_size = 22
entry_width = 30
my_image = None


def next_page():
    master.destroy()
    import ImageSelectorScreen


def prev_page():
    master.destroy()
    import HomeScreen


assessment_option = sm.ComboBoxWidget(master, option_type, ['RULA', 'REBA', 'Open Existing...'], 1, 0, 40, tk.N)
assessment_option.button.grid(row=assessment_option.row,
                              column=assessment_option.column, sticky=assessment_option.stick)
tk.Label(master, text='Select an option to continue.',
         font=('Arial', default_font_size)).grid(row=0, column=0, sticky=tk.NSEW)
tk.Button(master, text='NEXT', bg='#458B00', command=next_page).grid(row=4, column=1, sticky=tk.E, padx=15, ipadx=15)
tk.Button(master, text='BACK', bg='#8B2323', command=prev_page).grid(row=4, column=0, sticky=tk.W, padx=15, ipadx=15)

master.title('RULA / REBA Assessment')
master.mainloop()

