from controller.transaksi import getTransaksiByDateRange as getTransaksiByDateRangeController
from controller import furnitur as furniturController


def pemilikView():
  isLogin = True
  while(isLogin):
    print()
    print("List aksi")
    print("1. Update detail furnitur dan bagian furnitur ")
    print("2. Tampilkan laporan penjualan transaksi")
    print('3. Log Out')
    
    userInput = int(input("Pilih aksi yang ingin dilakukan : "))
    
    if(userInput == 1):
      try:
        furniturList = furniturController.getAllFurnitur()
        
        print()
        for furnitur in furniturList:
          print(f'{furnitur[0]} \t{furnitur[1]}')
        
        print()
        idFurnitur = input("Masukkan id furnitur yang ingin diubah : ")
        bagianFurniturList = furniturController.getDetailFurnitur(idFurnitur)
        
        ctr = 1
        for bagianFurnitur in bagianFurniturList:
          print(f'Bagian Furnitur Nomor : {ctr}')
          print(f'Nama : {bagianFurnitur["nama_bagian_furnitur"]}')
          print(f'Warna : {bagianFurnitur["nama_warna"]}')
          print(f'Material : {bagianFurnitur["nama_material"]}')
          print("------------------------------------------------")
          ctr += 1
        print()
        noBaris = int(input("Masukkan nomor bagian furnitur yang ingin diubah : "))

        dataBagianFurniturDict = bagianFurniturList[noBaris-1]
        # dataBagianFurniturDict = furniturController.getDetailFurnitur(idFurnitur,id_bagian_furnitur=bagianFurnitur{"id_bagian_furnitur"}, id_warna=idWarna, id_material=idMaterial)[0]
        
        updatedNama = input(f'Nama({dataBagianFurniturDict["nama_bagian_furnitur"]}) : ')
        updatedPanjang = input(f'Panjang({dataBagianFurniturDict["panjang"]}) : ')
        updatedLebar = input(f'Lebar({dataBagianFurniturDict["lebar"]}) : ')
        updatedTinggi = input(f'Tinggi({dataBagianFurniturDict["tinggi"]}) : ')
        updatedHarga = input(f'Harga({dataBagianFurniturDict["harga"]}) : ')
        updatedStok = input(f'Stok({dataBagianFurniturDict["stok"]}) : ')
        
        furniturController.updateBagianFurnitur(id_bagian_furnitur=dataBagianFurniturDict['id_bagian_furnitur'],id_warna=dataBagianFurniturDict['id_warna'],id_material=dataBagianFurniturDict['id_material'],nama_bagian_furnitur=updatedNama, panjang=updatedPanjang, lebar=updatedLebar,tinggi=updatedTinggi,harga=updatedHarga, stok=updatedStok)
        
      except Exception as e:
        print(e)
    elif(userInput == 2):
      try:
        startDate = input("Masukkan rentang awal transaksi(YYYYMMDD) :")
        endDate = input("Masukkan rentang akhir transaksi(YYYYMMDD) :")
        transaksiDict = getTransaksiByDateRangeController(startDate, endDate)

        transaksi = transaksiDict["transaksi"]
        totalPendapatan = transaksiDict["totalPendapatan"]
        print()
        print(f"Total pendapatan pada rentang {startDate} - {endDate}  :", totalPendapatan)
        print()
        # for i in range(0, len(transaksi)):
        #   # print(str((i+1))+ ".", end="")
        #   print(transaksi[i])
        #   print("=======================")
        # print(transaksi)
        print("List transaksi : ")
        ctr = 1
        for t in transaksi :
          print(str(ctr) + ". ", end="")
          print(t["listBagianFurnitur"][0]["nama_furnitur"])

          for bagianFurnitur in t["listBagianFurnitur"] :
            namaBagianFurnitur = bagianFurnitur["nama_bagian_furnitur"]
            warna = bagianFurnitur["nama_warna"]
            material = bagianFurnitur["nama_material"]
            kuantitas = bagianFurnitur["kuantitas"]
            print(f"{namaBagianFurnitur} {material} {warna} x{kuantitas}")
            
          print("===========================================")
          ctr+= 1
        

      except Exception as e:
        print(e)
    elif(userInput == 3):
      print()
      isLogin = False


