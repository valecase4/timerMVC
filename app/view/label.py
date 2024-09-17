from tkinter import *

class MyLabel(Label):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.configure(
            text="Button clicked!",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 30)
        )