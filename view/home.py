
def homeView ():
    print("Selamat datang di toko Furnitur Kapi")

    print("1. Login")
    print("2. Register")
    print("3. Lihat furnitur")

    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    while(userInput != 1 and userInput != 2 and userInput != 3):
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    return userInput

    
