from tkinter import *
from .model.model import Model
from .view.view import View
from .controller.controller import Controller

class App(Tk):
    """
    Root of the application
    """

    def __init__(self) -> None:
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 400

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title("Timer")
        self.resizable(False, False)

        self.model = Model()
        self.controller = Controller(self.model, None)
        
        self.view = View(self, self.controller)
        self.view.pack(expand=True, fill="both")

        self.controller.view = self.view




