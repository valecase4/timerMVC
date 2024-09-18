class Controller:
    """
    Link between model and view
    """

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def start(self) -> None:
        self.model.start()
        self.disable_start_btn()
        self.update_timer()

    def update_timer(self) -> None:
        self.view.timer.after_id = self.view.timer.after(1000, self.update_timer)

        time_value = self.converter()
        self.view.timer.configure(text=time_value)

    def countdown(self) -> int:
        time_left = self.model.countdown()

        if time_left == 0:
            self.end_timer()
        else:
            return time_left
    
    def converter(self) -> str:
        time_left = self.countdown()
        time_value = self.model.converter(time_left)

        return time_value

    def disable_start_btn(self) -> None:
        self.view.start_btn.disable()

    def end_timer(self) -> None:
        self.view.start_btn.enable()
        self.view.timer.default_settings()
        self.model.reset()



