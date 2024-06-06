from controller import furnitur as furniturController 

def updateFurnitureView():
    print("List seluruh furnitur")    
    furniturList = furniturController.getAllFurnitur()
    
    ctr = 1
    print()
    for furnitur in furniturList:
        print(f'{ctr}.  {furnitur[1]}')
        ctr +=1
    
    print()
    rowFurnitur = input("Masukkan baris furnitur yang ingin diubah : ")
    idxFurnitur = rowFurnitur - 1
    
    updatedNama = input(f'Nama({furniturList[idxFurnitur][1]}) : ') or furniturList[idxFurnitur][1]
    updatedDeskripsi = input(f'Deskripsi({furniturList[idxFurnitur][2]}) : ') or furniturList[idxFurnitur][2]
    
    furniturController.updateFurniture(furniturList[idxFurnitur][0],updatedNama,updatedDeskripsi)
    
    print("Berhasil mengubah data furnitur!")
    print()