class Model:
    """
    Backend of timer
    """

    def __init__(self) -> None:
        self.seconds = 60
        self.is_running = False

    def start(self) -> None:
        """
        Set the timer running
        """

        self.is_running = True

    def countdown(self) -> None:
        """
        Decrease timer by 1 second
        """
        if self.is_running:
            if self.seconds > 0:
                self.seconds -= 1

                return self.seconds
            else:
                self.reset()
                print("timer finished") # test

    def reset(self) -> None:
        """
        Reset timer: self.seconds = 60, self.is_running = False
        """

        self.seconds = 60
        self.is_running = False

    def converter(self, seconds) -> str:
        """
        Convert seconds to MM:SS format string
        """

        if seconds:
            if seconds < 60:
                time_value = f"00:{seconds}" if len(str(seconds)) == 2 else f"00:0{seconds}"
            else:
                time_value = "01:00"

            return time_value