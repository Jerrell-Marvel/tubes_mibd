import pyodbc

from connectDB import conn

# buat cursor dari connection
cursor = conn.cursor()

a = cursor.execute("SELECT 5").fetchone()[0]
b = cursor.execute("SELECT 6").fetchone()[0]

print(a)