import tkinter as tk
from tkinter import filedialog
import os
import PIL
from PIL import ImageTk, Image


# images = list of ImageWidget objects
class ScreenManager:
    def __init__(self, master, title, sub_title, images, selects, others):
        self.master = master
        self.title = title
        self.sub_title = sub_title
        self.images = images
        self.adjustment_checks = selects
        self.other_items = others

    def attach_to_main(self, should_clear):
        if should_clear:
            for w in self.master.winfo_children():
                w.grid_remove()

        self.title.grid(row=self.title.row, column=self.title.column)
        self.sub_title.grid(row=self.sub_title.row, column=self.sub_title.column)

        for img in self.images:
            img.grid(row=self.img.row, column=self.img.column)

        for adj in self.adjustment_checks:
            adj.grid(row=self.adj.row, column=self.adj.column)

        for ot in self.other_items:
            ot.grid()


class CheckButtonWidget:
    def __init__(self, master, var_type, text, row, column):
        self.master = master
        self.var_type = var_type
        self.text = text
        self.row = row
        self.column = column

    def create_check_button(self):
        return tk.Checkbutton(self.master, text=self.text, variable=self.var_type)


class TitleWidget:
    def __init__(self, master, title, row, column, font, f_size):
        self.master = master
        self.title = title
        self.row = row
        self.column = column
        self.font = font
        self.f_size = f_size

    def create_title(self):
        return tk.Label(self.master, text=self.title, font=(self.font, self.f_size))


class ImageWidget:
    def __init__(self, master, img, var_type, row, column):
        self.master = master
        self.image = self.create_image(img)
        self.var_type = var_type
        self.row = row
        self.column = column

    def create_image(self, img):
        pic = Image.open(img)
        print(pic)
        pic = pic.resize((50, 50), Image.ANTIALIAS)
        final_pic = ImageTk.PhotoImage(pic)
        final_pic.image = pic
        return tk.Checkbutton(self.master, image=pic, variable=self.var_type)

