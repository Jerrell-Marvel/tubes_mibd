from services.pengguna import getPenggunaByUsername
from services import kelurahan
from executeQuery import execute_query
from services import pengguna
from connectDB import conn

def login(username, password):
  try:
    pengguna = execute_query(getPenggunaByUsername, username)
    
    if(pengguna.password != password):
      raise Exception("Password yang dimasukkan salah!")
    else: 
      return {"id_pengguna" : pengguna.id_pengguna, "role":pengguna.role}
    
  except Exception as e:
    raise e
  

def register(username, email, nama, password, nomor_telepon, alamat, nama_kelurahan):
    try :
        cursor = conn.cursor()
        idKelurahan = execute_query(kelurahan.getKelurahan, nama_kelurahan, cursor=cursor)[0]
        execute_query(pengguna.insertPengguna, username, email, nama, password, nomor_telepon, alamat, idKelurahan, cursor=cursor)
        cursor.commit()
    except ValueError as e: 
        cursor.rollback()
        raise e
    finally :
        cursor.close()