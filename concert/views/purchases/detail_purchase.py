import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class DetailPurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
    def update_view(self):
        label = tk.Label(self, text="Detail Transaksi", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        alldata = purchases_ctrl.lihat_detail_pembelian(Session.USER_DATA.get('purchase_id'))
        for col, res in alldata:
            self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            pagesize=2,
            height=2,
            bootstyle=PRIMARY,
            )
            self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: self.controller.show_frame("PurchasePage", True))
        button1.pack()