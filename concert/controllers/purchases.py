from concert.models.purchases import ModelPurchases
from concert.helpers.session import Session
from concert.controllers.tickets import ticket_ctrl
from concert.controllers.users import user_ctrl
from concert.controllers.concerts import concert_ctrl

class PurchasesController:
    def __init__(self):
        self.model = ModelPurchases()
        
    def purchase(self, id_tiket, quantity):
        quantity = int(quantity)
        total = ticket_ctrl.lihat_harga_tiket(id_tiket) * quantity
        if user_ctrl.get_saldo() > total:
            req = {
                'user_id': Session.USER_ID,
                'tiket_id': id_tiket,
                'kuantitas': quantity,
                'total_pembayaran': total,
            }
            self.model.insert(req)
            user_ctrl.ubah_saldo(total, False)
            ticket_ctrl.ubah_stok(id_tiket, quantity, False)
        else:
            raise Exception("Saldo tidak mencukupi!")
        
    def lihat_semua_pembelian(self):
        if self.model.count_rows()[0] > 0:
            transform = lambda x: (x[0], ticket_ctrl.get_format_nama(x[2]), x[3],
                                   x[4], x[5], 'Refund' if x[6] == 1 else 'Normal')
            res = list(map(transform, self.model.select(order="tanggal_transaksi desc",
                                    condition="user_id=%s"%(Session.USER_ID,))))
            col = ('id', 'Judul', 'Kuantitas', 'Total', 'Tanggal', 'Status')
            return col, res
        return None
    
    def refund(self, id_purchase):
        res = self.model.select(fields='total_pembayaran, tiket_id, kuantitas',
                                condition="id=%s"%(id_purchase,))
        self.model.update({'status_refund': 1}, 'id=%s'%(id_purchase,))
        user_ctrl.ubah_saldo(float(res[0][0]), True)
        ticket_ctrl.ubah_stok(res[0][1], res[0][2], True)
        
    def lihat_detail_pembelian(self, id_purchase):
        all_info = []
        transform = lambda x: (x[0], x[2], x[3], x[4], x[5],
                               'Refund' if x[6] == 1 else 'Normal')
        res = list(map(transform, self.model.select(condition="id=%s"%(id_purchase,))))
        col = ('id', 'ID Tiket', 'Kuantitas', 'Total', 'Tanggal', 'Status')
        all_info.append((col, res))
        res = self.model.select(fields='tiket_id',
            condition="id=%s"%(id_purchase,))
        all_info.append(ticket_ctrl.lihat_detail_tiket(res[0][0]))
        all_info.append(concert_ctrl.lihat_detail_konser(
            ticket_ctrl.get_id_konser(res[0][0])
        ))
        return all_info
        
    def cek_refund(self, id_purchase):
        res = self.model.select(fields="status_refund",
            condition="id=%s"%(id_purchase,))
        return res[0][0] == 1
    
        
purchases_ctrl = PurchasesController()
