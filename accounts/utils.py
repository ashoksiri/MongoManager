import MySQLdb

def check_connection(host,port,username,password):
    try:
        db = MySQLdb.connect(host=host, user=username,
                             passwd=password,port=port)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        results = cursor.fetchone()
        # Check if anything at all is returned
        if results:
            return True
        else:
            return False
    except MySQLdb.Error:
        print("ERROR IN CONNECTION")
    return False