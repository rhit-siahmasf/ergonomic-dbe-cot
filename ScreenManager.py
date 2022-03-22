import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import PIL
from PIL import ImageTk, Image


# images = list of ImageWidget objects
class ScreenManager:
    def __init__(self, master, title, sub_title, imgs, selects, descriptions, entries, prev, nxt):
        self.master = master
        self.title = title
        self.sub_title = sub_title
      #  self.images = imgs
        self.adjustment_checks = selects
        self.instr_items = descriptions
        self.entry = entries
        self.prev_screen_manager = prev
        self.next_screen_manager = nxt

    def clear_screen(self):
        for w in self.master.winfo_children():
            w.grid_remove()

    def go_back_prev_page(self):
        self.clear_screen()
        self.prev_screen_manager.display_page()

    def continue_next_page(self):
        self.clear_screen()
        self.next_screen_manager.display_page()

    def display_page(self, should_clear):
        if should_clear:
            self.clear_screen()

        self.title.label.grid(row=self.title.row, column=self.title.column, sticky=self.title.stick)
        self.sub_title.label.grid(row=self.sub_title.row, column=self.sub_title.column, sticky=self.sub_title.stick)
        self.entry.wid.grid(row=self.entry.row, column=self.entry.column, sticky=self.entry.stick)

        #for img in self.images:
         #   img.image.grid(row=img.row, column=img.column)

        for adj in self.adjustment_checks:
            adj.button.grid(row=adj.row, column=adj.column, sticky=adj.stick)

        for d in self.instr_items:
            d.label.grid(row=d.row, column=d.column, sticky=d.stick)




class ComboBoxWidget:
    def __init__(self, master, var_type, texts, row, column, stik):
        self.master = master
        self.var_type = var_type
        self.values = texts
        self.row = row
        self.column = column
        self.stick = stik
        btn = self.create_check_button()
        self.button = btn

    def create_check_button(self):
        return ttk.Combobox(self.master, values=self.values)
        #return tk.Checkbutton(self.master, text=self.text, variable=self.var_type)

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
    def __init__(self, master, img, var_type, row, column, stik):
        self.master = master
        self.var_type = var_type
        self.row = row
        self.column = column
        self.stick = stik
        crt = img
        self.image = crt

    def create_image(self, img):
        pic = Image.open(img)
        pic = pic.resize((50, 50), Image.ANTIALIAS)
        final_pic = ImageTk.PhotoImage(pic)
        final_pic.image = pic
        return tk.Checkbutton(self.master, image=final_pic, variable=self.var_type)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class EntryWidget:
    def __init__(self, master, var_type, row, column, stik):
        self.master = master
        self.var_type = var_type
        self.row = row
        self.column = column
        self.stick = stik
        entry = self.create_entry()
        self.wid = entry

    def create_entry(self):
        return tk.Entry(self.master, textvariable=self.var_type)

