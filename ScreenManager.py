import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import PIL
from PIL import ImageTk, Image

fileDir = os.path.dirname(os.path.realpath(__file__))


# images = list of ImageWidget objects
class ScreenManager:
    def __init__(self, master, title, sub_title, imgs, selects, descriptions, entries, mine):
        self.master = master
        self.title = title
        self.sub_title = sub_title
        self.my_image = mine
        self.images = imgs
        self.adjustment_checks = selects
        self.instr_items = descriptions
        self.entry = entries

    def clear_screen(self):
        for w in self.master.winfo_children():
            w.grid_remove()

    def display_page(self):

        self.title.label.grid(row=self.title.row, column=self.title.column, sticky=self.title.stick)
        self.sub_title.label.grid(row=self.sub_title.row, column=self.sub_title.column, sticky=self.sub_title.stick)
        self.entry.wid.grid(row=self.entry.row, column=self.entry.column, sticky=self.entry.stick)

        for img in self.images:
            img.create_image()
            img.label.grid(row=img.row, column=img.column, sticky=img.stick)

        for adj in self.adjustment_checks:
            adj.button.grid(row=adj.row, column=adj.column, sticky=adj.stick, pady=20)

        for d in self.instr_items:
            d.label.grid(row=d.row, column=d.column, sticky=d.stick, pady=20)

        # self.my_image.recreate_image()
        # self.my_image.label.grid(row=self.my_image.row, column=self.my_image.column, sticky=self.my_image.stick)


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
        pic = pic.resize((100, 90), Image.ANTIALIAS)
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
