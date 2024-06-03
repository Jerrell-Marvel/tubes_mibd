
"OUTPUT INSERTED.id_pengguna, INSERTED.username, INSERTED.nama"

def insertPengguna(username, email, nama, password, nomor_telepon, alamat, id_kelurahan, cursor=None):
    query = '''
        INSERT INTO Pengguna (username, email, nama, password, nomor_telepon, alamat, id_kelurahan)
        OUTPUT INSERTED.id_pengguna, INSERTED.username, INSERTED.nama, INSERTED.alamat
        VALUES 
        (?, ?, ?, ?, ?, ?, ?);
    '''
    queryResult = cursor.execute(query, (username, email, nama, password, nomor_telepon, alamat, id_kelurahan))

    dataPengguna = queryResult.fetchone()

    return {
        "id_pengguna" : dataPengguna[0],
        "username" : dataPengguna[1],
        "nama" : dataPengguna[2],
        "alamat" : dataPengguna[3]
    }
    
def getPenggunaByUsername(username,cursor):
    query = '''
        SELECT id_pengguna, username, password, role, nama, alamat FROM Pengguna 
        WHERE LOWER(username) = LOWER(?) 
    '''
    pengguna = cursor.execute(query, (username)).fetchone()
    
    if(pengguna is None):
        raise Exception("Username tidak terdaftar!")
    
    dictPengguna = {
        "id_pengguna": pengguna[0],
        "username": pengguna[1],
        "password": pengguna[2],
        "role": pengguna[3],
        "nama": pengguna[4],
        "alamat" : pengguna[5]
    }
    
    return dictPengguna