import questionary as qs
from concert.helpers.console import console, clear_output
from concert.helpers.session import Session
from concert.views_cli.exit_view import exit_view
from concert.views_cli.concerts.show_concerts import show_concerts
from concert.views_cli.payments.topup import topup
from concert.views_cli.purchases.show_purchaces import show_purchaces

menu = ["🕵️ Lihat info konser", "💵 Top Up Saldo", "📩 Pesanan Saya", "❌ Keluar"]

def menu_app():
    while True:
        clear_output()
        console.print(f'SELAMAT DATANG {Session.USER_DATA["nama"]} DI HAFLOKET', style='bold dark_olive_green3')
        console.print('PILIH LAYANAN KAMI!', style='dark_olive_green3')
        console.print(f'SALDO ANDA: {Session.USER_DATA["saldo"]}', style='dark_olive_green3')
        pilihan = qs.select("Silahkan pilih", choices=menu).ask()
        if pilihan == menu[-1]:
            break
        elif pilihan == menu[0]:
            show_concerts()
        elif pilihan == menu[1]:
            topup()
        elif pilihan == menu[2]:
            show_purchaces()