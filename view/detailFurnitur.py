from controller import furnitur as furniturController
from view import home as homeView
from controller import transaksi as transaksiController

def detailFurniturView(id_furnitur, loggedInUserInfo):
    print()
    print("Detail Furnitur : ")

    detailFurnitur = furniturController.getDetailFurnitur(id_furnitur)

    print("Nama furnitur: ", detailFurnitur[0]["nama_furnitur"])
    print("Deskripsi: ", detailFurnitur[0]["deskripsi"])

    print()

    print("Nama bagian furnitur: ")
    for i in range(0, len(detailFurnitur)):
        detail = detailFurnitur[i]

        print(str(i + 1) + ".", end=" ")
        print(detail["nama_bagian_furnitur"])
        panjang = detail['panjang']
        lebar = detail['lebar']
        tinggi = detail['tinggi']
        print(f"Dimensi : {panjang} x {lebar} x {tinggi}")
        print(f"Warna : {detail['nama_warna']}")
        print(f"Material : {detail['nama_material']}")
        print(f"Harga : {float(detail['harga'])}")
        print(f"Stok : {detail['stok']}")
        print("========================")

    print("1. Lakukan pemesanan")
    print("2. Kembali ke halaman utama")
    userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    while(userInput != 1 and userInput != 2):
        print()
        print("Opsi yang dimasukkan tidak valid")
        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

    if(userInput == 1):
        nomorBagianFurnitur = int(input("Pilih bagian furnitur : "))
        while(nomorBagianFurnitur < 1 or nomorBagianFurnitur > len(detailFurnitur)):
            print()
            print("Opsi yang dimasukkan tidak valid")
            nomorBagianFurnitur = int(input("Pilih bagian furnitur : "))
        kuantitas = int(input("Masukkan kuantitas : "))
        detail = detailFurnitur[nomorBagianFurnitur - 1]
        listDetail = [{
            'id_bagian_furnitur' : detail['id_bagian_furnitur'],
            'id_warna' : detail['id_warna'],
            'id_material' : detail['id_material'],
            'kuantitas' : kuantitas
        }]
        transaksiController.melakukanTransaksi(loggedInUserInfo['id_pengguna'], id_furnitur=id_furnitur, transaksiBagianFurniturData=listDetail)

        homeView.loggedInHomeView(loggedInUserInfo)
    elif(userInput == 2):
        homeView.loggedInHomeView(loggedInUserInfo)
        # print(str(i + 1) + ".",
        #       detailFurnitur[i]["nama_bagian_furnitur"], detailFurnitur[i]["nama_material"], detailFurnitur[i]["nama_warna"], ", harga:", float(detailFurnitur[i]["harga"]), ", stok:", detailFurnitur[i]["stok"], ", panjang:", detailFurnitur[i]["panjang"], ", lebar:", detailFurnitur[i]["lebar"], ", tinggi:", detailFurnitur[0]["tinggi"])

    # print(detailFurnitur)
