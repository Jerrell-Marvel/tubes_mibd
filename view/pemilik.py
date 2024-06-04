from controller.transaksi import getTransaksiByDateRange as getTransaksiByDateRangeController
from controller import furnitur as furniturController


def pemilikView():
  print()
  print("List aksi")
  print("1. Update detail furnitur dan bagian furnitur ")
  print("2. Ubah harga bagian furnitur")
  print("3. Tampilkan laporan penjualan transaksi")
  
  userInput = int(input("Pilih aksi yang ingin dilakukan : "))
  

  if(userInput == 1):
    print()
  elif(userInput == 2):
    try:
      furniturList = furniturController.getAllFurnitur()
      
      print()
      for furnitur in furniturList:
        print(f'{furnitur["id_furnitur"]} \t{furnitur["nama"]}')
      
      print()
      idFurnitur = input("Masukkan id furnitur yang ingin diubah : ")
      bagianFurniturList = furniturController.getDetailFurnitur(idFurnitur)
      
      for bagianFurnitur in bagianFurniturList:
        print(f'Id bagian furnitur : {bagianFurnitur["id_bagian_Furnitur"]}')
        print(f'Nama : {bagianFurnitur["nama_bagian_furnitur"]}')
        print(f'Id warna : {bagianFurnitur["id_warna"]}')
        print(f'Warna : {bagianFurnitur["nama_warna"]}')
        print(f'Id material : {bagianFurnitur["id_material"]}')
        print(f'Material : {bagianFurnitur["nama_material"]}')
        print("------------------------------------------------")
        
      print()
      print("Masukkan bagian furnitur yang ingin diubah  ")
      idBagianFurnitur = input("Id bagian furnitur : ")
      idWarna = input("Id warna : ")
      idMaterial = input("Id material : ")
      dataBagianFurniturDict = furniturController.getDetailFurnitur(idFurnitur,id_bagian_furnitur=idBagianFurnitur, id_warna=idWarna, id_material=idMaterial)[0]
      
      updatedNama = input(f'Nama({dataBagianFurniturDict["nama_bagian_furnitur"]}) : ')
      updatedPanjang = input(f'Panjang({dataBagianFurniturDict["panjang"]}) : ')
      updatedLebar = input(f'Lebar({dataBagianFurniturDict["lebar"]}) : ')
      updatedTinggi = input(f'Tinggi({dataBagianFurniturDict["tinggi"]}) : ')
      updatedHarga = input(f'Harga({dataBagianFurniturDict["harga"]}) : ')
      updatedStok = input(f'Stok({dataBagianFurniturDict["stok"]}) : ')
      
      furniturController.updateBagianFurnitur(id_bagian_furnitur=idBagianFurnitur,id_warna=idWarna,id_material=idMaterial,nama_bagian_furnitur=updatedNama, panjang=updatedPanjang, lebar=updatedLebar,tinggi=updatedTinggi,harga=updatedHarga, stok=updatedStok)
      
    except Exception as e:
      print(e)
  elif(userInput == 3):
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
      
      pemilikView()
    except Exception as e:
      print(e)
  elif(userInput == 4):
    print()

