import tkinter as tk
from tkinter import filedialog
import os
import PIL
from PIL import ImageTk, Image


# images = list of ImageWidget objects
class ScreenManager:
    def __init__(self, master, title, sub_title, imgs, selects, others, prev, nxt):
        self.master = master
        self.title = title
        self.sub_title = sub_title
      #  self.images = imgs
        self.adjustment_checks = selects
        self.other_items = others
        self.prev_screen_manager = prev
        self.next_screen_manager = nxt

    def go_back_prev_page(self):
        for w in self.master.winfo_children:
            w.destroy()

        self.prev_screen_manager.display_page()

    def continue_next_page(self):
        for w in self.master.winfo_children:
            w.destroy()

        self.next_screen_manager.display_page()

    def display_page(self):
        self.title.title.grid(row=self.title.row, column=self.title.column, sticky=self.title.stick)
        self.sub_title.title.grid(row=self.sub_title.row, column=self.sub_title.column)

        #for img in self.images:
         #   img.image.grid(row=img.row, column=img.column)

        for adj in self.adjustment_checks:
            adj.button.grid(row=adj.row, column=adj.column)

        for ot in self.other_items:
            ot.grid()


class CheckButtonWidget:
    def __init__(self, master, var_type, text, row, column, stik):
        self.master = master
        self.var_type = var_type
        self.text = text
        self.row = row
        self.column = column
        self.stick = stik
        btn = self.create_check_button()
        self.button = btn

    def create_check_button(self):
        return tk.Checkbutton(self.master, text=self.text, variable=self.var_type)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class TitleWidget:
    def __init__(self, master, title, row, column, font, f_size, stik):
        self.master = master
        self.font = font
        self.f_size = f_size
        self.stick = stik
        self.row = row
        self.column = column
        me = self.create_title(title)
        self.title = me

    def create_title(self, title):
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
        crt = self.create_image(img)
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
