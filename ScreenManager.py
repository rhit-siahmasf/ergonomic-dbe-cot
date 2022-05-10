import conversion
import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# images = list of ImageWidget objects


class ScreenManager:
    default_font = 'Arial'
    text_font_size = 14
    default_font_size = 16
    title_font_size = 18
    entry_width = 30
    num_lines = 3
    default_height = 750
    default_width = 1100

    def __init__(self, title, sub_title, imgs, image_selects, adjustments):
        self.title = title
        self.sub_title = sub_title
        self.images = imgs
        self.image_selects = image_selects
        self.adjustment_checks = adjustments

        self.entry_box = None
        self.master = None

    def create_page(self, master, is_regular_page):
        self.master = ttk.Frame(master, width=ScreenManager.default_width, height=ScreenManager.default_height)

        # row / column configurations
        self.master.columnconfigure(0, weight=4)
        self.master.columnconfigure(1, weight=2)
        self.master.rowconfigure(0, weight=2)
        self.master.rowconfigure(1, weight=2)
        self.master.rowconfigure(2, weight=2)
        self.master.rowconfigure(3, weight=2)
        self.master.rowconfigure(4, weight=2)

        # screen manager items
        if bool(self.title):
            tk.Label(self.master, text=self.title,
                     font=(ScreenManager.default_font, ScreenManager.title_font_size)) \
                .grid(row=0, column=0, sticky=tk.NSEW)

        if bool(self.sub_title) and type(self.sub_title) == list:
            row = 0
            for sub in self.sub_title:
                tk.Label(self.master, text=sub, font=(ScreenManager.default_font, ScreenManager.default_font_size)) \
                    .grid(row=row, column=0, sticky=tk.S, padx=25)
                row += 1

        elif bool(self.sub_title):
            tk.Label(self.master, text=self.sub_title,
                     font=(ScreenManager.default_font, ScreenManager.default_font_size)) \
                .grid(row=0, column=0, sticky=tk.S)

        if is_regular_page:
            self.regular_page()
        elif self.adjustment_checks is not None:
            self.special_page()

        return self.master

    def regular_page(self):
        ttk.Label(self.master, text='Explain your adjustment selection. Reference the SPECIFIC part of the body.',
                  font=(ScreenManager.default_font, ScreenManager.text_font_size)).grid(row=3, column=1,
                                                                                        sticky=tk.NW)
        ttk.Label(self.master, text='Select the necessary adjustment.',
                  font=(ScreenManager.default_font, ScreenManager.text_font_size)).grid(row=2, column=1,
                                                                                        sticky=tk.NW)

        self.entry_box = tk.Text(self.master, width=ScreenManager.entry_width, height=ScreenManager.num_lines)
        self.entry_box.grid(row=3, column=1, sticky=tk.W)

        if bool(self.adjustment_checks) and bool(self.sub_title):
            temp = self.adjustment_checks
            self.adjustment_checks = ttk.Combobox(self.master, width=40, values=temp, state="readonly")
            self.adjustment_checks.grid(row=2, column=1, sticky=tk.SW)

        # images
        if bool(self.images) and bool(self.image_selects):
            fileDir = os.path.dirname(os.path.realpath(__file__))
            count = 0
            for img_wid in self.images:
                absolute = os.path.join(fileDir, img_wid)
                pic = Image.open(absolute)
                pic = pic.resize((270, 120), Image.ANTIALIAS)
                pic = ImageTk.PhotoImage(pic)
                panel = tk.Label(self.master, image=pic)
                panel.image = pic
                if count == 0:
                    panel.grid(row=0, column=1, sticky=tk.W, ipadx=75)
                else:
                    panel.grid(row=0, column=1, sticky=tk.E)
                count += 1

        if bool(self.image_selects):
            temp = self.image_selects
            self.image_selects = ttk.Combobox(self.master, width=40, values=temp, state="readonly")
            self.image_selects.grid(row=2, column=1, sticky=tk.W)

    def special_page(self):
        if bool(self.adjustment_checks):
            temp = self.adjustment_checks
            self.adjustment_checks = ttk.Combobox(self.master, width=80, values=temp, state="readonly")

        if bool(self.image_selects):
            temp = self.image_selects
            self.image_selects = ttk.Combobox(self.master, width=40, values=temp, state="readonly")
            self.image_selects.grid(row=1, column=0, sticky=tk.N)

        if not bool(self.sub_title) and bool(self.adjustment_checks):
            self.adjustment_checks.grid(row=1, column=0, sticky=tk.N)
        elif bool(self.sub_title):
            self.adjustment_checks.grid(row=2, column=0, sticky=tk.N, pady=20)

    def get_tab_master(self):
        return self.master

    def get_user_entry(self):
        if self.entry_box is not None:
            return self.entry_box.get('1.0', 'end')
        else:
            return ""

    def get_adjustment_checks(self):
        if self.adjustment_checks is not None:
            return self.adjustment_checks.get()
        else:
            return ""

    def get_image_selection(self):
        if self.image_selects is not None:
            return self.image_selects.get()
        else:
            return ""

    def get_subtitle(self):
        if self.sub_title is not None and type(self.sub_title) is not list:
            return self.sub_title
        else:
            return ""

