import customtkinter


class AlertWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.geometry("300x100")
        self.resizable(0, 0)

        label1 = customtkinter.CTkLabel(self, text=kwargs.get('title'), font=('Plus Jakarta Sans', 24, "bold"), text_color="red")
        label1.pack(pady=5)
        label2 = customtkinter.CTkLabel(self, text=kwargs.get('subtitle'), font=('Plus Jakarta Sans', 18))
        label2.pack(pady=5)