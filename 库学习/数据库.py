import pymysql

param = {'host':'127.0.0.1',
         'port':3306,
         'user':'root',
         'passwd':'zxw2314700',
         'db':'MySQL',
         'charset':'utf8'}

conn = pymysql.connect(**param)


cur = conn.cursor()

sql = "select * from user"

cur.execute(sql)

rows = cur.fetchall()

#print(rows)

for dr in rows:
    print(dr)

conn.close()