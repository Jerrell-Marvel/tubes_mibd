def getKelurahan(nama_kelurahan, cursor = None):
    query = '''
    SELECT id_kelurahan 
    FROM Kelurahan
    WHERE LOWER(nama) = LOWER(?)
    '''

    kelurahan = cursor.execute(query,(nama_kelurahan)).fetchone()

    if kelurahan is None :
        raise Exception("Kelurahan tidak terdaftar!")
    
    return {"id_kelurahan" : kelurahan[0]}