import os
import tkinter as tk
from tkinter import ttk
# import StepA1Screen as a1
# # import StepA2Screen as a2
# # import StepA3Screen as a3
# # import StepA456Screen as a456
# # import StepA7Screen as a7
from PIL import ImageTk, Image

fileDir = os.path.dirname(os.path.realpath(__file__))


# images = list of ImageWidget objects
class ScreenManager:
    def __init__(self, master, sub_title, image_selects, adjustments, text_box):
        self.master = master
        self.sub_title = sub_title
        self.images = image_selects
        self.adjustment_checks = adjustments
        self.user_entry = text_box

    def get_tab_master(self):
        return self.master

    def get_user_entry(self):
        return self.user_entry.get()

    def get_adjustment_checks(self):
        return self.adjustment_checks.current(0)

    def get_image_selection(self):
        return self.images.current(0)


class ComboBoxWidget:
    def __init__(self, master, var_type, texts, row, column, w, stik):
        self.master = master
        self.var_type = var_type
        self.values = texts
        self.row = row
        self.column = column
        self.stick = stik
        self.wdth = w
        btn = self.create_check_button()
        self.button = btn

    def create_check_button(self):
        return ttk.Combobox(self.master, width=self.wdth, values=self.values, state="readonly")

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class LabelWidget:
    def __init__(self, master, title, row, column, font, f_size, stik):
        self.master = master
        self.font = font
        self.f_size = f_size
        self.stick = stik
        self.row = row
        self.column = column
        me = self.create_label(title)
        self.label = me

    def create_label(self, title):
        return tk.Label(self.master, text=title, font=(self.font, self.f_size))

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class ImageWidget:
    def __init__(self, master, img, label, row, column, comp, stik):
        self.label = None
        self.image = None
        self.master = master
        self.row = row
        self.column = column
        self.stick = stik
        self.compwd = comp
        self.txt = label
        self.path = img

    def create_image(self):
        pic = Image.open(os.path.join(fileDir, self.path))
        pic = pic.resize((150, 150), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(pic)
        self.label = tk.Label(self.master, text=self.txt, image=self.image, compound=self.compwd)

    def recreate_image(self):
        pic = Image.open(self.path)
        pic = pic.resize((200, 200), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(pic)
        self.label = tk.Label(self.master, image=self.image)


class EntryWidget:
    def __init__(self, master, var_type, row, column, w, stik):
        self.master = master
        self.var_type = var_type
        self.row = row
        self.column = column
        self.stick = stik
        self.wdth = w
        entry = self.create_entry()
        self.wid = entry

    def create_entry(self):
        return tk.Entry(self.master, width=self.wdth, textvariable=self.var_type)
