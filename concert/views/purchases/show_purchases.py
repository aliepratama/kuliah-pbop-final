import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu Transaksi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Detail Purchase",
                           command=lambda: controller.show_frame("DetailPurchasePage"))
        button2 = tk.Button(self, text="Refund",
                           command=lambda: controller.show_frame("RefundPage"))
        button3 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("AppPage"))
        button1.pack()
        button2.pack()
        button3.pack()
        