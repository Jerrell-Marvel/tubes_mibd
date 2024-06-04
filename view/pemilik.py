from controller.transaksi import getTransaksiByDateRange as getTransaksiByDateRangeController


def pemilikView():
  print("1. Update detail furnitur dan bagian furnitur ")
  print("2. Ubah harga bagian furnitur")
  print("3. Tampilkan laporan penjualan transaksi")
  
  userInput = int(input("Pilih aksi yang ingin dilakukan : "))
  

  if(userInput == 1):
    print()
  elif(userInput == 2):
    print()
  elif(userInput == 3):
    try:
      startDate = input("Masukkan rentang awal transaksi(YYYYMMDD) :")
      endDate = input("Masukkan rentang akhir transaksi(YYYYMMDD) :")
      transaksiDict = getTransaksiByDateRangeController(startDate, endDate)

      transaksi = transaksiDict["transaksi"]
      totalPendapatan = transaksiDict["totalPendapatan"]

      print(f"Total pendapatan pada rentang {startDate} - {endDate}  :", totalPendapatan)
      
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
  elif(userInput == 4):
    print()

