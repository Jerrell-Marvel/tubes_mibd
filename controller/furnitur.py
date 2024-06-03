from services import furnitur as furniturService
from executeQuery import execute_query

def getAllFurnitur():
    furnitur = execute_query(furniturService.getAllFurnitur)
    return furnitur

def getDetailFurnitur(id_furnitur):
    detailFurnitur = execute_query(furniturService.getDetailFurniturById, id_furnitur)

    if detailFurnitur is None : 
        raise Exception("Furnitur tidak ditemukan")
    
    return detailFurnitur