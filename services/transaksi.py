def insertTransaksi(id_pengguna, id_furnitur, cursor=None):
    query = '''INSERT INTO transaksi (id_pengguna, id_furnitur) VALUES (?, ?)'''

    cursor.execute(query, (id_pengguna, id_furnitur))

def insertManyTransaksiBagianFurnitur(id_transaksi,transaksiBagianFurniturData,cursor=None) : 
    query = '''INSERT INTO (id_transaksi, id_bagian_furnitur, id_warna, id_material, kuantitas)
    VALUES '''

    colValues = []
    for data in transaksiBagianFurniturData:
        query += "(?, ?, ?, ?, ?), "
        colValues.append(id_transaksi)
        colValues.append(data.get("id_bagian_furnitur"))
        colValues.append(data.get("id_warna"))
        colValues.append(data.get("id_material"))
        colValues.append(data.get("kuantitas"))
    
    query = query.rstrip(", ")

    cursor.execute(query, colValues)