from controller import furnitur as furniturController


def detailFurniturView(id_furnitur):
    print("Detail Furnitur : ")
    print()

    detailFurnitur = furniturController.getDetailFurnitur(id_furnitur)

    print("Nama furnitur: ", detailFurnitur[0]["nama_furnitur"])
    print("Deskripsi: ", detailFurnitur[0]["deskripsi"])

    print()

    print("Nama bagian furnitur: ")
    for i in range(0, len(detailFurnitur)):
        print(str(i + 1) + ".",
              detailFurnitur[i]["nama_bagian_furnitur"], detailFurnitur[i]["nama_material"], detailFurnitur[i]["nama_warna"], ", harga:", float(detailFurnitur[i]["harga"]), ", stok:", detailFurnitur[i]["stok"], ", panjang:", detailFurnitur[i]["panjang"], ", lebar:", detailFurnitur[i]["lebar"], ", tinggi:", detailFurnitur[0]["tinggi"])

    # print(detailFurnitur)
