from tkinter import Tk
from ui.ui import Window


def main():
    root = Tk()
    root.geometry("400x300")
    app = Window(root)
    app.showStartText()
    root.mainloop()


if __name__ == '__main__':
    main()
