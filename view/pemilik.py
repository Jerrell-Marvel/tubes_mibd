from controller.transaksi import getTransaksiByDateRange as getTransaksiByDateRangeController
from controller import furnitur as furniturController

from view.updateFurnitur import updateFurnitureView
from view.deleteFurnitur import deleteFurnitureView
from view.deleteBagianFurnitur import deleteBagianFurnitureView



def pemilikView():
    isLogin = True
    while (isLogin):
        print()
        print("List aksi")
        print("1. Tambahkan furnitur")
        print("2. Tambahkan bagian furnitur")
        print("3. Kelola furnitur")
        print("4. Kelola bagian furnitur")
        print("5. Hapus furnitur")
        print("6. Hapus bagian furnitur")
        print("7. Tampilkan laporan penjualan transaksi")
        print('8. Log Out')

        userInput = int(input("Pilih aksi yang ingin dilakukan : "))

        if (userInput == 1):
            namaFurnitur = input("Masukkan nama furnitur: ")
            deskripsiFurnitur = input("Masukkan deskripsi furnitur: ")
            tambahBagianFurnitur = 'Y'
            listBagianFurnitur = []
            while (tambahBagianFurnitur == 'Y'):

                namaBagianFurnitur = input("Masukkan nama bagian furnitur: ")
                panjangBagianFurnitur = input(
                    "Masukkan panjang bagian furnitur: ")
                lebarBagianFurnitur = input(
                    "Masukkan lebar bagian furnitur: ")
                tinggiBagianFurnitur = input(
                    "Masukkan tinggi bagian furnitur: ")

                tambahDetailBagianFurnitur = 'Y'
                listDetailBagianFurnitur = []
                while (tambahDetailBagianFurnitur == 'Y'):

                    warnaDetailBagianFurnitur = input(
                        "Masukkan warna detail bagian furnitur: ")
                    materialDetailBagianFurnitur = input(
                        "Masukkan material detail bagian furnitur: ")
                    hargaDetailBagianFurnitur = input(
                        "Masukkan harga detail bagian furnitur: ")
                    stokDetailBagianFurnitur = input(
                        "Masukkan stok detail bagian furnitur: ")
                    dictDetailBagianFurnitur = {
                        'warna': warnaDetailBagianFurnitur,
                        'material': materialDetailBagianFurnitur,
                        'harga': hargaDetailBagianFurnitur,
                        'stok': stokDetailBagianFurnitur
                    }
                    listDetailBagianFurnitur.append(dictDetailBagianFurnitur)
                    tambahDetailBagianFurnitur = input(
                        "Tambahkan detail bagian furnitur lainnya ? (Y/N) :")

                    if (tambahDetailBagianFurnitur == 'N'):
                        break

                dictBagianFurnitur = {
                    'nama': namaBagianFurnitur,
                    'panjang': panjangBagianFurnitur,
                    'lebar': lebarBagianFurnitur,
                    'tinggi': tinggiBagianFurnitur,
                    'detailBagianFurnitur': listDetailBagianFurnitur
                }

                listBagianFurnitur.append(dictBagianFurnitur)
                tambahBagianFurnitur = input(
                    "Tambahkan bagian furnitur lainnya ? (Y/N) :")
                # jika input tambahBagianFurnitur salah
                while (tambahBagianFurnitur != 'N' and tambahBagianFurnitur != 'Y'):
                    print("Opsi yang dimasukkan tidak valid")
                    print()
                    tambahBagianFurnitur = input(
                        "Tambahkan bagian furnitur lainnya ? (Y/N) :")

                if (tambahBagianFurnitur == 'N'):
                    break
            print("METHOD INSERT FURNITUR")
            try:
              furniturController.insertFurnitur(namaFurnitur, deskripsiFurnitur, listBagianFurnitur)
            except Exception as e :
              print(e)
        elif (userInput == 2):
            print("List seluruh furnitur")
            furniturList = furniturController.getAllFurnitur()

            ctr = 1
            print()
            for furnitur in furniturList:
                print(f'{ctr}.  {furnitur[1]}')
                ctr +=1

            print()
            rowFurnitur = int(input("Masukkan baris furnitur yang ingin diubah : "))
            idFurnitur = rowFurnitur - 1
    
            tambahBagianFurnitur = 'Y'
            listBagianFurnitur = []
            while (tambahBagianFurnitur == 'Y'):

                namaBagianFurnitur = input("Masukkan nama bagian furnitur: ")
                panjangBagianFurnitur = input(
                    "Masukkan panjang bagian furnitur: ")
                lebarBagianFurnitur = input(
                    "Masukkan lebar bagian furnitur: ")
                tinggiBagianFurnitur = input(
                    "Masukkan tinggi bagian furnitur: ")

                tambahDetailBagianFurnitur = 'Y'
                listDetailBagianFurnitur = []
                while (tambahDetailBagianFurnitur == 'Y'):

                    warnaDetailBagianFurnitur = input(
                        "Masukkan warna detail bagian furnitur: ")
                    materialDetailBagianFurnitur = input(
                        "Masukkan material detail bagian furnitur: ")
                    hargaDetailBagianFurnitur = input(
                        "Masukkan harga detail bagian furnitur: ")
                    stokDetailBagianFurnitur = input(
                        "Masukkan stok detail bagian furnitur: ")
                    dictDetailBagianFurnitur = {
                        'warna': warnaDetailBagianFurnitur,
                        'material': materialDetailBagianFurnitur,
                        'harga': hargaDetailBagianFurnitur,
                        'stok': stokDetailBagianFurnitur
                    }


                    listDetailBagianFurnitur.append(dictDetailBagianFurnitur)
                    tambahDetailBagianFurnitur = input(
                        "Tambahkan detail bagian furnitur lainnya ? (Y/N) :")

                    if (tambahDetailBagianFurnitur == 'N'):
                        break

                dictBagianFurnitur = {
                    'nama': namaBagianFurnitur,
                    'panjang': panjangBagianFurnitur,
                    'lebar': lebarBagianFurnitur,
                    'tinggi': tinggiBagianFurnitur,
                    'detailBagianFurnitur': listDetailBagianFurnitur
                }

                listBagianFurnitur.append(dictBagianFurnitur)
                tambahBagianFurnitur = input(
                    "Tambahkan bagian furnitur lainnya ? (Y/N) :")
                # jika input tambahBagianFurnitur salah
                while (tambahBagianFurnitur != 'N' and tambahBagianFurnitur != 'Y'):
                    print("Opsi yang dimasukkan tidak valid")
                    print()
                    tambahBagianFurnitur = input(
                        "Tambahkan bagian furnitur lainnya ? (Y/N) :")

                if (tambahBagianFurnitur == 'N'):
                    break
            print("ID FURNITUR , METHOD INSERT BAGIAN FURNITUR")
            furniturController.insertBagianFurnitur(idFurnitur, listBagianFurnitur)

            
        elif (userInput == 3):
            # print("Kelola furnitur")
            updateFurnitureView()
        elif (userInput == 4):
            try:
                print("List seluruh furnitur")
                furniturList = furniturController.getAllFurnitur()

                ctr = 1
                print()
                for furnitur in furniturList:
                    print(f'{ctr}.  {furnitur[1]}')
                    ctr +=1

                print()
                
                rowFurnitur = int(input("Masukkan baris furnitur yang ingin diubah : "))
                idFurnitur = rowFurnitur - 1
    

                bagianFurniturList = furniturController.getDetailFurnitur(
                    idFurnitur)

                ctr = 1
                for bagianFurnitur in bagianFurniturList:
                    print(f'Bagian Furnitur Nomor : {ctr}')
                    print(f'Nama : {bagianFurnitur["nama_bagian_furnitur"]}')
                    print(f'Warna : {bagianFurnitur["nama_warna"]}')
                    print(f'Material : {bagianFurnitur["nama_material"]}')
                    print("------------------------------------------------")
                    ctr += 1
                print()

                noBaris = int(
                    input("Masukkan nomor bagian furnitur yang ingin diubah : "))

                dataBagianFurniturDict = bagianFurniturList[noBaris-1]
                # dataBagianFurniturDict = furniturController.getDetailFurnitur(idFurnitur,id_bagian_furnitur=bagianFurnitur{"id_bagian_furnitur"}, id_warna=idWarna, id_material=idMaterial)[0]

                updatedNama = input(
                    f'Nama({dataBagianFurniturDict["nama_bagian_furnitur"]}) : ') or dataBagianFurniturDict["nama_bagian_furnitur"]
                updatedPanjang = input(
                    f'Panjang({dataBagianFurniturDict["panjang"]}) : ') or dataBagianFurniturDict["panjang"]
                updatedLebar = input(
                    f'Lebar({dataBagianFurniturDict["lebar"]}) : ') or dataBagianFurniturDict["lebar"]
                updatedTinggi = input(
                    f'Tinggi({dataBagianFurniturDict["tinggi"]}) : ') or dataBagianFurniturDict["tinggi"]
                updatedHarga = input(
                    f'Harga({dataBagianFurniturDict["harga"]}) : ') or dataBagianFurniturDict["harga"]
                updatedStok = input(
                    f'Stok({dataBagianFurniturDict["stok"]}) : ') or dataBagianFurniturDict["stok"]

                furniturController.updateBagianFurnitur(id_bagian_furnitur=dataBagianFurniturDict['id_bagian_furnitur'], id_warna=dataBagianFurniturDict['id_warna'], id_material=dataBagianFurniturDict[
                                                        'id_material'], nama_bagian_furnitur=updatedNama, panjang=updatedPanjang, lebar=updatedLebar, tinggi=updatedTinggi, harga=updatedHarga, stok=updatedStok)

            except Exception as e:
                print(e)
        elif (userInput == 5):
            deleteFurnitureView()
        elif (userInput == 6):
            deleteBagianFurnitureView()
        elif (userInput == 7):
            try:
                startDate = input(
                    "Masukkan rentang awal transaksi(YYYYMMDD) :")
                endDate = input("Masukkan rentang akhir transaksi(YYYYMMDD) :")
                transaksiDict = getTransaksiByDateRangeController(
                    startDate, endDate)

                transaksi = transaksiDict["transaksi"]
                totalPendapatan = transaksiDict["totalPendapatan"]
                print()
                print(
                    f"Total pendapatan pada rentang {startDate} - {endDate}  :", totalPendapatan)
                print()
                # for i in range(0, len(transaksi)):
                #   # print(str((i+1))+ ".", end="")
                #   print(transaksi[i])
                #   print("=======================")
                # print(transaksi)
                print("List transaksi : ")
                ctr = 1
                for t in transaksi:
                    print(str(ctr) + ". ", end="")
                    print(t["listBagianFurnitur"][0]["nama_furnitur"])

                    for bagianFurnitur in t["listBagianFurnitur"]:
                        namaBagianFurnitur = bagianFurnitur["nama_bagian_furnitur"]
                        warna = bagianFurnitur["nama_warna"]
                        material = bagianFurnitur["nama_material"]
                        kuantitas = bagianFurnitur["kuantitas"]
                        print(
                            f"{namaBagianFurnitur} {material} {warna} x{kuantitas}")

                    print("===========================================")
                    ctr += 1

            except Exception as e:
                print(e)
        elif (userInput == 8):
            print()
            isLogin = False
