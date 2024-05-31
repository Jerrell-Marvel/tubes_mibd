from connectDB import conn

def insertFurnitur(nama , deskripsi, url_foto_display, cursor=None):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi, url_foto_display)
        VALUES
        (?, ?, ?);
    '''
    cursor.execute(query, (nama, deskripsi, url_foto_display))

def insertBagianFurnitur(nama, panjang, lebar, tinggi, id_furnitur, cursor=None) :
    query = '''
        INSERT INTO Bagian_Furnitur (nama, panjang, lebar, tinggi, id_furnitur)
        VALUES
        (?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (nama, panjang, lebar, tinggi, id_furnitur))



