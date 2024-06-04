from view.furnitur import furniturView
from view.transaksiPengguna import transaksiPenggunaView

def homeView ():
    print("Selamat datang di toko Furnitur Kapi")

    print("1. Login")
    print("2. Register")

    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    while(userInput != 1 and userInput != 2):
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    return userInput

def loggedInHomeView(loggedInUserInfo) : 
    isLogin = True
    while(isLogin == True):
        print()
        print("List aksi")
        print("1. Lihat furnitur")
        print("2. Lihat history transaksi")
        print("3. Log out")

        userInput = int(input("Pilih aksi yang ingin dilakukan : "))
        while(userInput != 1 and userInput != 2 and userInput != 3):
            print("Opsi yang dimasukkan tidak valid")
            userInput = int(input("Pilih aksi yang ingin dilakukan : "))
        
        if userInput == 1 :
            furniturView(loggedInUserInfo)
        elif userInput == 2 :
            transaksiPenggunaView(loggedInUserInfo)
        elif userInput == 3 :
            print()
            isLogin = False