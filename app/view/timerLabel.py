from tkinter import *

class Timer(Label):
    """
    Label displaying time flow
    """

    def __init__(self, parent, controller) -> None:
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.configure(
            text="00:00",
            background="#ffffff",
            foreground="#000000",
            font=(
                "Arial",
                70,
                "bold"
            )
        )

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["pady"] = 20

        super().pack(*args, **kwargs)