from tkinter import *
from .startBtn import StartBtn
from .timerLabel import Timer

class View(Frame):
    """
    Main Frame of the application
    """

    def __init__(self, parent, controller) -> None:
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.configure(
            width=800,
            height=400,
            background="#ffffff"
        )

        self.start_btn = StartBtn(self, controller=self.controller)
        self.start_btn.pack()

        self.timer = Timer(self, controller=self.controller)
        self.timer.pack()

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["expand"] = True
        kwargs["fill"] = BOTH

        super().pack(*args, **kwargs)
