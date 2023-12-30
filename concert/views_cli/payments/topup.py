import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.users import user_ctrl

def topup():
    while True:
        clear_output()
        console.print('TOP UP SALDO', style='bold dark_olive_green3')
        try:
            res = qs.text("Nominal Topup", 
                        validate=lambda text: True if text.isnumeric() and text != '0' else "Masukkan data angka"
                        ).ask()
            try:
                loading()
                user_ctrl.ubah_saldo(int(res), True)
                success_msg('Berhasil melakukan topup!')
                return True
            except Exception as e:
                error_msg(e)
        except KeyboardInterrupt:
            break