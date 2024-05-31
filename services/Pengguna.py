from connectDB import conn

def insertPengguna(username, email, nama, password, nomor_telepon, alamat, id_kelurahan, cursor=None):
    query = '''
        INSERT INTO Pengguna (username, email, nama, password, nomor_telepon, alamat, id_kelurahan)
        VALUES
        (?, ?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(query, (username, email, nama, password, nomor_telepon, alamat, id_kelurahan))