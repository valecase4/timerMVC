class Controller:
    """
    Link between model and view
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_label(self):
        """
        Display a label on the screen
        """

        label = self.model.create_label()
        