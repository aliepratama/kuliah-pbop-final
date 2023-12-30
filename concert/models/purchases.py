from concert.models.base import ModelBase
from concert.config import Config

class ModelPurchases(ModelBase):
    def __init__(self):
        super().__init__(Config.DB_FILE)
        self.connect()
        query = """
        CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                tiket_id INTEGER NOT NULL,
                kuantitas INTEGER,
                total_pembayaran VARCHAR(15),
                tanggal_transaksi DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                status_refund BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(tiket_id) REFERENCES tickets(id)
            )
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
        
    def insert(self, data):
        super().insert('purchases', data)
    
    def select(self, condition='', fields='*', order='id desc'):
        return super().select('purchases', condition, fields, order)
    
    def update(self, data, condition):
        super().update('purchases', data, condition)
        
    def count_rows(self, condition=''):
        return super().count_rows('purchases', condition)
    