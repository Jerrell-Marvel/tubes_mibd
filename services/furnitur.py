
def insertFurnitur(nama, deskripsi, cursor=None):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi)
        OUTPUT INSERTED.id_furnitur
        VALUES
        (?, ?);
    '''
    queryResult = cursor.execute(query, (nama, deskripsi))

    idFurnitur = queryResult.fetchone()[0]

    return idFurnitur


def insertBagianFurnitur(nama, panjang, lebar, tinggi, id_furnitur, cursor=None):
    query = '''INSERT INTO Bagian_Furnitur (nama, panjang, lebar, tinggi, id_furnitur)
                OUTPUT INSERTED.id_bagian_furnitur
                VALUES (?, ?, ?, ?, ?)'''

    queryResult = cursor.execute(
        query, (nama, panjang, lebar, tinggi, id_furnitur))

    idBagianFurnitur = queryResult.fetchone()[0]

    return idBagianFurnitur


def insertDetailBagianFurnitur(id_bagian_furnitur, id_warna, id_material, harga, stok, cursor=None):
    query = '''INSERT INTO Detail_Bagian_Furnitur (id_bagian_furnitur, id_warna, id_material, harga, stok)
    VALUES (?, ?, ?, ?, ?)'''

    queryResult = cursor.execute(
        query, (id_bagian_furnitur, id_warna, id_material, harga, stok))


def updateFurnitur(id_furnitur, nama=None, deskripsi=None, cursor=None):
    query = '''UPDATE Furnitur SET '''

    colValue = []
    if nama is not None:
        query += f"nama=?, "
        colValue.append(nama)

    if deskripsi is not None:
        query += f"deskripsi=?, "
        colValue.append(deskripsi)

    query = query.rstrip(", ")

    colValue.append(id_furnitur)
    query += " WHERE id_furnitur = ?"

    cursor.execute(query, colValue)


def deleteFurnitur(id_furnitur, cursor=None):
    query = '''UPDATE Furnitur SET is_active = 0 WHERE id_furnitur = ?'''

    cursor.execute(query, (id_furnitur,))


def deleteBagianFurnitur(id_bagian_furnitur, cursor=None):
    query = '''
        UPDATE Bagian_Furnitur 
        SET is_active = 0 
        WHERE id_bagian_furnitur = ?'''

    cursor.execute(query, (id_bagian_furnitur,))


def getAllFurnitur(cursor=None):
    query = '''SELECT id_furnitur, nama, deskripsi FROM Furnitur WHERE is_active = 1'''

    queryResult = cursor.execute(query)

    furnitur = queryResult.fetchall()

    return furnitur


def getDetailFurniturById(id_furnitur, id_bagian_furnitur=None, id_warna=None, id_material=None, cursor=None):
    query = '''
        SELECT 
            f.id_furnitur,
            f.nama as nama_furnitur,
            f.deskripsi,
            bf.id_bagian_furnitur,
            bf.nama AS nama_bagian_furnitur,
            bf.panjang AS panjang,
            bf.lebar AS lebar,
            bf.tinggi AS tinggi,
            w.id_warna AS id_warna,
            w.nama AS nama_warna,
            m.id_material AS id_material,
            m.nama AS nama_material,
            dbf.harga AS harga,
            dbf.stok AS stok
        FROM
            Furnitur f
        INNER JOIN
            Bagian_Furnitur bf
        ON
            f.id_furnitur = bf.id_furnitur
        INNER JOIN
            Detail_Bagian_Furnitur dbf
        ON
            bf.id_bagian_furnitur = dbf.id_bagian_furnitur
        INNER JOIN
            Warna w
        ON
            dbf.id_warna = w.id_warna
        INNER JOIN
            Material m
        ON
            dbf.id_material = m.id_material
        WHERE
            f.id_furnitur = ? AND f.is_active = 1 AND bf.is_active = 1 
    '''
    colValue = [id_furnitur]

    if (id_bagian_furnitur is not None):
        query += f" AND id_bagian_furnitur=?"
        colValue.append(id_bagian_furnitur)

    if (id_warna is not None):
        query += f" AND id_warna=?"
        colValue.append(id_warna)

    if (id_material is not None):
        query += f" AND id_material=?"
        colValue.append(id_material)

    queryResult = cursor.execute(query, colValue)

    detailFurnitur = queryResult.fetchall()

    if detailFurnitur is None:
        raise Exception("Furnitur tidak ditemukan")

    columnNames = [column[0] for column in cursor.description]

    detailFurniturList = []
    for i in range(0, len(detailFurnitur)):
        detailFurniturDict = {}
        for j in range(0, len(columnNames)):
            detailFurniturDict[columnNames[j]] = detailFurnitur[i][j]
        detailFurniturList.append(detailFurniturDict)

    return detailFurniturList


def updateBagianFurnitur(id_bagian_furnitur, id_warna, id_material, nama_bagian_furnitur, panjang, lebar, tinggi, harga, stok, cursor=None):
    queryUpdateBagianFurnitur = '''
        UPDATE Bagian_Furnitur SET
        nama = ?,
        panjang = ?,
        lebar = ?,
        tinggi = ?
        WHERE id_bagian_furnitur = ?
    '''

    queryUpdateDetailBagianFurnitur = '''
        UPDATE Detail_Bagian_Furnitur SET
        harga = ?,
        stok = ?
        WHERE id_bagian_furnitur = ? AND id_warna = ? AND id_material = ?
    '''

    cursor.execute(queryUpdateBagianFurnitur, (nama_bagian_furnitur,
                   panjang, lebar, tinggi, id_bagian_furnitur))
    cursor.execute(queryUpdateDetailBagianFurnitur,
                   (harga, stok, id_bagian_furnitur, id_warna, id_material))


def getDetailBagianFurnitur(id_bagian_furnitur, id_warna, id_material, rowLock=False, cursor=None):
    query = '''SELECT 
    dbf.id_bagian_furnitur,
    dbf.id_warna,
    dbf.id_material,
    dbf.harga,
    dbf.stok
    FROM Detail_Bagian_Furnitur dbf'''

    if rowLock == True:
        query += " WITH (UPDLOCK, ROWLOCK)"

    query += ''' WHERE dbf.id_bagian_furnitur = ? AND dbf.id_warna = ? AND dbf.id_material = ?'''

    queryResult = cursor.execute(
        query, (id_bagian_furnitur, id_warna, id_material))

    detailBagianFurnitur = queryResult.fetchone()

    return {
        "id_bagian_furnitur": detailBagianFurnitur[0],
        "id_warna": detailBagianFurnitur[1],
        "id_material": detailBagianFurnitur[2],
        "harga": detailBagianFurnitur[3],
        "stok": detailBagianFurnitur[4],
    }


def updateStokDetailBagianFurnitur(id_bagian_furnitur, id_warna, id_material, stokDibeli, cursor=None):
    query = '''UPDATE Detail_Bagian_Furnitur SET stok = stok - ? WHERE id_bagian_furnitur = ? AND id_warna = ? AND id_material = ?'''

    queryResult = cursor.execute(
        query, (stokDibeli, id_bagian_furnitur, id_warna, id_material))


# def updateStokDetailBagianFurnitur(id_bagian_furnitur, id_warna, id_material, jumlahStokDibeli, cursor=None):
#     query = ''''''
