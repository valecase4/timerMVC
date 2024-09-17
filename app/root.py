from tkinter import *
from .view.view import View

class App(Tk):
    """
    Root of the application
    """

    def __init__(self) -> None:
        super().__init__()

        self.view = View(self, None)
        self.view.pack()

        self.WIDTH = 800
        self.HEIGHT = 400

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title("Timer")
        self.resizable(False, False)