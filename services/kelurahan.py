def getKelurahan(nama_kelurahan, cursor = None):
    query = '''
    SELECT id_kelurahan 
    FROM Kelurahan
    WHERE LOWER(nama) = LOWER(?)
    '''

    queryResult = cursor.execute(query,(nama_kelurahan))

    if queryResult is None :
        raise Exception("Kelurahan tidak terdaftar!")
    
    kelurahan = queryResult.fetchone()
    
    return {"id_kelurahan" : kelurahan[0]}