import ttkbootstrap.constants as ttkc
from ttkbootstrap.tableview import Tableview
import customtkinter


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class DetailPurchasePage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        
        
    def update_view(self):
        label = customtkinter.CTkLabel(self, text="Detail Transaksi", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        alldata = purchases_ctrl.lihat_detail_pembelian(Session.USER_DATA.get('purchase_id'))
        for col, res in alldata:
            self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            pagesize=2,
            height=2,
            bootstyle=ttkc.PRIMARY,
            )
            self.dt.pack(fill=ttkc.BOTH, expand=ttkc.YES, padx=10, pady=10)
        button1 = customtkinter.CTkButton(self, text="Kembali",
                           command=lambda: self.controller.show_frame("PurchasePage", True))
        button1.pack()