import customtkinter, os
from PIL import Image
from CTkTable import CTkTable

from concert.controllers.concerts import concert_ctrl
from concert.helpers.session import Session


class DetailConcertPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
    
    
    def update_view(self):
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=64, padx=48, fill="both")
        
        res = concert_ctrl.lihat_detail_konser(Session.USER_DATA.get('concert_id'))
        
        label1 = customtkinter.CTkLabel(self.__container, text="Detail konser", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Berikut detail konser yang dipilih", font=('Plus Jakarta Sans', 24))
        label2.pack(pady=10)
        
        back_image = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/arrow-left-solid-svg.png')), 
            size=(20, 20))
        back_button = customtkinter.CTkButton(self.__container, text="Kembali",
                            fg_color="transparent",
                            hover_color="#FFFFFF",
                            image=back_image,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#000000",
                            command=lambda: self.controller.show_frame("ConcertPage", True))
        back_button.place(x=0, y=0)
        
        self.dt = CTkTable(
            master=self.__container,
            values=res,
        )
        self.dt.pack(fill='both', expand=True, padx=10, pady=32)
        