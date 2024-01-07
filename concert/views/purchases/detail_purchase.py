import customtkinter, os
from PIL import Image
from CTkTable import CTkTable


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class DetailPurchasePage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        
        
    def update_view(self):
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=24, padx=48, fill="both")
        
        self.__entries = [
            {
                'title': 'Detail Pembelian',
                'col': 0,
                'row': 0,
                'colspan': 1,
            },
            {
                'title': 'Detail Konser',
                'col': 1,
                'row': 0,
                'colspan': 1,
            },
            {
                'title': 'Detail Tiket',
                'col': 0,
                'row': 1,
                'colspan': 2,
            },
        ]
        
        label1 = customtkinter.CTkLabel(self.__container, text="Detail pembelian", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Berikut detail pembelian yang dipilih", font=('Plus Jakarta Sans', 24))
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
                            command=lambda: self.controller.show_frame("PurchasePage", True))
        back_button.place(x=0, y=0)
        
        alldata = purchases_ctrl.lihat_detail_pembelian(Session.USER_DATA.get('purchase_id'))
        frametables = customtkinter.CTkFrame(self.__container, fg_color="transparent")
        for i in range(len(alldata)):
            dt_frame = customtkinter.CTkFrame(frametables, fg_color="transparent")
            
            dt_label = customtkinter.CTkLabel(dt_frame, text=self.__entries[i]['title'], font=('Plus Jakarta Sans', 12))
            dt_label.pack(pady=1)
            
            dt = CTkTable(
                master=dt_frame,
                values=alldata[i],
            )
            dt.pack()
            
            dt_frame.grid(row=self.__entries[i]['row'], column=self.__entries[i]['col'], columnspan=self.__entries[i]['colspan'], padx=2)
        frametables.pack(pady=20)
            