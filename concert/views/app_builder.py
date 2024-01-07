import customtkinter

from concert.views.menu_utama import StartPage
from concert.views.menu_app import AppPage
from concert.views.accounts.login import LoginPage
from concert.views.accounts.register import RegisterPage
from concert.views.concerts.show_concerts import ConcertPage
from concert.views.concerts.detail_concert import DetailConcertPage
from concert.views.concerts.buy_ticket import BuyTicketsPage
from concert.views.payments.topup import TopupPage
from concert.views.purchases.show_purchases import PurchasePage
from concert.views.purchases.detail_purchase import DetailPurchasePage
from concert.views.purchases.refund import RefundPage


class ConcertApp(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        customtkinter.set_appearance_mode("light")
        self.title('Aplikasi Pemesanan Tiket Konser')
        self.geometry("720x600")
        self.resizable(0, 0)
        self.configure(background='white')
        self.title_font = customtkinter.CTkFont(family='Arial', size=18, weight="bold")

        self._container = customtkinter.CTkFrame(self, fg_color="white")
        self._container.pack(side="top", fill="both", expand=True)
        self._container.grid_rowconfigure(0, weight=1)
        self._container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, RegisterPage, AppPage, ConcertPage, 
                  TopupPage, PurchasePage, DetailPurchasePage, RefundPage, 
                  BuyTicketsPage, DetailConcertPage):
            page_name = F.__name__
            frame = F(parent=self._container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, update=False):
        frame = self.frames[page_name]
        frame.__init__(parent=self._container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        # if update:
        #     frame.__init__(parent=self._container, controller=self)
        #     frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise() 
        if update:
            frame.update_view()
            
app = ConcertApp()
