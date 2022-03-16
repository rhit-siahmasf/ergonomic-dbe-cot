import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image


class ScreenManager:
    def __init__(self, master, title, sub_title, should_clear, image, button_commands, options, item_list):
        self.master = master
        self.screen_items = item_list
        self.title = title
        self.sub_title = self.create_title(sub_title)
        self.images = self.create_image_checks(image)
        self.continue_button = self.create_continue_button(button_commands, should_clear)
        self.selectable_options = self.create_description_checks(options)

    def create_title(self, title):
        label_title = tk.Label(self.master, text=title, font=('Arial', 14))
        self.screen_items.append(label_title)
        return label_title

    def create_continue_button(self, btn_params, should_clear):
        cont_btn = tk.Button(self.master, text='Continue',
                             command=lambda: self.attach_new_screen_to_main(btn_params, should_clear))
        self.screen_items.append(cont_btn)
        return cont_btn

    def create_image_checks(self, choices):
        img_type = tk.IntVar()
        images = []
        for img in choices:
            pic = Image.open(img)
            pic = pic.resize((50, 50), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(pic)
            final_pic = tk.Checkbutton(self.master, image=pic, variable=img_type)
            final_pic.image = pic
            self.screen_items.append(final_pic)
            images.append(final_pic)
        return images

    def create_description_checks(self, options):
        desc_vars = []
        desc_type = tk.StringVar()
        for txt in options:
            chk_button = tk.Checkbutton(self.master, text=txt, variable=desc_type)
            desc_vars.append(chk_button)
            self.screen_items.append(chk_button)
        return desc_vars

    def attach_new_screen_to_main(self, widgets, should_clear):
        print(should_clear)
        if should_clear:
            for w in self.master.winfo_children():
                w.pack_forget()

        for w in widgets:
            w.pack()

    def create_layout(self, layout):
        for row in layout:
            print(row)
