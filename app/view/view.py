from tkinter import *
from .startBtn import StartBtn
from .timerLabel import TimerLabel

class View(Frame):
    """
    Main frame
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            bg="#ffffff",
            width=800,
            height=400
        )

        self.start_btn = StartBtn(self, self.controller)
        self.start_btn.pack()

        self.timer = TimerLabel(self, self.controller)
        self.timer.pack()