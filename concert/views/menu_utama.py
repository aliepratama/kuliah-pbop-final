import customtkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)
        self.segemented_button_var = customtkinter.StringVar(value="Value 1")
        self.segemented_button = customtkinter.CTkSegmentedButton(self, values=["Value 1", "Value 2", "Value 3"],
                                                            command=self.segmented_button_callback,
                                                            variable=self.segemented_button_var)
        self.segemented_button.grid(row=1, column=0, padx=20, pady=10)
        
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)

    # add methods to app
    def button_click(self):
        print("button click")
    
    def segmented_button_callback(self, value):
        print("segmented button clicked:", value)


app = App()