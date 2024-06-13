from view.furnitur import furniturView
from view.transaksiPengguna import transaksiPenggunaView
from controller.pengguna import updatePengguna
from controller import pengguna as penggunaController


def homeView():
    print("Selamat datang di toko Furnitur Kapi")

    print("1. Login")
    print("2. Register")

    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    while (userInput != 1 and userInput != 2):
        print()
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    return userInput


def loggedInHomeView(loggedInUserInfo):
    isLogin = True
    while (isLogin == True):
        print()
        print("List aksi")
        print("1. Lihat furnitur")
        print("2. Lihat history transaksi")
        print("3. Lihat profil")
        print("4. Log out")

        userInput = int(input("Pilih aksi yang ingin dilakukan : "))
        while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4):
            print("Opsi yang dimasukkan tidak valid")
            userInput = int(input("Pilih aksi yang ingin dilakukan : "))

        if userInput == 1:
            furniturView(loggedInUserInfo)
        elif userInput == 2:
            transaksiPenggunaView(loggedInUserInfo)
        elif userInput == 3:
            userDataDetail = penggunaController.getPenggunaByUsername(loggedInUserInfo["username"])
            print()
            print("Profil pengguna")
            print()
            print(f'ID_Pengguna : {userDataDetail["id_pengguna"]}')
            print(f'Username : {userDataDetail["username"]}')
            print(f'Password : {userDataDetail["password"]}')
            print(f'Role : {userDataDetail["role"]}')
            print(f'Nama : {userDataDetail["nama"]}')
            print(f'Alamat : {userDataDetail["alamat"]}')
            print(f'Nama Kelurahan : {userDataDetail["nama_kelurahan"]}')
            print(f'Nama Kecamatan : {userDataDetail["nama_kecamatan"]}')
            print()

            print("List aksi")
            print("1. Ubah profil")
            print("2. Kembali ke halaman utama")

            userInput = int(input("Pilih aksi yang ingin dilakukan: "))
            if (userInput == 1):
                nama = input(
                    f'Masukkan nama({userDataDetail["nama"]}): ') or userDataDetail["nama"]
                nomorTelepon = input(
                    f'Masukkan nomor telepon({userDataDetail["nomor_telepon"]}): ') or userDataDetail["nomor_telepon"]
                email = input(
                    f'Masukkan email({userDataDetail["email"]}): ') or userDataDetail["email"]
                alamat = input(
                    f'Masukkan alamat({userDataDetail["alamat"]}): ') or userDataDetail["alamat"]
                namaKelurahan = input(
                    f'Masukkan nama kelurahan({userDataDetail["nama_kelurahan"]}): ') or userDataDetail["nama_kelurahan"]

                updatePengguna(
                    userDataDetail["id_pengguna"], nama, nomorTelepon, email, alamat, namaKelurahan)
                
            elif (userInput == 2):
                print()
        elif userInput == 4:
            print()
            isLogin = False
            return
