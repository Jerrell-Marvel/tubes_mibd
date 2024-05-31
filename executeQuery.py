from connectDB import conn

def execute_query(queryFn, params, cursor=None):
    commit = False
    if cursor is None:
        cursor = conn.cursor()
        commit = True
    
    queryFn(*params, cursor)
    
    if commit:
        conn.commit()
        cursor.close()