import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image


class ScreenManager:
    def __init__(self, master, title, sub_title, image, button_commands, options):
        self.master = master
        self.title = title
        self.sub_title = self.create_title(sub_title)
        self.images = self.create_image_checks(image)
        self.continue_button = self.create_continue_button(button_commands)
        self.selectable_options = self.create_description_checks(options)

    def create_title(self, title):
        return tk.Label(self.master, text=title, font=('Arial', 14))

    def create_continue_button(self, button_commands):
        return tk.Button(self.master, text='Continue',
                         command=lambda: button_commands)

    def create_image_checks(self, choices):
        img_type = tk.IntVar()
        images = []
        for img in choices:
            pic = Image.open(img)
            pic = pic.resize((50, 50), Image.ANTIALIAS)
            final_pic = ImageTk.PhotoImage(self.master, image=pic, variable=img_type)
            final_pic.image = pic
            images.append(final_pic)
        return final_pic

    def create_description_checks(self, options):
        desc_vars = []
        desc_type = tk.StringVar()
        for txt in options:
            chk_button = tk.Checkbutton(self.master, text=txt, variable=desc_type)
            desc_vars.append(chk_button)
        return desc_vars
