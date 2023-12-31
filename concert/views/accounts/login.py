import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from concert.controllers.users import user_ctrl


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__entries = [
            {
                'name': 'email',
                'label': 'Email',
                'store': tk.StringVar(),
            },
            {
                'name': 'password',
                'label': 'Password',
                'store': tk.StringVar(),
                'show': '*',
            },
        ]
        label = tk.Label(self, text="Silahkan Masuk Aplikasi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        for entry in self.__entries:
            tk.Label(self, text=entry.get('label'), font=controller.title_font).pack()
            tk.Entry(self,textvariable=entry.get('store'), 
                     font=controller.title_font, show=entry.get('show')).pack()
        button1 = tk.Button(self, text="Masuk",
                           command=self._login)
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()

    def _login(self):
        res = {}
        for i in range(len(self.__entries)):
            res[self.__entries[i]['name']] = self.__entries[i]['store'].get()
        print('RES>>>>>', res)
        try:
            user_ctrl.login(res)
            print('Berhasil masuk!')
            self.controller.show_frame("AppPage", True)
        except Exception as e:
            print(e)
        