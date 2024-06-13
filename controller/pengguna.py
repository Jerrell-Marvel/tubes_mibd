from services import kelurahan
from executeQuery import execute_query
from services import pengguna as penggunaServices
from connectDB import conn


def login(username, password):
    try:
        pengguna = execute_query(penggunaServices.getPenggunaByUsername, username)

        if (pengguna["password"] != password):
            raise Exception("Password yang dimasukkan salah!")
        else:
            return pengguna

    except Exception as e:
        raise e


def register(username, email, nama, password, nomor_telepon, alamat, nama_kelurahan):

    try:
        cursor = conn.cursor()
        kelurahanQueryRes = execute_query(
            kelurahan.getKelurahan, nama_kelurahan, cursor=cursor)
        idKelurahan = kelurahanQueryRes["id_kelurahan"]
        dataPengguna = execute_query(penggunaServices.insertPengguna, username, email,
                                     nama, password, nomor_telepon, alamat, idKelurahan, cursor=cursor)
        cursor.commit()

        return dataPengguna
    except Exception as e:
        cursor.rollback()
        raise e
    finally:
        cursor.close()


def updatePengguna(id_pengguna, nama, nomor_telepon, email, alamat, nama_kelurahan):
    id_kelurahan = execute_query(kelurahan.getKelurahan, nama_kelurahan)[
        "id_kelurahan"]

    execute_query(penggunaServices.updatePengguna, id_pengguna, nama,
                  nomor_telepon, email, alamat, id_kelurahan)


def getPenggunaByUsername(username): 
    return execute_query(penggunaServices.getPenggunaByUsername, username)