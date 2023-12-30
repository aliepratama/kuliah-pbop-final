import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Selamat Datang di Aplikasi Pemesanan Tiket Konser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Masuk aplikasi",
                            command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(self, text="Buat akun baru",
                            command=lambda: controller.show_frame("RegisterPage"))
        button1.pack()
        button2.pack()
