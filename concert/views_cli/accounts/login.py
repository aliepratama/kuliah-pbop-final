import questionary as qs
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading
from concert.controllers.users import user_ctrl


questions = [
    {
        'type': 'text',
        'name': 'email',
        'message': "Masukkan email anda",
    },
    {
        'type': 'password',
        'name': 'password',
        'message': "Masukkan password anda",
    },
]

def login_view():
    clear_output()
    console.print('MASUK APLIKASI', style='bold dark_cyan')
    res = qs.prompt(questions)
    try:
        loading()
        user_ctrl.login(res)
        success_msg('Berhasil masuk!')
        return True
    except Exception as e:
        error_msg(e)