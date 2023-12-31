import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class PurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
    def update_view(self):
        col, res = purchases_ctrl.lihat_semua_pembelian()
        label = tk.Label(self, text="Menu Transaksi", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
        )
        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        button1 = tk.Button(self, text="Detail Purchase",
                           command=self._detail)
        button2 = tk.Button(self, text="Refund",
                           command=self._refund)
        button3 = tk.Button(self, text="Kembali",
                           command=lambda: self.controller.show_frame("AppPage", True))
        button1.pack()
        button2.pack()
        button3.pack()
        
    def _detail(self):
        print(self.dt.get_rows(selected=True)[0].values)
        Session.USER_DATA['purchase_id'] = self.dt.get_rows(selected=True)[0].values[0]
        self.controller.show_frame("DetailPurchasePage", True)
    
    def _refund(self):
        print(self.dt.get_rows(selected=True)[0].values)
        Session.USER_DATA['purchase_id'] = self.dt.get_rows(selected=True)[0].values[0]
        self.controller.show_frame("RefundPage")