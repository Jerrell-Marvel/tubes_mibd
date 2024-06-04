import pyodbc

# data koneksi sql server
SERVER = 'LAPTOP-PVCB9MBF\SQLEXPRESS'
DATABASE = 'tubes6'
USERNAME = 'sa'
PASSWORD = 'jOuter2407123#*'

connectionString = 'DRIVER=Devart ODBC Driver for SQL Server;Description=ODBC Driver for SQL Server;Data Source=LAPTOP-OAT6HLEM;Initial Catalog=Tubes;Authentication=Windows'

# buat koneksi ke sql server
conn = pyodbc.connect(connectionString)