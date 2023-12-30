import questionary as qs, re
from concert.helpers.console import console, clear_output, success_msg, error_msg, loading
from concert.controllers.users import user_ctrl


def password_validator(password):
    if len(password) < 6:
        return "Password harus lebih dari 6 karakter"
    elif re.search("[0-9]", password) is None:
        return "Password harus ada angka"
    elif re.search("[a-z]", password) is None:
        return "Password harus ada huruf kecil"
    elif re.search("[A-Z]", password) is None:
        return "Password harus ada huruf besar"
    else:
        return True

questions = [
    {
        'type': 'text',
        'name': 'email',
        'message': "Masukkan email anda",
    },
    {
        'type': 'text',
        'name': 'nama',
        'message': "Masukkan nama lengkap anda",
    },
    {
        'type': 'password',
        'name': 'password',
        "validate": password_validator,
        'message': "Masukkan password anda",
    },
    {
        'type': 'text',
        'name': 'no_telp',
        'message': "Masukkan nomor telepon anda",
    },
    {
        'type': 'text',
        'name': 'no_identitas',
        'message': "Masukkan nomor identitas anda",
    },
    {
        'type': 'confirm',
        'message': 'Konfirmasi untuk membuat akun',
        'name': 'konfirmasi',
        'default': True,
    }
]

def register_view():
    clear_output()
    console.print('BUAT AKUN', style='bold dark_cyan')
    res = qs.prompt(questions)
    res.pop('konfirmasi', None)
    try:
        loading()
        user_ctrl.register(res)
        success_msg('Berhasil menambahkan akun!')
    except:
        error_msg('Gagal menambahkan akun!')
    