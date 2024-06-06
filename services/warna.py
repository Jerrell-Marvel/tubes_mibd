def insertWarna(nama_warna, cursor=None):
    query = '''
    INSERT INTO Warna(nama)
    VALUES
    (?)
    '''

    cursor.execute(query, (nama_warna))

def getWarnaByName(nama_warna, cursor=None):
    query = '''SELECT id_warna FROM Warna WHERE LOWER(nama) = LOWER(?)'''

    queryResult = cursor.execute(query, (nama_warna,))

    

    idWarna = queryResult.fetchone()

    if idWarna is None : 
        raise Exception("Warna tidak ditemukan")

    return idWarna[0]