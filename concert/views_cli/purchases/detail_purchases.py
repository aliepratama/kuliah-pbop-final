import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.purchases import purchases_ctrl

def detail_purchaces(id_pembelian):
    res = purchases_ctrl.lihat_detail_pembelian(id_pembelian)
    titles = ["Detail Pembelian", "Detail Tiket", "Detail Konser"]
    for i in range(len(titles)):
        console.print(tabel(titles[i], res[i]))
    qs.press_any_key_to_continue(
        message="Ketik manapun untuk kembali...").ask()
