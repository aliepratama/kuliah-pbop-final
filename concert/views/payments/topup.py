import customtkinter, os
from PIL import Image

from concert.controllers.users import user_ctrl

class TopupPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=120, padx=120, fill="both")
        
        self.__entries = [
            {
                'name': 'topup',
                'label': 'Nominal Topup',
                'store': customtkinter.IntVar(),
            },
        ]
        
        back_image = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/arrow-left-solid-svg.png')), 
            size=(20, 20))
        back_button = customtkinter.CTkButton(self.__container, text="Kembali",
                            fg_color="transparent",
                            hover_color="#FFFFFF",
                            image=back_image,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#000000",
                            command=lambda: controller.show_frame("AppPage", True))
        back_button.place(x=0, y=12)
        label1 = customtkinter.CTkLabel(self.__container, text="Topup", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Silahkan masukkan nominal Rupiah", font=('Plus Jakarta Sans', 24))
        label2.pack(pady=10)
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color='transparent')
        for entry in self.__entries:
            customtkinter.CTkLabel(frame1, text=entry.get('label'), font=('Plus Jakarta Sans', 16)).pack(anchor='w')
            customtkinter.CTkEntry(frame1,textvariable=entry.get('store'), 
                     font=('Plus Jakarta Sans', 16), show=entry.get('show'), width=400).pack(anchor='w', ipady=2)
        frame1.pack(pady=16)
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/circle-up-solid-svg.png')), 
            size=(20, 20))
        button1 = customtkinter.CTkButton(self.__container, text="Topup saldo",
                            fg_color="#015395",
                            hover_color="#013865",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#FFFFFF",
                            command=self.__topup)
        button1.pack(ipady=6, ipadx=6)
        
    def __topup(self):
        saldo = self.__entries[0]['store'].get()
        try:
            user_ctrl.ubah_saldo(saldo, True)
            print('Berhasil topup!')
        except Exception as e:
            print('Gagal topup!', e)
        self.controller.show_frame("AppPage", True)
        