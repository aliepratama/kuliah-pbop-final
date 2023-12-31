import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from concert.helpers.session import Session


class AppPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
    def update_view(self):
        label1 = tk.Label(self, text="Silahkan Daftar Akun Baru", font=self.controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text=f"Saldo: {Session.USER_DATA.get('saldo')}", font=self.controller.title_font)
        label2.pack()
        button1 = tk.Button(self, text="Lihat Tiket Konser",
                           command=lambda: self.controller.show_frame("ConcertPage"))
        button1.pack()
        button2 = tk.Button(self, text="Topup Saldo",
                           command=lambda: self.controller.show_frame("TopupPage"))
        button2.pack()
        button3 = tk.Button(self, text="Lihat Pembelian",
                           command=lambda: self.controller.show_frame("PurchasePage", True))
        button3.pack()
        button4 = tk.Button(self, text="Keluar",
                           command=lambda: self.controller.show_frame("StartPage"))
        button4.pack()
        