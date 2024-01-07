# import tkinter as tk
# from tkinter import font as tkfont
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
import customtkinter, os
from PIL import Image

from concert.views.etc.alert import AlertWindow
from concert.controllers.users import user_ctrl


class RegisterPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        self.__container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.__container.pack(pady=50, padx=120, fill="both")
        
        self.__entries = [
            {
                'name': 'email',
                'label': 'Email',
                'store': customtkinter.StringVar(),
            },
            {
                'name': 'nama',
                'label': 'Nama Lengkap',
                'store': customtkinter.StringVar(),
            },
            {
                'name': 'password',
                'label': 'Password',
                'store': customtkinter.StringVar(),
                'show': '*',
            },
            {
                'name': 'no_telp',
                'label': 'Nomor Telepon',
                'store': customtkinter.StringVar(),
            },
            {
                'name': 'no_identitas',
                'label': 'Nomor Identitas',
                'store': customtkinter.IntVar(),
            },
        ]
        back_image = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/arrow-left-solid-svg.png')), 
            size=(20, 20))
        back_button = customtkinter.CTkButton(self.__container, text="Kembali",
                            fg_color="transparent",
                            hover_color="#FFFFFF",
                            image=back_image,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            text_color="#000000",
                            command=lambda: controller.show_frame("StartPage"))
        back_button.place(x=0, y=12)
        label1 = customtkinter.CTkLabel(self.__container, text="Register", font=('Plus Jakarta Sans', 40, "bold"))
        label1.pack()
        label2 = customtkinter.CTkLabel(self.__container, text="Silahkan buat akun anda", font=('Plus Jakarta Sans', 24))
        label2.pack(pady=10)
        
        frame1 = customtkinter.CTkFrame(self.__container, fg_color='transparent')
        for entry in self.__entries:
            customtkinter.CTkLabel(frame1, text=entry.get('label'), font=('Plus Jakarta Sans', 16)).pack(anchor='w')
            customtkinter.CTkEntry(frame1,textvariable=entry.get('store'), 
                     font=('Plus Jakarta Sans', 16), show=entry.get('show'), width=400).pack(anchor='w', ipady=2)
        frame1.pack(pady=16)
        button_image1 = customtkinter.CTkImage(
            Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static/user-plus-solid-svg.png')), 
            size=(25, 20))
        button1 = customtkinter.CTkButton(self.__container, text="Buat Akun",
                            fg_color="#FFD60A",
                            hover_color="#e6bf00",
                            text_color="#000000",
                            image=button_image1,
                            font=('Plus Jakarta Sans', 16, "bold"),
                            command=self.__register)
        button1.pack(ipady=6, ipadx=6)
        self.alert_window = None
    
    def __register(self):
        res = {}
        for i in range(len(self.__entries)):
            res[self.__entries[i]['name']] = self.__entries[i]['store'].get()
        print('RES>>>>>', res)
        try:
            user_ctrl.register(res)
            print('Berhasil menambahkan akun!')
        except:
            print('Gagal menambahkan akun!')
            self.__failed('Gagal menambahkan akun!')
        self.controller.show_frame("LoginPage")
        
    def __failed(self, error_msg):
        if self.alert_window is None or not self.alert_window.winfo_exists():
            self.alert_window = AlertWindow(self, title="Gagal!", subtitle=error_msg)
        else:
            self.alert_window.focus()
