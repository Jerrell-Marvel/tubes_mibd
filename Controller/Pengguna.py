from services.Pengguna import getPenggunaByUsername
from executeQuery import execute_query

def login(username, password):
  try:
    pengguna = execute_query(getPenggunaByUsername, username)
    
    if(pengguna.password == password):
      raise Exception("Password yang dimasukkan salah!")
    else: 
      return (pengguna.id_pengguna, pengguna.role)
    
  except Exception as e:
    raise e