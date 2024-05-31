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