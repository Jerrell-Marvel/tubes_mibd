from controller.transaksi import getTransaksiByDateRange as getTransaksiByDateRangeController


def pemilikView():
  print("1. Update detail furnitur dan bagian furnitur ")
  print("2. Ubah harga bagian furnitur")
  print("3. Tampilkan laporan penjualan transaksi")
  print("4. Tampilkan laporan pendapatan transaksi")
  
  userInput = int(input("Pilih aksi yang ingin dilakukan : "))
  

  if(userInput == 1):
    print()
  elif(userInput == 2):
    print()
  elif(userInput == 3):
    try:
      startDate = input("Masukkan rentang awal transaksi(YYYYMMDD) :")
      endDate = input("Masukkan rentang akhir transaksi(YYYYMMDD) :")
      transaksi = getTransaksiByDateRangeController(startDate, endDate)
      
      for i in range(0, len(transaksi)):
        print(str((i+1))+ ".", end="")
        print(transaksi[i])
    except Exception as e:
      print(e)
  elif(userInput == 4):
    print()
