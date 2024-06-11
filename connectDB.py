import pyodbc

# data koneksi sql server
SERVER = 'LAPTOP-ES7ENIHT\SQLEXPRESS'
DATABASE = 'tubes6'
USERNAME = 'wombatu'
PASSWORD = 'wombatu2024'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'

# buat koneksi ke sql server
conn = pyodbc.connect(connectionString)
