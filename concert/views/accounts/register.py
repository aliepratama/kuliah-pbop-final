import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from concert.controllers.users import user_ctrl


class RegisterPage(tk.Frame):

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
                'name': 'nama',
                'label': 'Nama Lengkap',
                'store': tk.StringVar(),
            },
            {
                'name': 'password',
                'label': 'Password',
                'store': tk.StringVar(),
                'show': '*',
            },
            {
                'name': 'no_telp',
                'label': 'Nomor Telepon',
                'store': tk.StringVar(),
            },
            {
                'name': 'no_identitas',
                'label': 'Nomor Identitas',
                'store': tk.IntVar(),
            },
        ]
        label = tk.Label(self, text="Silahkan Daftar Akun Baru", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        for entry in self.__entries:
            tk.Label(self, text=entry.get('label'), font=controller.title_font).pack()
            tk.Entry(self,textvariable=entry.get('store'), 
                     font=controller.title_font, show=entry.get('show')).pack()
        button1 = tk.Button(self, text="Daftar",
                           command=self._register)
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
    
    def _register(self):
        res = {}
        for i in range(len(self.__entries)):
            res[self.__entries[i]['name']] = self.__entries[i]['store'].get()
        print('RES>>>>>', res)
        try:
            user_ctrl.register(res)
            print('Berhasil menambahkan akun!')
        except:
            print('Gagal menambahkan akun!')
        self.controller.show_frame("LoginPage")