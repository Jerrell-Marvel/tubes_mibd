from view.furnitur import furniturView

def homeView ():
    print("Selamat datang di toko Furnitur Kapi")

    print("1. Login")
    print("2. Register")

    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    while(userInput != 1 and userInput != 2):
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    return userInput

def loggedInHomeView() : 
    print("1. Lihat furnitur")
    print("2. Lihat transaksi")

    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    while(userInput != 1 and userInput != 2):
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    
    if userInput == 1 :
        furniturView()
    else :
        print("transaksi view")

    
