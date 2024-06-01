def insertTransaksi(id_pengguna, id_furnitur, cursor=None):
    query = '''INSERT INTO transaksi (id_pengguna, id_furnitur) VALUES (?, ?)'''

    cursor.execute(query, (id_pengguna, id_furnitur))

def insertTransaksiBagianFurnitur(id_transaksi, id_bagian_furnitur,id_warna, id_material, kuantitas,cursor=None) : 
    query = '''INSERT INTO (id_transaksi, id_bagian_furnitur, id_warna, id_material, kuantitas)
    VALUES
    (?, ?, ?, ?, ?)'''

    cursor.execute(query, (id_transaksi, id_bagian_furnitur,id_warna, id_material, kuantitas))