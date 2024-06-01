def insertPengguna(username, email, nama, password, nomor_telepon, alamat, id_kelurahan, cursor=None):
    query = '''
        INSERT INTO Pengguna (username, email, nama, password, nomor_telepon, alamat, id_kelurahan)
        VALUES
        (?, ?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(query, (username, email, nama, password, nomor_telepon, alamat, id_kelurahan))
    
def getPenggunaByUsername(username,cursor):
    query = '''
        SELECT id_pengguna, username, password, role FROM Pengguna 
        WHERE LOWER(username) = LOWER(?) 
    '''
    pengguna = cursor.execute(query, (username)).fetchone()
    
    if(pengguna is None):
        raise Exception("Username dimasukkan tidak terdaftar!")
    
    dictPengguna = {
        "id_pengguna": pengguna[0],
        "username": pengguna[1],
        "password": pengguna[2],
        "role": pengguna[3],
    }
    
    return dictPengguna