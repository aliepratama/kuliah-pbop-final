from concert.models.users import ModelUsers
from concert.helpers.session import Session

class UsersController:
    def __init__(self):
        self.model = ModelUsers()
        
    def register(self, data):
        pwd = data.get('password')
        pwd = self.model.make_password_hash(pwd)
        data['password'] = pwd
        self.model.insert(data)
    
    def login(self, data):
        res = self.model.select(
            condition="email='%s'"%(data['email'])
        )
        if len(res) == 0:
            raise Exception('Email tidak ditemukan!')
        res = res[0]
        if not self.model.check_password_hash(res[3], data['password']):
            raise Exception('Password salah!')
        Session.USER_ID = res[0]
        Session.USER_DATA = {
            'email': res[1],
            'nama': res[2],
            'saldo': res[5],
        }
        
    def ubah_saldo(self, nominal, is_add = True):
        res = self.model.select(fields='saldo',
                                condition='id=%s'%(Session.USER_ID,))
        if is_add:
            saldo = res[0][0] + nominal
        else:
            saldo = res[0][0] - nominal
        req = {
            'saldo': saldo
        }
        self.model.update(req, 'id=%s'%(Session.USER_ID,))
        Session.USER_DATA['saldo'] = saldo
    
    def get_saldo(self):
        return self.model.select(fields='saldo',
                                condition='id=%s'%(Session.USER_ID,))[0][0]
        
        
user_ctrl = UsersController()
