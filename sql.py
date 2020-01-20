# SQLの接続、読み込みなどをする用

import psycopg2

#connection = psycopg2.connect("host=192.168.0.10 port=5432 dbname=testdb user=testuser password=testpassword")
#cursor = connection.cursor()
#cur.execute('SELECT * FROM users')
#cur.close()
#conn.close()

def connect():
    return True