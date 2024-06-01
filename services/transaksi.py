def insertTransaksi(id_pengguna, id_furnitur, cursor=None):
    query = '''INSERT INTO Transaksi (id_pengguna, id_furnitur)
    OUTPUT INSERTED.id_transaksi
    VALUES (?, ?)'''

    cursor.execute(query, (id_pengguna, id_furnitur))

    id_transaksi = cursor.fetchone()[0]

    return {"id_transaksi": id_transaksi}


def insertManyTransaksiBagianFurnitur(id_transaksi, transaksiBagianFurniturData, cursor=None):
    query = '''INSERT INTO Transaksi_Bagian_Furnitur(id_transaksi, id_bagian_furnitur, id_warna, id_material, kuantitas)
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
