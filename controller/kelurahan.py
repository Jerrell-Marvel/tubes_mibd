from services import kelurahan as kelurahanService
from executeQuery import execute_query

def getKelurahan(namaKelurahan):
    queryResult =  execute_query(kelurahanService.getKelurahan, nama_kelurahan=namaKelurahan)
    return queryResult["id_kelurahan"]

