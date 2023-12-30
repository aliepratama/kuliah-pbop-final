import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class AppPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Silahkan Daftar Akun Baru", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Lihat Tiket Konser",
                           command=lambda: controller.show_frame("ConcertPage"))
        button1.pack()
        button2 = tk.Button(self, text="Topup Saldo",
                           command=lambda: controller.show_frame("TopupPage"))
        button2.pack()
        button3 = tk.Button(self, text="Lihat Pembelian",
                           command=lambda: controller.show_frame("PurchasePage"))
        button3.pack()
        button4 = tk.Button(self, text="Keluar",
                           command=lambda: controller.show_frame("StartPage"))
        button4.pack()
        