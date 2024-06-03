
def insertFurnitur(nama, deskripsi, cursor=None):
    query = '''
        INSERT INTO Furnitur (nama, deskripsi)
        VALUES
        (?, ?);
    '''
    cursor.execute(query, (nama, deskripsi))


def updateFurnitur(id_furnitur, nama=None, deskripsi=None, cursor=None):
    query = '''UPDATE Furnitur SET '''

    colValue = []
    if nama is not None :
        query += f"nama=?, "
        colValue.append(nama)
    
    if deskripsi is not None :
        query += f"deskripsi=?, "
        colValue.append(deskripsi)
    
    query = query.rstrip(", ")
    
    colValue.append(id_furnitur)
    query += " WHERE id_furnitur = ?"

    cursor.execute(query, colValue)

def deleteFurnitur(id_furnitur, cursor=None):
    query  = '''UPDATE Furnitur SET is_active = 0 WHERE id_furnitur = ?'''

    cursor.execute(query, (id_furnitur,))

def getAllFurnitur(cursor=None):
    query = '''SELECT nama FROM Furnitur WHERE is_active = 1'''

    queryResult = cursor.execute(query)

    furnitur = queryResult.fetchall()

    print(furnitur)

    return furnitur





