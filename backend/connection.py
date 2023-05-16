import psycopg2

class Connection():

    conn = None

    def __init__(self):

        try:
            self.conn = psycopg2.connect(host="database", database="test", user="postgres", password="password")
        except:
            return {"message":"Error de conexión"}
            self.conn.close()
        
    def __del__(self):

        self.conn.close()

    def read_all(self, tb_name):

        cur = self.conn.cursor()
        cur.execute("""SELECT * FROM %s""" % (tb_name))
        data = cur.fetchall()
        return data
        