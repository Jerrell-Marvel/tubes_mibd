def insertMaterial(nama_material, cursor=None):
    query = '''
    INSERT INTO Material(nama)
    VALUES(?)
    '''

    cursor.execute(query, (nama_material))

def getMaterialByName(nama_material, cursor=None):
    query = '''SELECT id_material FROM Material WHERE LOWER(nama) = LOWER(?)'''

    queryResult = cursor.execute(query, (nama_material,))

    idMaterial = queryResult.fetchone()

    if idMaterial is None : 
        raise Exception("Material tidak ditemukan")
    
    return idMaterial[0]