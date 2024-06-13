
def insertPengguna(username, email, nama, password, nomor_telepon, alamat, id_kelurahan, cursor=None):
    query = '''
        INSERT INTO Pengguna (username, email, nama, password, nomor_telepon, alamat, id_kelurahan)
        OUTPUT INSERTED.id_pengguna, INSERTED.username, INSERTED.nama, INSERTED.alamat
        VALUES 
        (?, ?, ?, ?, ?, ?, ?);
    '''
    queryResult = cursor.execute(
        query, (username, email, nama, password, nomor_telepon, alamat, id_kelurahan))

    dataPengguna = queryResult.fetchone()

    return {
        "id_pengguna": dataPengguna[0],
        "username": dataPengguna[1],
        "nama": dataPengguna[2],
        "alamat": dataPengguna[3]
    }


def getPenggunaByUsername(username, cursor=None):
    query = '''
        SELECT p.id_pengguna, p.username, p.password, p.role, p.nama, p.alamat, k.nama, k.id_kelurahan, kec.nama, kec.id_kecamatan, p.nomor_telepon, p.email FROM Pengguna p INNER JOIN Kelurahan k ON p.id_kelurahan = k.id_kelurahan INNER JOIN Kecamatan kec ON k.id_kecamatan = kec.id_kecamatan
        WHERE LOWER(username) = LOWER(?) 
    '''
    pengguna = cursor.execute(query, (username)).fetchone()

    if (pengguna is None):
        raise Exception("Username tidak terdaftar!")

    dictPengguna = {
        "id_pengguna": pengguna[0],
        "username": pengguna[1],
        "password": pengguna[2],
        "role": pengguna[3],
        "nama": pengguna[4],
        "alamat": pengguna[5],
        "nama_kelurahan": pengguna[6],
        "id_kelurahan": pengguna[7],
        "nama_kecamatan": pengguna[8],
        "id_kecamatan": pengguna[9],
        "nomor_telepon": pengguna[10],
        "email": pengguna[11]
    }

    return dictPengguna


def updatePengguna(id_pengguna, nama, nomor_telepon, email, alamat, id_kelurahan, cursor=None):
    query = '''
        UPDATE Pengguna 
        SET nama = ?, nomor_telepon = ?, email = ?, alamat = ?, id_kelurahan = ?
        WHERE id_pengguna = ?'''

    queryResult = cursor.execute(
        query, (nama, nomor_telepon, email, alamat, id_kelurahan, id_pengguna))
