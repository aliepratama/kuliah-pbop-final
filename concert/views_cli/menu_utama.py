import questionary as qs
from concert.helpers.console import console, clear_output

from concert.views_cli.exit_view import exit_view
from concert.views_cli.accounts.login import login_view
from concert.views_cli.accounts.register import register_view
from concert.views_cli.menu_app import menu_app

def menu_utama():
    while True:
        clear_output()
        console.print('SELAMAT DATANG DI HAFLOKET', style='bold dark_olive_green3')
        console.print(' "PESAN TIKET KONSER DENGAN SENTUHAN JARI" ', style='dark_olive_green3')
        console.print('APLIKASI PEMBELIAN TIKET KONSER', style='dark_sea_green3')
        pilihan = qs.select("Silahkan pilih",
                    choices=[
                        "👥 Buat Akun",
                        "📥 Masuk",
                        "❌ Keluar"
                    ]).ask()
        if pilihan == '👥 Buat Akun':
            register_view()
        elif pilihan == '📥 Masuk':
            if login_view():
                menu_app()
        elif pilihan == '❌ Keluar':
            exit_view()
            break
    