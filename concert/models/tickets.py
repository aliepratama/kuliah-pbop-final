from concert.models.base import ModelBase
from concert.config import Config
  

class ModelTickets(ModelBase):
    def __init__(self):
        super().__init__(Config.DB_FILE)
        self.connect()
        query = """
        CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                konser_id INTEGER NOT NULL,
                jenis_tiket VARCHAR(30) NOT NULL,
                stok INTEGER,
                harga FLOAT,
                FOREIGN KEY (konser_id) REFERENCES concerts(id)
            )
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def select(self, condition='', fields='*', order='id desc'):
        return super().select('tickets', condition, fields, order)

    def update(self, data, condition):
        super().update('tickets', data, condition)
