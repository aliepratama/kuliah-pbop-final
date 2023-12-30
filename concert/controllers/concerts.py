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
        res = self.model.select(condition=f"id={id}")
        tuple_into_dict = lambda x: {
            'Tanggal': x[1], 
            'Judul Konser': x[2],
            'Lokasi': x[3],
            'Deskripsi': x[4]
        }
        return list(map(tuple_into_dict, res))
    
    def get_format_nama(self, id):
        res = self.model.select(fields="nama_konser", condition="id=%s"%(id,))
        return res[0][0]
        
concert_ctrl = ConcertsController()