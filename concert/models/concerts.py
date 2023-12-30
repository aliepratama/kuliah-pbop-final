from concert.models.base import ModelBase
from concert.config import Config

class ModelConcerts(ModelBase):
    def __init__(self):
        super().__init__(Config.DB_FILE)
        self.connect()
        query = """
        CREATE TABLE IF NOT EXISTS concerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tanggal DATETIME NOT NULL,
                nama_konser VARCHAR(100) NOT NULL,
                lokasi VARCHAR(100) NOT NULL,
                deskripsi VARCHAR(100)
            )
        """
        self.cur.execute(query)
        self.db.commit()
        self.db.close()
    
    def select(self, condition='', fields='*', order='id desc'):
        return super().select('concerts', condition, fields, order)
