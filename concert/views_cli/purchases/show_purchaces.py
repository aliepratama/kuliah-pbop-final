import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.purchases import purchases_ctrl
from concert.views_cli.purchases.detail_purchases import detail_purchaces
from concert.views_cli.purchases.refund import refund

menu_konser = ["Detail Pembelian", "Refund", "❌ Keluar"]

def show_purchaces():
    while True:
        clear_output()
        res = purchases_ctrl.lihat_semua_pembelian()
        if res:
            choices_id = list(map(lambda x: x['id'], res))
            choices = list(map(lambda x: str(x['Judul']), res))
            choices.append("❌ Keluar")
            console.print(tabel('Semua Data Pembelian', res))
            pilihan = qs.select("Silahkan pilih pembelian",
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
                        detail_purchaces(temp_id)
                    elif pilihan_1 == menu_konser[1]:
                        if purchases_ctrl.cek_refund(temp_id):
                            error_msg("Pesanan ini sudah melakukan refund")
                        else:
                            refund(temp_id)
        else:
            error_msg("Anda belum memiliki pesanan!")
            break
