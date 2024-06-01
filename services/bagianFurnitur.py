def insertBagianFurnitur(nama, panjang, lebar, tinggi, id_furnitur, cursor=None) :
    query = '''
        INSERT INTO Bagian_Furnitur (nama, panjang, lebar, tinggi, id_furnitur)
        VALUES
        (?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (nama, panjang, lebar, tinggi, id_furnitur))

def insertDetailBagianFurnitur(id_bagian_furnitur, id_warna, id_material, harga, stok, cursor=None):
    query = '''
        INSERT INTO Detail_Bagian_Furnitur(id_bagian_furnitur, id_warma, id_material, harga, stok)
        VALUES
        (?, ?, ?, ?, ?)
    '''

    cursor.execute(query, (id_bagian_furnitur, id_warna, id_material, harga, stok))

def updateBagianFurnitur(id_bagian_furnitur, nama=None, cursor=None):
    query = '''UPDATE Bagian_Furnitur SET '''

    if nama is not None :
        query += f"nama=?"
    
    query += " WHERE id_bagian_furnitur = ?"

    cursor.execute(query, (nama, id_bagian_furnitur))

def updateDetailBagianFurnitur(id_bagian_furnitur, harga=None, stok=None, cursor=None):
    query = '''UPDATE Detail_Bagian_Furnitur SET '''

    colValue = []
    if harga is not None :
        query += f"harga=?, "
        colValue.append(harga)
    
    if stok is not None :
        query += f"stok=?, "
        colValue.append(stok)

    query = query.rstrip(", ")
    
    colValue.append(id_bagian_furnitur)
    query += " WHERE id_bagian_furnitur = ?"

    cursor.execute(query, colValue)

def deleteBagianFurnitur(id_bagian_furnitur, cursor=None) :
    query  = '''UPDATE Bagian_Furnitur SET is_active = 0 WHERE id_bagian_furnitur = ?'''

    cursor.execute(query, (id_bagian_furnitur,))