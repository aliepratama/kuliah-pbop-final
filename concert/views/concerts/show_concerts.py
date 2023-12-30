import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from concert.controllers.concerts import concert_ctrl
from concert.helpers.session import Session


class ConcertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        col, res = concert_ctrl.lihat_semua_konser()
        label = tk.Label(self, text="Data Konser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
        )
        self.dt.hide_selected_column(cid=0)
        self.dt.hide_selected_column(cid=4)
        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        button1 = tk.Button(self, text="Beli Tiket",
                           command=self._read)
        button2 = tk.Button(self, text="Detail Konser",
                           command=lambda: controller.show_frame("DetailConcertPage"))
        button3 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("AppPage"))
        button1.pack()
        button2.pack()
        button3.pack()
    
    def _read(self):
        print(self.dt.get_rows(selected=True)[0].values)
        Session.USER_DATA['concert_id'] = self.dt.get_rows(selected=True)[0].values[0]
        self.controller.show_frame('BuyTicketsPage', update=True
                                   )