import ttkbootstrap.constants as ttkc
from ttkbootstrap.tableview import Tableview
import customtkinter, os
from PIL import Image

from concert.controllers.tickets import ticket_ctrl
from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class BuyTicketsPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        self.__entries = [
            {
                'name': 'quantity',
                'label': 'Jumlah Tiket',
                'store': customtkinter.IntVar(),
            },
        ]
        
    def update_view(self):
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=40, padx=120, fill="both")
        
        col, res = ticket_ctrl.lihat_semua_tiket(Session.USER_DATA.get('concert_id'))
        label1 = customtkinter.CTkLabel(self.__container, text="Beli tiket", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Silahkan pilih jenis tiket dan jumlah", font=('Plus Jakarta Sans', 24))
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
                            command=lambda: self.controller.show_frame("ConcertPage"))
        back_button.place(x=0, y=12)
        
        self.dt = Tableview(
            master=self.__container,
            coldata=col,
            rowdata=res,
            bootstyle=ttkc.PRIMARY,
        )
        for c_id in [0, 1]:
            self.dt.hide_selected_column(cid=c_id)
        self.dt.pack(fill=ttkc.BOTH, expand=ttkc.YES, padx=10, pady=10)
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color='transparent')
        for entry in self.__entries:
            customtkinter.CTkLabel(frame1, text=entry.get('label'), font=('Plus Jakarta Sans', 16)).pack(anchor='w')
            customtkinter.CTkEntry(frame1,textvariable=entry.get('store'), 
                     font=('Plus Jakarta Sans', 16), show=entry.get('show'), width=400).pack(anchor='w', ipady=2)
        frame1.pack(pady=8)
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/circle-up-solid-svg.png')), 
            size=(20, 20))
        button1 = customtkinter.CTkButton(self.__container, text="Beli",
                            fg_color="#015395",
                            hover_color="#013865",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#FFFFFF",
                            command=self.__purchase)
        button1.pack(ipady=6, ipadx=2)
        # for entry in self.__entries:
        #     customtkinter.CTkLabel(self, text=entry.get('label'), font=self.controller.title_font).pack()
        #     customtkinter.CTkEntry(self,textvariable=entry.get('store'), 
        #              font=self.controller.title_font, show=entry.get('show')).pack()
        # button1 = customtkinter.CTkButton(self, text="Beli",
        #                    command=self.__purchase)
        # button1.pack()
        # button2 = customtkinter.CTkButton(self, text="Kembali",
        #                    command=lambda: self.controller.show_frame("ConcertPage"))
        # button2.pack()
    
    def __purchase(self):
        print(self.dt.get_rows(selected=True)[0].values)
        id_tiket = self.dt.get_rows(selected=True)[0].values[0]
        quantity = self.__entries[0]['store'].get()
        try:
            purchases_ctrl.purchase(id_tiket, quantity)
            print('Berhasil beli tiket!')
        except Exception as e:
            print('Gagal beli tiket!', e)
        self.controller.show_frame("AppPage", True)
        