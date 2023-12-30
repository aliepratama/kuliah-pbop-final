import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Silahkan Masuk Aplikasi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Masuk",
                           command=lambda: controller.show_frame("AppPage"))
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
