import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from concert.controllers.users import user_ctrl

class TopupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__entries = [
            {
                'name': 'topup',
                'label': 'Nominal Topup',
                'store': tk.IntVar(),
            },
        ]
        label = tk.Label(self, text="Top Up", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        for entry in self.__entries:
            tk.Label(self, text=entry.get('label'), font=self.controller.title_font).pack()
            tk.Entry(self,textvariable=entry.get('store'), 
                     font=self.controller.title_font, show=entry.get('show')).pack()
        button1 = tk.Button(self, text="Topup",
                           command=self._topup)
        button1.pack()
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("AppPage", True))
        button2.pack()
        
    def _topup(self):
        saldo = self.__entries[0]['store'].get()
        try:
            user_ctrl.ubah_saldo(saldo, True)
            print('Berhasil topup!')
        except Exception as e:
            print('Gagal topup!', e)
        self.controller.show_frame("AppPage", True)
        