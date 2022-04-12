from tkinter import *

class CollectGui:
    def __init__(self, parent):

        # Creates a frames
        f1 = Frame(parent)

        # Creates label widgets
        self.l1 = Label(f1, text="Collecting Person Data")
        self.l2 = Label(f1, text="First Name:   ")
        self.l3 = Label(f1, text="Age:  ")
        self.l4 = Label(f1, text="Do you have a mobile phone?   ")

        # Arrange placement
        self.l1.grid(row=1, column=0, sticky=W, pady=30)
        self.l2.grid(row=2, column=0, sticky=W, pady=10)
        self.l3.grid(row=3, column=0, sticky=W, pady=10)
        self.l4.grid(row=4, column=0, sticky=W, pady=25)

        # Creates entry widgets
        self.e1 = Entry(f1)
        self.e2 = Entry(f1)

        # Arrange entry
        self.e1.grid(row=2, column=1, sticky=W, pady=10, padx=20)
        self.e2.grid(row=3, column=1, sticky=W, pady=10, padx=20)

        # Create buttons
        self.show_button = Button(f1, text="Show All")
        self.enter_button = Button(f1, text="Enter Data")

        # Arrange buttons
        self.show_button.grid(row=1, column=1, pady=30)
        self.enter_button.grid(row=6, pady=30, padx=60)

        # Create radio buttons

        self.var = StringVar()
        self.yes = Radiobutton(f1, text="Yes", variable=self.var, value="Yes").grid(row=4, column=1, pady=10)
        self.no = Radiobutton(f1, text="No", variable=self.var, value="No").grid(row=5, column=1, pady=10)

        f1.pack()

class DisplayGui:
    def __init__(self, parent):

        # Creates a frames
        f1 = Frame(parent)

        # Creates label widgets
        self.display = Label(f1, text="Displaying Person Data")
        self.firstname = Label(f1, text="First Name:   ")
        self.lastname = Label(f1, text="Age:  ")

        # Arrange placement
        self.display.grid(f1, row=1, column=0, sticky=W, pady=30)
        self.firstname.grid(f1, row=2, column=0, sticky=W, pady=10)
        self.lastname.grid(f1, row=3, column=0, sticky=W, pady=10)

        # Create buttons
        self.add_button = Button(f1, text="Add New Person")
        self.next = Button(f1, text="Previous")
        self.prev = Button(f1, text="Next")

        # Arrange buttons
        self.add_button.grid(f1, row=1, column=1, pady=30)
        self.next.grid(f1, row=6, column=1, pady=30, sticky=W)
        self.prev.grid(f1, row=6, pady=30, sticky=E)

        f1.pack()


if __name__ == "__main__":
    root = Tk()
    buttons = CollectGui(root)
    root.mainloop()
