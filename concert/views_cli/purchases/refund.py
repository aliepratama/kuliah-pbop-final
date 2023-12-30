import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.purchases import purchases_ctrl

def refund(id_pembelian):
    while True:
        clear_output()
        if qs.confirm("Konfirmasi untuk refund?").ask():
            try:
                loading()
                purchases_ctrl.refund(id_pembelian)
                success_msg('Berhasil melakukan refund!')
                return True
            except Exception as e:
                error_msg(e)
        else:
            break
