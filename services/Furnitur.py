def createFurnitur(nama , deskripsi, url_foto_display):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi, url_foto_display)
        VALUES
        (?, ?, ?);
    '''

