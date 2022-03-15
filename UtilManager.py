
class UtilManager:
    def __init__(self, master):
        self.master = master

    def clear_screen(self):
        for w in self.master.winfo_children():
            w.pack_forget()

    @staticmethod
    def attach_to_main(widgets, name):
        for w in widgets:
            w.pack()
        print('On screen ', name)

    @staticmethod
    def attach_image_main(self, el):
        el.pack()
