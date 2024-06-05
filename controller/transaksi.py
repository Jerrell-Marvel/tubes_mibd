from connectDB import conn

from services import transaksi as transaksiServices
from services import furnitur as furniturServices
from executeQuery import execute_query
from utils.sqlUtils import groupTransaksi



def melakukanTransaksi(id_pengguna, id_furnitur, transaksiBagianFurniturData):
    cursor = conn.cursor()

    try:
        idTransaksi = execute_query(transaksiServices.insertTransaksi, id_pengguna, id_furnitur, cursor=cursor)['id_transaksi']

        for bagianFurniturData in transaksiBagianFurniturData :
            idBagianFurnitur = bagianFurniturData["id_bagian_furnitur"]
            idWarna = bagianFurniturData["id_warna"]
            idMaterial = bagianFurniturData["id_material"]
            kuantitasDibeli = bagianFurniturData["kuantitas"]

            detailBagianFurnitur = execute_query(furniturServices.getDetailBagianFurnitur, idBagianFurnitur, idWarna, idMaterial, rowLock = True, cursor=cursor)

            stokTersedia = detailBagianFurnitur["stok"]

            if stokTersedia >= kuantitasDibeli : 
                execute_query(furniturServices.updateStokDetailBagianFurnitur, idBagianFurnitur, idWarna, idMaterial, kuantitasDibeli, cursor=cursor)
            else :
                raise Exception("Kuantitas tidak valid (barang tidak tersedia)")


        execute_query(transaksiServices.insertManyTransaksiBagianFurnitur, idTransaksi, transaksiBagianFurniturData, cursor=cursor)

        cursor.commit()
    except Exception as e:
        cursor.rollback()
        raise e
    finally:
        cursor.close()


def getTransaksiByDateRange(startDate, endDate):
    try:
        transaksi = execute_query(transaksiServices.getTransaksiByDateRange, startDate=startDate,endDate=endDate)

        groupedTransaksi = groupTransaksi(transaksi)
        
        totalPendapatan = execute_query(transaksiServices.getTotalPendapatan, startDate, endDate)

        return {
            "transaksi" : groupedTransaksi,
            "totalPendapatan" : totalPendapatan
        }
    except Exception as e:
        raise e
    
def getTransaksiPengguna(id_pengguna):
    transaksi = execute_query(transaksiServices.getTransaksiByDateRange, id_pengguna=id_pengguna)

    
    groupedTransaksi = groupTransaksi(transaksi)
    return groupedTransaksi