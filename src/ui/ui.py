from tkinter import Button, Label, Entry, Frame, Menu, Toplevel
from ordermaker.ordermaker import OrderMaker
from recipereader.recipereader import RecipeReader
from logic.logic import Logic


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master  # tk window = master widget
        self.init_window()

    def init_window(self):
        self.master.title("Transform recipes to order")
        # widget to take the full space of the root window
        self.pack(fill='both', expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Show Text", command=self.showStartText)

    def showStartText(self):
        text = Label(
            self, text="This recipe reader already 'knows' valid recipes.")
        text.pack()
        eaters_label = Label(self, text="Give amount of eaters below:")
        eaters_entry = Entry(self)
        eaters_label.pack()
        eaters_entry.pack()
        generate_btn = Button(self, text="Generate order",
                              command=lambda: self.showEntry(eaters_entry.get()))
        generate_btn.pack()

    def showEntry(self, entry):
        try:
            eaters = int(entry)
        except ValueError:
            e_text = "Invalid input. Please input an integer."
            self.create_error_window(e_text)
        e_label = Label(self, text=f'Attempting to generate order for {entry}')
        e_label.pack()
        logic = Logic(eaters)
        ret_str = logic.generate_order_based_on_recipes()
        done_label = Label(
            self, text=f"Successfully generated order files for {entry}")
        done_label.pack()
        end_label = Label(self, text=ret_str)
        end_label.pack()

    def create_error_window(self, e_text):
        newWindow = Toplevel(self)
        e_label = Label(newWindow, text=e_text)
        e_label.pack()

    def client_exit(self):
        exit()
