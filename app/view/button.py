from tkinter import *

class MyButton(Button):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.configure(
            text="CLICK ME",
            font=("Arial", 40),
            bg="#ffffff",
            command=lambda: self.controller.display_label()
        )