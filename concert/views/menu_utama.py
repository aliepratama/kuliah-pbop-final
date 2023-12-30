import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, RegisterPage, AppPage, ConcertPage, TopupPage, PurchasePage, DetailPurchasePage, RefundPage, BuyTicketsPage, DetailConcertPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


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


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Silahkan Daftar Akun Baru", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Daftar",
                           command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        
class AppPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Silahkan Daftar Akun Baru", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Lihat Tiket Konser",
                           command=lambda: controller.show_frame("ConcertPage"))
        button2 = tk.Button(self, text="Topup Saldo",
                           command=lambda: controller.show_frame("TopupPage"))
        button3 = tk.Button(self, text="Lihat Pembelian",
                           command=lambda: controller.show_frame("PurchasePage"))
        button4 = tk.Button(self, text="Keluar",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        
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
        
class BuyTicketsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Beli Tiket", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("ConcertPage"))
        button1.pack()
        
class DetailConcertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Detail Konser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("ConcertPage"))
        button1.pack()
        
class TopupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Top Up", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("AppPage"))
        button1.pack()
        
class PurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Top Up", font=controller.title_font)
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
        
class DetailPurchasePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Detail Transaksi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("PurchasePage"))
        button1.pack()
        
class RefundPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Refund", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Kembali",
                           command=lambda: controller.show_frame("PurchasePage"))
        button1.pack()


app = SampleApp()