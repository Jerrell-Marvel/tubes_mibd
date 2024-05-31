from connectDB import conn

def insertFurnitur(nama, deskripsi, url_foto_display, cursor=None):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi, url_foto_display)
        VALUES
        (?, ?, ?);
    '''
    cursor.execute(query, (nama, deskripsi, url_foto_display))


def updateFurnitur(id_furnitur, nama=None, deskripsi=None, url_foto_display=None, cursor=None):
    query = '''UPDATE Furnitur SET '''

    colValue = []
    if nama is not None :
        query += f"nama=?, "
        colValue.append(nama)
    
    if deskripsi is not None :
        query += f"deskripsi=?, "
        colValue.append(deskripsi)

    if url_foto_display is not None :
        query += f"url_foto_display=?"
        colValue.append(url_foto_display)
    
    query = query.rstrip(", ")
    
    colValue.append(id_furnitur)
    query += " WHERE id_furnitur = ?"

    cursor.execute(query, colValue)




