from app.root import Root
from app.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    root = Root(controller)
    root.mainloop()