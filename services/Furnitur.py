
def insertFurnitur(nama, deskripsi, cursor=None):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi)
        VALUES
        (?, ?);
    '''
    cursor.execute(query, (nama, deskripsi))


def updateFurnitur(id_furnitur, nama=None, deskripsi=None, cursor=None):
    query = '''UPDATE Furnitur SET '''

    colValue = []
    if nama is not None :
        query += f"nama=?, "
        colValue.append(nama)
    
    if deskripsi is not None :
        query += f"deskripsi=?, "
        colValue.append(deskripsi)
    
    query = query.rstrip(", ")
    
    colValue.append(id_furnitur)
    query += " WHERE id_furnitur = ?"

    cursor.execute(query, colValue)

def deleteFurnitur(id_furnitur, cursor=None):
    query  = '''UPDATE Furnitur SET is_active = 0 WHERE id_furnitur = ?'''

    cursor.execute(query, (id_furnitur,))

def getAllFurnitur(cursor=None):
    query = '''SELECT id_furnitur, nama, deskripsi FROM Furnitur WHERE is_active = 1'''

    queryResult = cursor.execute(query)

    furnitur = queryResult.fetchall()

    return furnitur

def getDetailFurniturById(id_furnitur, cursor=None):
    query = '''
        SELECT 
            f.id_furnitur,
            f.nama as nama_furnitur,
            f.deskripsi,
            bf.id_bagian_furnitur,
            bf.nama AS nama_bagian_furnitur,
            bf.panjang,
            bf.lebar,
            bf.tinggi,
            w.id_warna,
            w.nama AS nama_warna,
            m.id_material,
            m.nama AS nama_material,
            dbf.harga,
            dbf.stok
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
            f.id_furnitur = ?;
    '''

    queryResult = cursor.execute(query, (id_furnitur,))

    detailFurnitur = queryResult.fetchall()

    if detailFurnitur is None : 
        raise Exception("Furnitur tidak ditemukan")

    columnNames = [column[0] for column in cursor.description]

    detailFurniturList = []
    for i in range(0, len(detailFurnitur)) :
        detailFurniturDict = {}
        for j in range(0, len(columnNames)) :
            detailFurniturDict[columnNames[j]] = detailFurnitur[i][j]
        detailFurniturList.append(detailFurniturDict)

    

    return detailFurniturList





