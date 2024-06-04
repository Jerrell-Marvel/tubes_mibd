from services import furnitur as furniturService
from executeQuery import execute_query

def getAllFurnitur():
    furnitur = execute_query(furniturService.getAllFurnitur)
    return furnitur

def getDetailFurnitur(id_furnitur, id_bagian_furnitur=None,  id_warna=None, id_material=None):
    detailFurniturList = execute_query(furniturService.getDetailFurniturById, id_furnitur, id_bagian_furnitur=id_bagian_furnitur, id_warna=id_warna, id_material=id_material)
    
    return detailFurniturList


def updateBagianFurnitur(id_bagian_furnitur, id_warna, id_material, nama_bagian_furnitur, panjang, lebar, tinggi, harga, stok):
    execute_query(furniturService.updateBagianFurnitur,id_bagian_furnitur, id_warna, id_material, nama_bagian_furnitur, panjang, lebar, tinggi, harga, stok)