import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ConcertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Data Konser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Beli Tiker",
                           command=lambda: controller.show_frame("BuyTicketsPage"))
        button2 = tk.Button(self, text="Detail Konser",
                           command=lambda: controller.show_frame("DetailConcertPage"))
        button3 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("AppPage"))
        button1.pack()
        button2.pack()
        button3.pack()
        