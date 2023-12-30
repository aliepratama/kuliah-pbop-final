import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.concerts import concert_ctrl
from concert.views_cli.concerts.detail_concert import detail_concert
from concert.views_cli.concerts.buy_tickets import buy_tickets

menu_konser = ["Detail Konser", "Beli Tiket", "❌ Keluar"]

def show_concerts():
    while True:
        clear_output()
        res = concert_ctrl.lihat_semua_konser()
        choices_id = list(map(lambda x: x['id'], res))
        choices = list(map(lambda x: x['Judul Konser'], res))
        choices.append("❌ Keluar")
        console.print(tabel('Semua Data Konser', res))
        pilihan = qs.select("Silahkan pilih konser",
                        choices=choices).ask()
        if pilihan == choices[-1]:
            break
        else:
            while True:
                clear_output()
                console.print(pilihan, style='bold dark_olive_green3')
                temp_id = choices_id[choices.index(pilihan)]
                pilihan_1 = qs.select("Silahkan pilih layanan",
                            choices=menu_konser).ask()
                if pilihan_1 == menu_konser[-1]:
                    break
                elif pilihan_1 == menu_konser[0]:
                    detail_concert(temp_id)
                elif pilihan_1 == menu_konser[1]:
                    buy_tickets(temp_id)
                    