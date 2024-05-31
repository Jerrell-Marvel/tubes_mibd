from connectDB import conn

def execute_query(queryFn,argsTuple, cursor=None, **kwargs):

    commit = False
    if cursor is None:
        cursor = conn.cursor()
        commit = True

    queryFn(*argsTuple, cursor=cursor, **kwargs)
    
    if commit:
        conn.commit()
        cursor.close()