from controller import furnitur as furniturController

def furniturView():
    print("List furnitur : ")

    furnitur = furniturController.getAllFurnitur()
