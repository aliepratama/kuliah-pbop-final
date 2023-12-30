import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from concert.controllers.tickets import ticket_ctrl
from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class BuyTicketsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__entries = [
            {
                'name': 'quantity',
                'label': 'Jumlah Tiket',
                'store': tk.IntVar(),
            },
        ]
        
    def update_view(self):
        col, res = ticket_ctrl.lihat_semua_tiket(Session.USER_DATA.get('concert_id'))
        label = tk.Label(self, text="Beli Tiket", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            bootstyle=PRIMARY,
        )
        self.dt.hide_selected_column(cid=0)
        self.dt.hide_selected_column(cid=1)
        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        for entry in self.__entries:
            tk.Label(self, text=entry.get('label'), font=self.controller.title_font).pack()
            tk.Entry(self,textvariable=entry.get('store'), 
                     font=self.controller.title_font, show=entry.get('show')).pack()
        button1 = tk.Button(self, text="Beli",
                           command=self._purchase)
        button1.pack()
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: self.controller.show_frame("ConcertPage"))
        button2.pack()
    
    def _purchase(self):
        print(self.dt.get_rows(selected=True)[0].values)
        id_tiket = self.dt.get_rows(selected=True)[0].values[0]
        quantity = self.__entries[0]['store'].get()
        try:
            purchases_ctrl.purchase(id_tiket, quantity)
            print('Berhasil beli tiket!')
        except Exception as e:
            print('Gagal beli tiket!', e)
        self.controller.show_frame("AppPage")
        