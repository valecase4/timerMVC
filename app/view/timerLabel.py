from tkinter import *

class TimerLabel(Label):
    """
    Label representing time flow
    """

    def __init__(self, master, controller) -> None:
        super().__init__(master)

        self.master = master
        self.controller = controller
        self.after_id = None

        self.configure(
            text="01:00",
            bg="#ffffff",
            font=("Arial", 56, "bold")
        )

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["pady"] = 20

        super().pack(*args, **kwargs)

    def default_settings(self) -> None:
        """
        Restart timer label
        """
        
        self.after_cancel(self.after_id)
        self.configure(text="01:00")

