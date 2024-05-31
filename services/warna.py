def insertWarna(nama_warna, cursor=None):
    query = '''
    INSERT INTO Warna(nama)
    VALUES
    (?)
    '''

    cursor.execute(query, (nama_warna))