from tkinter import *

class DataStorage:
    def __init__(self):
        self.data = []

    def input(self, firstname, age, mobile):
        new_data = {"name": firstname, "age": age, "mobile": mobile}
        self.data.append(new_data)
        print(len(self.data))

    def view(self):
        return self.data

userData = DataStorage()

class CollectGui:
    def __init__(self, parent):
        self.parent = parent

        # Creates a frames
        f1 = Frame(parent)

        self.userData = userData

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
        self.firstname = Entry(f1)
        self.age = Entry(f1)

        # Arrange entry
        self.firstname.grid(row=2, column=1, sticky=W, pady=10, padx=20)
        self.age.grid(row=3, column=1, sticky=W, pady=10, padx=20)

        # Create buttons
        self.show_button = Button(f1, text="Show All", command=self.show_data)
        self.enter_button = Button(f1, text="Enter Data", command=self.enter_data)

        # Arrange buttons
        self.show_button.grid(row=1, column=1, pady=30)
        self.enter_button.grid(row=6, pady=30, padx=60)

        # Create radio buttons
        self.var = StringVar()
        self.yes = Radiobutton(f1, text="Yes", variable=self.var, value="Yes")
        self.no = Radiobutton(f1, text="No", variable=self.var, value="No")

        # Places radio buttons
        self.yes.grid(row=4, column=1, pady=10)
        self.no.grid(row=5, column=1, pady=10)

        f1.pack()

        # Input Data
    def enter_data(self):
        self.userData.input(self.firstname.get(), self.age.get(), self.var.get())
        print(self.userData.view())

    def show_data(self):
        self.nf = Toplevel(self.parent)
        self.app = DisplayGui(self.nf)

class DisplayGui:
    def __init__(self, parent):
        # Creates a frames
        f1 = Frame(parent)

        self.point = 0

        self.UD = userData.view()

        # Creates label widgets
        self.display = Label(f1, text="Displaying Person Data")
        self.firstname = Label(f1, text="First Name:   ")
        self.age = Label(f1, text="Age:  ")
        self.mobile = Label(f1, text="Mobile Phone:    ")

        # Arrange placement
        self.display.grid(row=1, column=0, sticky=W, pady=30)
        self.firstname.grid(row=2, column=0, sticky=W, pady=10)
        self.age.grid(row=3, column=0, sticky=W, pady=10)
        self.mobile.grid(row=4, column=0, sticky=W, pady=10)

        # Create buttons
        self.add_button = Button(f1, text="Add New Person")
        self.next = Button(f1, text="Previous", command=self.next)
        self.prev = Button(f1, text="Next", command=self.prev)

        # Arrange buttons
        self.add_button.grid(row=1, column=1, pady=30)
        self.next.grid(row=6, column=1, pady=30, sticky=W)
        self.prev.grid(row=6, pady=30, sticky=E)

        # Results
        self.name_r = Label(f1, text="")
        self.age_r = Label(f1, text="")
        self.mobile_phone_r = Label(f1, text="")

        # Places the results
        self.name_r.grid(row=2, column=1)
        self.age_r.grid(row=3, column=1)
        self.mobile_phone_r.grid(row=4, column=1)

        self.name_r.configure(text=self.UD[0]["name"])
        self.age_r.configure(text=self.UD[0]["age"])
        self.mobile_phone_r.configure(text=self.UD[0]["mobile"])

        f1.pack()

    def next(self):
        self.point += 1
        self.name_r.configure(text=self.UD[self.point]["name"])
        self.age_r.configure(text=self.UD[self.point]["age"])
        self.mobile_phone_r.configure(text=self.UD[self.point]["mobile"])

    def prev(self):
        self.point -= 1
        self.name_r.configure(text=self.UD[self.point]["name"])
        self.age_r.configure(text=self.UD[self.point]["age"])
        self.mobile_phone_r.configure(text=self.UD[self.point]["mobile"])


if __name__ == "__main__":
    root = Tk()
    buttons = CollectGui(root)
    root.mainloop()

