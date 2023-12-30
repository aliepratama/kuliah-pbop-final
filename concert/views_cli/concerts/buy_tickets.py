import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.tickets import ticket_ctrl
from concert.controllers.purchases import purchases_ctrl

def buy_tickets(id):
    while True:
        clear_output()
        res = ticket_ctrl.lihat_semua_tiket(id)
        choices_id = list(map(lambda x: x['id'], res))
        choices = list(map(lambda x: x['Jenis Tiket'], res))
        choices.append("❌ Keluar")
        console.print(tabel('Semua Data Tiket', res))
        pilihan = qs.select("Silahkan pilih tiket",
                        choices=choices).ask()
        if pilihan == choices[-1]:
            break
        else:
            while True:
                clear_output()
                console.print(pilihan, style='bold dark_olive_green3')
                temp_id = choices_id[choices.index(pilihan)]
                try:
                    res = qs.text("Jumlah orang", 
                                validate=lambda text: True if text.isnumeric() and text != '0' else "Masukkan data angka"
                                ).ask()
                    try:
                        loading()
                        purchases_ctrl.purchase(temp_id, res)
                        success_msg('Berhasil melakukan transaksi!')
                        return True
                    except Exception as e:
                        error_msg(e)
                        break
                except KeyboardInterrupt:
                    break
