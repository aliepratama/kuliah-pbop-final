from concert.models.concerts import ModelConcerts

class ConcertsController:
    def __init__(self):
        self.model = ModelConcerts()
    
    def lihat_semua_konser(self):
        res = self.model.select(order="tanggal desc")
        col = ('id', 'Tanggal', 'Judul Konser', 'Lokasi', 'Deskripsi')
        print('CTRL SHOW KONSER>>>>', res)
        return col, res
    
    def lihat_detail_konser(self, id):
        transform = lambda x : (x[1], x[2], x[3], x[4])
        res = list(map(transform, self.model.select(condition=f"id={id}")))
        col = ('Tanggal', 'Judul Konser', 'Lokasi', 'Deskripsi')
        print('CTRL DETAIL KONSER>>>>', res)
        return col, res
    
    def get_format_nama(self, id):
        res = self.model.select(fields="nama_konser", condition="id=%s"%(id,))
        return res[0][0]
        
concert_ctrl = ConcertsController()