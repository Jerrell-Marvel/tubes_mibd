from controller import transaksi as transaksiController
from view import home as homeView


def transaksiPenggunaView(loggedInUserInfo):
    try:
        
        id_pengguna = loggedInUserInfo['id_pengguna']
        
        transaksi = transaksiController.getTransaksiPengguna(id_pengguna)

        print()
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
                print( f"   - {namaBagianFurnitur} {material} {warna} x{kuantitas}")
                
            ctr += 1
            print("===========================================")

        # homeView.loggedInHomeView(loggedInUserInfo)

    except Exception as e:
        print(e)