import pyodbc

from connectDB import conn

from services import furnitur

from executeQuery import execute_query


# buat cursor dari connection
cursor = conn.cursor()

a = cursor.execute("SELECT 5").fetchone()[0]
b = cursor.execute("SELECT 6").fetchone()[0]

# no transaction
# d = execute_query(Furnitur.insertFurnitur, ("lemari baju", "lemari baju bagus","wwwww"))

# with transaction
# try :
#     mainCursor = conn.cursor()
#     e = execute_query(Furnitur.insertFurnitur, ("lemari baju 4", "lemari baju bagus","wwwww"), cursor=mainCursor)
#     f = execute_query(Furnitur.insertFurnitur, ("lemari baju 5", "lemari baju bagus","wwwww"),cursor=mainCursor)
#     raise ValueError("LOLOLOL")
#     mainCursor.commit()
# except ValueError as e: 
#     print(e)
#     mainCursor.rollback()
# finally :
#     mainCursor.close()


execute_query(furnitur.updateFurnitur, (1,), nama="test", deskripsi="asalsdfsf")
# print(a)