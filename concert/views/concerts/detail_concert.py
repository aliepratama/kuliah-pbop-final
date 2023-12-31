import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from concert.controllers.concerts import concert_ctrl
from concert.helpers.session import Session


class DetailConcertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
    
    def update_view(self):
        col, res = concert_ctrl.lihat_detail_konser(Session.USER_DATA.get('concert_id'))
        label = tk.Label(self, text="Detail Konser", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.dt = Tableview(
            master=self,
            coldata=col,
            rowdata=res,
            bootstyle=PRIMARY,
        )
        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: self.controller.show_frame("ConcertPage"))
        button1.pack()