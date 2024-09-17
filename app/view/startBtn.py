from tkinter import *

class StartBtn(Button):
    """
    Start Button
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller

        self.configure(
            text="START",
            background="lightgreen",
            foreground="#ffffff",
            font=(
                "Arial",
                30,
                "bold"
            ),
            highlightthickness=0,
            cursor="hand2",
            activebackground="green",
            activeforeground="#ffffff",
            borderwidth=0
        )

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["pady"] = 20

        super().pack(*args, **kwargs)



