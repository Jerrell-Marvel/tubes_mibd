from view.furnitur import furniturView
from view.transaksiPengguna import transaksiPenggunaView
from controller.pengguna import updatePengguna


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
            print()
            print("Profil pengguna")
            print()
            print(f'ID_Pengguna : {loggedInUserInfo["id_pengguna"]}')
            print(f'Username : {loggedInUserInfo["username"]}')
            print(f'Password : {loggedInUserInfo["password"]}')
            print(f'Role : {loggedInUserInfo["role"]}')
            print(f'Nama : {loggedInUserInfo["nama"]}')
            print(f'Alamat : {loggedInUserInfo["alamat"]}')
            print(f'Nama Kelurahan : {loggedInUserInfo["nama_kelurahan"]}')
            print(f'Nama Kecamatan : {loggedInUserInfo["nama_kecamatan"]}')
            print()

            print("List aksi")
            print("1. Ubah profil")
            print("2. Kembali ke halaman utama")

            userInput = int(input("Pilih aksi yang ingin dilakukan: "))
            if (userInput == 1):
                nama = input(
                    f'Masukkan nama({loggedInUserInfo["nama"]}): ') or loggedInUserInfo["nama"]
                nomorTelepon = input(
                    f'Masukkan nomor telepon({loggedInUserInfo["nomor_telepon"]}): ') or loggedInUserInfo["nomor_telepon"]
                email = input(
                    f'Masukkan email({loggedInUserInfo["email"]}): ') or loggedInUserInfo["email"]
                alamat = input(
                    f'Masukkan alamat({loggedInUserInfo["alamat"]}): ') or loggedInUserInfo["alamat"]
                namaKelurahan = input(
                    f'Masukkan nama kelurahan({loggedInUserInfo["nama_kelurahan"]}): ') or loggedInUserInfo["nama_kelurahan"]

                updatePengguna(
                    loggedInUserInfo["id_pengguna"], nama, nomorTelepon, email, alamat, namaKelurahan)
                isLogin = False
            elif (userInput == 2):
                print()
        elif userInput == 4:
            print()
            isLogin = False
            return
