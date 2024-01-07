import ttkbootstrap.constants as ttkc
from ttkbootstrap.tableview import Tableview
import customtkinter, os
from PIL import Image

from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class PurchasePage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        
    def update_view(self):
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=40, padx=40, fill="both")
        
        col, res = purchases_ctrl.lihat_semua_pembelian()
        
        label1 = customtkinter.CTkLabel(self.__container, text="Data Pembelian", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Silahkan lihat pembelian anda", font=('Plus Jakarta Sans', 24))
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
                            command=lambda: self.controller.show_frame("AppPage", True))
        back_button.place(x=0, y=12)
        
        self.dt = Tableview(
            master=self.__container,
            coldata=col,
            rowdata=res,
            paginated=True,
            searchable=True,
            bootstyle=ttkc.PRIMARY,
        )
        self.dt.pack(fill=ttkc.BOTH, expand=ttkc.YES, padx=10, pady=10)
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color="transparent")
        frame1.pack(pady=12, anchor='center')
        
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/rotate-left-solid-svg.png')), 
            size=(20, 20))
        button1 = customtkinter.CTkButton(frame1, text="Refund",
                            fg_color="#FFD60A",
                            hover_color="#e6bf00",
                            text_color="#000000",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=self.__refund)
        
        button_image2 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/circle-info-solid-svg.png')), 
            size=(20, 20))
        button2 = customtkinter.CTkButton(frame1, text="Detail pembelian",
                            fg_color="#015395",
                            hover_color="#013865",
                            text_color="#FFFFFF",
                            image=button_image2,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=self.__detail)
        button1.grid(row=0, column=0, ipady=6, ipadx=6, padx=8)
        button2.grid(row=0, column=1, ipady=6, ipadx=6)
        
    def __detail(self):
        print(self.dt.get_rows(selected=True)[0].values)
        Session.USER_DATA['purchase_id'] = self.dt.get_rows(selected=True)[0].values[0]
        self.controller.show_frame("DetailPurchasePage", True)
    
    def __refund(self):
        print(self.dt.get_rows(selected=True)[0].values)
        Session.USER_DATA['purchase_id'] = self.dt.get_rows(selected=True)[0].values[0]
        self.controller.show_frame("RefundPage")