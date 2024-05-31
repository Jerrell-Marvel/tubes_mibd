def insertMaterial(nama_material, cursor=None):
    query = '''
    INSERT INTO Material(nama)
    VALUES(?)
    '''

    cursor.execute(query, (nama_material))