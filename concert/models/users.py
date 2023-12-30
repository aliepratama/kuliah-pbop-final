from werkzeug.security import generate_password_hash, check_password_hash
from concert.models.base import ModelBase
from concert.config import Config

class ModelUsers(ModelBase):
    def __init__(self):
        super().__init__(Config.DB_FILE)
        self.connect()
        query = """
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(50) NOT NULL,
                nama VARCHAR(100),
                password VARCHAR(255) NOT NULL,
                no_telp VARCHAR(15),
                saldo FLOAT DEFAULT '0',
                no_identitas VARCHAR(30)
            )
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
        
    def insert(self, data):
        super().insert('users', data)
    
    def select(self, condition='', fields='*', order='id desc'):
        return super().select('users', condition, fields, order)
    
    def update(self, data, condition):
        super().update('users', data, condition)
        
    def make_password_hash(self, password):
        return generate_password_hash(password)
        
    def check_password_hash(self, hashed_password, raw_password):
        return check_password_hash(hashed_password, raw_password)
    