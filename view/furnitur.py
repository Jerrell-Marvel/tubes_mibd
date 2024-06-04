from controller import furnitur as furniturController
from view.detailFurnitur import detailFurniturView


def furniturView(loggedInUserInfo):
    print()
    print("List furnitur : ")

    furnitur = furniturController.getAllFurnitur()

    for i in range(0, len(furnitur)):
        row = furnitur[i]
        print(f"{i + 1}. ", end="")
        print(row[1])

    userInput = int(input("Lihat detail furnitur : "))

    while (userInput < 1 or userInput > len(furnitur)):
        print(f"Input tidak sesuai, masukkan angka 1-{len(furnitur)}")
        userInput = int(input("Lihat detail furnitur : "))

    idFurnitur = furnitur[userInput - 1][0]

    detailFurniturView(idFurnitur, loggedInUserInfo)
