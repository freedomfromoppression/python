import sqlite3
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute("SELECT * FROM stock WHERE market='KOSPI' ")
# 커서는 휘발성
# for row in cur:
#     print(row)
rows = cur.fetchall() #전체       한개 fetchone(), 몇몇fetchmany(3)
conn.close()
for row in rows:
    print(row)