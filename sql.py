# SQLの接続、読み込みなどをする用

import psycopg2


def connect(self):
    self.conn=psycopg2.connect("host=127.0.0.1 dbname=food user=postgres password=postgres")
    self.cur=self.conn.cursor()

def query(self,text):
    self.cur.execute(text)
    return self.cur.fetchone()