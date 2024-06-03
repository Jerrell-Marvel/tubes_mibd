from services import furnitur as furniturService
from executeQuery import execute_query

def getAllFurnitur():
    furnitur = execute_query(furniturService.getAllFurnitur)
    return furnitur