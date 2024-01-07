import customtkinter, os
from PIL import Image


class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=120, padx=120, fill="both")
        
        label1 = customtkinter.CTkLabel(self.__container, text="Selamat Datang", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="di Aplikasi Pemesanan Tiket Konser", font=('Plus Jakarta Sans', 24))
        label2.pack(pady=10)
        
        frame = customtkinter.CTkFrame(self.__container, fg_color="transparent")
        frame.pack(pady=80)
        
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/arrow-right-to-bracket-solid-svg.png')), 
            size=(20, 20))
        button1 = customtkinter.CTkButton(frame, text="Masuk aplikasi",
                            fg_color="#015395",
                            hover_color="#013865",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#FFFFFF",
                            command=lambda: controller.show_frame("LoginPage"))
        
        button_image2 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/user-plus-solid-svg.png')), 
            size=(25, 20))
        button2 = customtkinter.CTkButton(frame, text="Buat akun baru",
                            fg_color="#FFD60A",
                            hover_color="#e6bf00",
                            text_color="#000000",
                            image=button_image2,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=lambda: controller.show_frame("RegisterPage"))
        button1.pack(ipady=6, ipadx=6)
        button2.pack(ipady=6, ipadx=6, pady=10)
