import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class RefundPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Refund", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Konfirmasi",
                           command=self._refund)
        button1.pack()
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("PurchasePage", True))
        button2.pack()
        
    def _refund(self):
        purchases_ctrl.refund(Session.USER_DATA['purchase_id'])
        self.controller.show_frame("PurchasePage", True)