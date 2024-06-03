from connectDB import conn


def execute_query(queryCallbackFn, *args, cursor=None, **kwargs):
    commit = False
    if cursor is None:
        cursor = conn.cursor()
        commit = True
    
    returnVal = queryCallbackFn(*args, cursor=cursor, **kwargs)

    if commit:
        conn.commit()
        cursor.close()

    return returnVal
