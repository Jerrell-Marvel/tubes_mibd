from view.furnitur import furniturView
from view.detailFurnitur import detailFurniturView
from view.register import registerView
from view.login import loginView
import pyodbc

from connectDB import conn

from view.home import homeView

# from services import furnitur, transaksi

# from services.Pengguna import insertPengguna


from executeQuery import execute_query

# from Controller.transaksi import melakukanTransaksi


# buat cursor dari connection
mainCursor = conn.cursor()


loggedInUserInfo = None
a = None
test = None


def main():

    userInput = homeView()

    if userInput == 1:
        userData = loginView()
        loggedInUserInfo = userData

        userRole = loggedInUserInfo["role"]
        if userRole == "pelanggan":
            furniturView()
        elif userRole == "pemilik":
            print("view pemilik")

        print(loggedInUserInfo)
    elif userInput == 2:
        userData = registerView()
        loggedInUserInfo = {"role": "pelanggan", **userData}

    elif userInput == 3:
        furniturView()


main()

# a = cursor.execute("SELECT 5").fetchone()[0]
# b = cursor.execute("SELECT 6").fetchone()[0]

# no transaction
# d = execute_query(furnitur.insertFurnitur, "lemari baju 555dsfsdf5", "lemari baju bagus","wwwww")

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

# execute_query(furnitur.insertFurnitur, "lemari bagus", "desk lemari")

# execute_query(furnitur.deleteFurnitur, 1)

# execute_query(furnitur.updateFurnitur,  1, nama="test", deskripsi="asalsdfsf", cursor=mainCursor)
# print(a)


# idPengguna = 3
# idFurnitur = 1

# data = [{"id_bagian_furnitur": 1, "id_warna": 1, "id_material": 1, "kuantitas": 5}, {
#     "id_bagian_furnitur": 2, "id_warna": 1, "id_material": 1, "kuantitas": 4}]

# execute_query(transaksi.insertManyTransaksiBagianFurnitur, 10, data)

# melakukanTransaksi(idPengguna, idFurnitur, data)

# from controller import pengguna as penggunaController

# try:
#     dataP = penggunaController.register("asep4", "asep4@gmail.com", "asep nama", "12345", "0887883", "jalan jalan", "babakan ciparay")
#     print(dataP)
# except Exception as e:
#     print(e)
#     print("here")
