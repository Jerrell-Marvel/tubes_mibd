from controller import furnitur as furniturController

def detailFurnitur(id_furnitur):
    print("detail : ")

    detailFurnitur = furniturController.getDetailFurnitur(id_furnitur)

    print(detailFurnitur)