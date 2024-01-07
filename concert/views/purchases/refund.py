import customtkinter, os
from PIL import Image


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class RefundPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=120, padx=120, fill="both")
        
        label1 = customtkinter.CTkLabel(self.__container, text="Konfirmasi", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Apakah anda yankin untuk refund?", font=('Plus Jakarta Sans', 24))
        label2.pack(pady=10)
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color="transparent")
        frame1.pack(pady=12, anchor='center')
        
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/arrow-left-solid-svg (1).png')), 
            size=(18, 20))
        button1 = customtkinter.CTkButton(frame1, text="Batalkan",
                            fg_color="#cbd5e1",
                            hover_color="#94a3b8",
                            text_color="#334155",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=lambda: controller.show_frame("PurchasePage", True))
        
        button_image2 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/circle-check-solid-svg.png')), 
            size=(20, 20))
        button2 = customtkinter.CTkButton(frame1, text="Konfirmasi",
                            fg_color="#015395",
                            hover_color="#013865",
                            text_color="#FFFFFF",
                            image=button_image2,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=self.__refund)
        button1.grid(row=0, column=0, ipady=6, ipadx=6, padx=8)
        button2.grid(row=0, column=1, ipady=6, ipadx=6)
        
    def __refund(self):
        purchases_ctrl.refund(Session.USER_DATA['purchase_id'])
        self.controller.show_frame("PurchasePage", True)