def getKelurahan(nama_kelurahan, cursor = None):
    query = '''
    SELECT id_kelurahan 
    FROM Kelurahan
    WHERE LOWER(nama) = LOWER(?)
    '''

    queryResult = cursor.execute(query,(nama_kelurahan))
    
    kelurahan = queryResult.fetchone()

    if kelurahan is None :
        raise Exception("Kelurahan tidak terdaftar!")

    
    return {"id_kelurahan" : kelurahan[0]}