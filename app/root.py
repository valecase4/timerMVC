from tkinter import *
from .view.button import MyButton
from .view.label import MyLabel

class Root(Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.WIDTH = 800
        self.HEIGHT = 400

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title("Timer")
        self.resizable(False, False)

        button = MyButton(self, self.controller)
        button.pack()

