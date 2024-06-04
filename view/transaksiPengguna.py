from controller import transaksi as transaksiController


def transaksiPenggunaView(id_pengguna) : 

    try : 
        transaksi = transaksiController.getTransaksiPengguna(id_pengguna)

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
    except Exception as e :
        print(e)


