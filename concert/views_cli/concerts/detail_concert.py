import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading, tabel
from concert.controllers.concerts import concert_ctrl

def detail_concert(id):
    clear_output()
    res = concert_ctrl.lihat_detail_konser(id)
    console.print(tabel('Detail Data Konser', res))
    qs.press_any_key_to_continue(
        message="Ketik manapun untuk kembali...").ask()