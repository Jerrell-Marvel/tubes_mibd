from controller import pengguna as penggunaController 
from view.home import homeView

def registerView() : 
    email = input("Email : ")
    nama = input("Nama : ")
    noTelp = input("No telp : ")
    alamat = input("Alamat : ")
    kelurahan = input("Kelurahan : ")
    username = input("Username : ")
    password = input("Password : ")

    try : 
        dataPengguna = penggunaController.register(username, email, nama, password, noTelp, alamat, kelurahan)
        
        return dataPengguna

    except Exception as e : 
        print(e)
        print("Terjadi kesalahan saat registrasi")
        return None

