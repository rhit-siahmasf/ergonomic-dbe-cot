
class UtilManager:
    def __init__(self, master):
        self.master = master

    @staticmethod
    def attach_new_screen_to_main(self, widgets):
        for w in self.master.winfo_children():
            w.pack_forget()

        for w in widgets:
            w.pack()

    @staticmethod
    def attach_image_main(self, el):
        el.pack()
