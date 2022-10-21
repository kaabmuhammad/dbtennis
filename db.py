import psycopg2

#connect to db
con = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "postgres",
    port=5432

)

cur = con.cursor()

cur.execute("select * from clients")

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
#close the coonection
con.close()