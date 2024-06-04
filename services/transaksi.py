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
    
def getTransaksiByDateRange(startDate=None, endDate=None, id_pengguna=None, cursor=None):
    query = '''
        SELECT 
            T.id_transaksi, 
            T.tanggal_transaksi, 
            P.username, 
            F.nama AS nama_furnitur,
            BF.nama AS nama_bagian_furnitur,
            TBF.kuantitas,
            W.id_warna,
            W.nama AS nama_warna,
            M.id_material,
            M.nama AS nama_material,
            DBF.harga
        FROM Transaksi T 
        JOIN Transaksi_Bagian_Furnitur TBF
        ON T.id_transaksi = TBF.id_transaksi
        JOIN Furnitur F
        ON T.id_furnitur = F.id_furnitur
        JOIN Pengguna P
        ON T.id_pengguna = P.id_pengguna
        JOIN Bagian_Furnitur BF
        ON TBF.id_bagian_furnitur = BF.id_bagian_furnitur
        JOIN Warna W
        ON TBF.id_warna = W.id_warna
        JOIN Material M
        ON TBF.id_material = M.id_material
        JOIN Detail_Bagian_Furnitur DBF
        ON TBF.id_bagian_furnitur = DBF.id_bagian_furnitur AND TBF.id_warna = DBF.id_warna AND TBF.id_material = TBF.id_material
    '''

    
    values = []
    hasDate = False
    if(startDate is not None and endDate is not None):
        hasDate = True
        query += "WHERE T.tanggal_transaksi >= ? AND T.tanggal_transaksi <= ?"
        values.append(startDate)
        values.append(endDate)

    if id_pengguna is not None : 
        if hasDate == False : 
            query += " WHERE T.id_pengguna = ?"
        else : 
            query += " AND T.id_pengguna = ?"

        values.append(id_pengguna)

    query += " ORDER BY T.tanggal_transaksi ASC"

    transaksi = cursor.execute(query, values).fetchall()
    
    if(transaksi is None):
        raise Exception("Tidak terdapat terdapat transaksi pada rentang tersebut")
    
    columnNames = [column[0] for column in cursor.description]

    transaksiList = []
    for i in range(0, len(transaksi)) :
        transaksiDict = {}
        for j in range(0, len(columnNames)) :
            transaksiDict[columnNames[j]] = transaksi[i][j]
        transaksiList.append(transaksiDict)

    return transaksiList

def getTotalPendapatan(startDate, endDate, cursor=None):
    query = '''
    SELECT 
    SUM(DBF.harga * TBF.kuantitas) AS totalPendapatan
    FROM Transaksi T 
    JOIN Transaksi_Bagian_Furnitur TBF
    ON T.id_transaksi = TBF.id_transaksi
    JOIN Detail_Bagian_Furnitur DBF
    ON TBF.id_bagian_furnitur = DBF.id_bagian_furnitur AND TBF.id_warna = DBF.id_warna AND TBF.id_material = TBF.id_material
    WHERE T.tanggal_transaksi >= ? AND T.tanggal_transaksi <= ?
    '''

    queryResult = cursor.execute(query, (startDate, endDate))

    totalPendapatan = queryResult.fetchone()[0]

    return totalPendapatan