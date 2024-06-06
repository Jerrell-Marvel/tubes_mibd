from controller import furnitur as furniturController 

def deleteBagianFurnitureView():
    print("List seluruh furnitur")
    furniturList = furniturController.getAllFurnitur()
    
    ctr = 1
    print()
    for furnitur in furniturList:
        print(f'{ctr}.  {furnitur[1]}')
        ctr +=1
    
    print()
    rowFurnitur = int(input("Masukkan baris furnitur yang ingin diubah : "))
    idxFurnitur = rowFurnitur - 1
    bagianFurniturList = furniturController.getDetailFurnitur(furniturList[idxFurnitur][0])
    
    ctr = 1
    for bagianFurnitur in bagianFurniturList:
        print(f'Bagian Furnitur Nomor : {ctr}')
        print(f'Nama : {bagianFurnitur["nama_bagian_furnitur"]}')
        print(f'Warna : {bagianFurnitur["nama_warna"]}')
        print(f'Material : {bagianFurnitur["nama_material"]}')
        print("------------------------------------------------")
        ctr += 1
    print()
    noBaris = int(input("Masukkan baris bagian furnitur yang ingin diubah : "))
    
    furniturController.deleteBagianFurnitur(bagianFurniturList[noBaris-1]["id_bagian_furnitur"])
    
    print("Berhasil menghapus bagian furnitur!")