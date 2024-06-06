from controller import furnitur as furniturController 

def deleteFurnitureView():
    print("List seluruh furnitur")    
    furniturList = furniturController.getAllFurnitur()
    
    ctr = 1
    print()
    for furnitur in furniturList:
        print(f'{ctr}.  {furnitur[1]}')
        ctr +=1
    
    print()
    rowFurnitur = input("Masukkan baris furnitur yang ingin dihapus : ")
    
    furniturController.deleteFurnitur(furniturList[rowFurnitur - 1][0])
    
    print("Berhasil menghapus data furnitur!")
    print()
    