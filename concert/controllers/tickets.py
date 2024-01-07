from concert.models.tickets import ModelTickets
from concert.controllers.concerts import concert_ctrl

class TicketsController:
    def __init__(self):
        self.model = ModelTickets()
    
    def lihat_semua_tiket(self, id_konser):
        res = self.model.select(order="id asc", 
                                condition="konser_id=%s"%(id_konser,))
        col = ['id', 'Konser ID', 'Jenis Tiket', 'Stok', 'Harga']
        print('CTRL SHOW TIKET>>>>', res)
        return col, res
    
    def lihat_harga_tiket(self, id_tiket):
        res = self.model.select(fields='harga',
                                order="id asc", 
                                condition="id=%s"%(id_tiket,))
        return res[0][0]
    
    def ubah_stok(self, id_tiket, stok, is_add = True):
        res = self.model.select(fields='stok',
                                condition='id=%s'%(id_tiket,))
        if is_add:
            req = {
                'stok': res[0][0] + stok
            }
        else:
            req = {
                'stok': res[0][0] - stok
            }
        self.model.update(req, 'id=%s'%(id_tiket,))
        
    def lihat_detail_tiket(self, id):
        transform = lambda x: [['id', x[0]], ['Jenis Tiket', x[2]], ['Stok', x[3]], ['Harga', x[4]]]
        res = list(map(transform, self.model.select(condition="id=%s"%(id,))))
        return res[0]
    
    def get_id_konser(self, id):
        res = self.model.select(fields="konser_id", condition="id=%s"%(id,))
        return res[0][0]
    
    def get_format_nama(self, id):
        res = self.model.select(fields="jenis_tiket, konser_id", condition="id=%s"%(id,))
        judul_konser = concert_ctrl.get_format_nama(res[0][1])
        return f"{judul_konser} | {res[0][0]}"
        
ticket_ctrl = TicketsController()
