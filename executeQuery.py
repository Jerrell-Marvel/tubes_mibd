from connectDB import conn

def execute_query(queryFn, *args , cursor=None, **kwargs):

    commit = False
    if cursor is None:
        cursor = conn.cursor()
        commit = True

    queryFn(*args, cursor=cursor, **kwargs)
    
    if commit:
        conn.commit()
        cursor.close()