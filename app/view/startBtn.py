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
            bg="lightgreen",
            fg="#ffffff",
            highlightthickness=0,
            border=0,
            font=("Arial", 30, "bold"),
            cursor="hand2",
            activebackground="green",
            activeforeground="#ffffff",
            command=self.on_click
        )

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))

    def pack(self, *args, **kwargs) -> None:
        """
        Override pack method
        """

        kwargs["pady"] = 20

        super().pack(*args, **kwargs)

    def on_enter(self, event) -> None:
        """
        Background effect when cursor is on the button
        """
        
        self.configure(bg="green")

    def on_leave(self, event) -> None:
        """
        Background effect when cursor leaves the button
        """

        self.configure(bg="lightgreen")

    def on_click(self) -> None:
        """
        Handle click on start button
        """

        self.controller.start()

    def enable(self) -> None:
        """
        Set button enabled
        """

        self.configure(
            bg="lightgreen",
            fg="#ffffff",
            state="normal"
        )

        self.bind("<Enter>", lambda e : self.on_enter(e))
        self.bind("<Leave>", lambda e : self.on_leave(e))

    def disable(self) -> None:
        """
        Set button disabled
        """

        self.configure(
            background="lightgray",
            state="disabled"
        )

        self.unbind("<Enter>")
        self.unbind("<Leave>")
