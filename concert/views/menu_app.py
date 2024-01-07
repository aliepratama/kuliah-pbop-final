import customtkinter, os
from PIL import Image


from concert.helpers.session import Session


class AppPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        self.button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/magnifying-glass-solid-svg.png')), 
            size=(48, 48))
        self.button_image2 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/circle-up-solid-svg.png')), 
            size=(48, 48))
        self.button_image3 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/clipboard-list-solid-svg.png')), 
            size=(36, 48))
        self.button_image4 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/right-from-bracket-solid-svg.png')), 
            size=(48, 48))
        self.icon_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/wallet-solid-svg.png')), 
            size=(16, 16))
        
    def update_view(self):
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=60, padx=60, fill="both")
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color="transparent")
        frame1.grid(row=0, column=0, sticky='w', pady=20, padx=20)
        label1 = customtkinter.CTkLabel(frame1, text=f"Hai {Session.USER_DATA.get('nama')}", font=('Plus Jakarta Sans', 24, 'bold'))
        label1.pack(anchor='w')
        label2 = customtkinter.CTkLabel(frame1, text="Ayo nonton konser!", font=('Plus Jakarta Sans', 16))
        label2.pack(anchor='w')
        
        frame2 = customtkinter.CTkFrame(self.__container, fg_color='transparent')
        frame2.grid(row=1, column=0, padx=20)
        
        frame2a = customtkinter.CTkFrame(frame2, fg_color='transparent')
        frame2a.grid(row=0, column=0, padx=10, pady=10)
        
        button1 = customtkinter.CTkButton(frame2a, text="",
                            width=120, height=120,
                            corner_radius=20,
                            fg_color="#FFD60A",
                            hover_color="#e6bf00",
                            text_color="#000000",
                            image=self.button_image1,
                            command=lambda: self.controller.show_frame("ConcertPage"))
        button1.pack()
        label3 = customtkinter.CTkLabel(frame2a, text="Lihat tiket konser", font=('Plus Jakarta Sans', 12))
        label3.pack()
        
        frame2b = customtkinter.CTkFrame(frame2, fg_color='transparent')
        frame2b.grid(row=0, column=1, padx=10, pady=10)
        
        button2 = customtkinter.CTkButton(frame2b, text="",
                            width=120, height=120,
                            corner_radius=20,
                            fg_color="#015395",
                            hover_color="#013865",
                            image=self.button_image2,
                            text_color="#FFFFFF",
                            command=lambda: self.controller.show_frame("TopupPage"))
        button2.pack()
        label4 = customtkinter.CTkLabel(frame2b, text="Topup saldo", font=('Plus Jakarta Sans', 12))
        label4.pack()
        
        frame2c = customtkinter.CTkFrame(frame2, fg_color='transparent')
        frame2c.grid(row=1, column=0, padx=10, pady=10)
        
        button3 = customtkinter.CTkButton(frame2c, text="",
                            width=120, height=120,
                            corner_radius=20,
                            fg_color="#015395",
                            hover_color="#013865",
                            image=self.button_image3,
                            text_color="#FFFFFF",
                            command=lambda: self.controller.show_frame("PurchasePage", True))
        button3.pack()
        label5 = customtkinter.CTkLabel(frame2c, text="Lihat pembelian", font=('Plus Jakarta Sans', 12))
        label5.pack()
        
        frame2d = customtkinter.CTkFrame(frame2, fg_color='transparent')
        frame2d.grid(row=1, column=1, padx=10, pady=10)
        
        button4 = customtkinter.CTkButton(frame2d, text="",
                            width=120, height=120,
                            corner_radius=20,
                            fg_color="#cbd5e1",
                            hover_color="#94a3b8",
                            image=self.button_image4,
                            text_color="#334155",
                            command=lambda: self.controller.show_frame("StartPage"))
        button4.pack()
        label6 = customtkinter.CTkLabel(frame2d, text="Keluar", font=('Plus Jakarta Sans', 12))
        label6.pack()
        
        frame3 = customtkinter.CTkFrame(self.__container, fg_color='#015395')
        frame3a = customtkinter.CTkFrame(frame3, fg_color='transparent')
        label7 = customtkinter.CTkLabel(frame3a, text="Saldo anda:", 
                                        font=('Plus Jakarta Sans', 24, 'bold'),
                                        text_color='#FFFFFF')
        label7.pack(anchor='center', side='top')
        
        label8 = customtkinter.CTkLabel(frame3a, text=f"{Session.USER_DATA.get('saldo')}", 
                                        font=('Plus Jakarta Sans', 20),
                                        text_color='#FFFFFF',
                                        image=self.icon_image1,
                                        compound='left',
                                        padx=5)
        label8.pack(anchor='n', side='top')
        frame3a.pack(fill='both', expand=True, anchor='center', pady=40, padx=40)
        frame3.grid(row=1, column=1, sticky='e', padx=20)
        