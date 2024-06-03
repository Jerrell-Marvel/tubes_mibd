from connectDB import conn
from services.transaksi import insertTransaksi
from services.transaksi import insertManyTransaksiBagianFurnitur
from executeQuery import execute_query



def melakukanTransaksi(id_pengguna, id_furnitur, transaksiBagianFurniturData):
    cursor = conn.cursor()

    try:
        idTransaksi = execute_query(insertTransaksi, id_pengguna, id_furnitur, cursor=cursor)['id_transaksi']

        execute_query(insertManyTransaksiBagianFurnitur, idTransaksi, transaksiBagianFurniturData, cursor=cursor)

        cursor.commit()
    except Exception as e:
        cursor.rollback()
        raise e
    finally:
        cursor.close()


def getTransaksiByDateRange(startDate, endDate):
    try:
        transaksi = execute_query(getTransaksiByDateRange, startDate,endDate)
    except Exception as e:
        raise e