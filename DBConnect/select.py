import psycopg2
# Connection details
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}
conn = psycopg2.connect(**db_config)
cursor = conn.cursor()


#select data
cursor.execute("SELECT * FROM users where id > 2")
myresult = cursor.fetchall()
for x in myresult:
    print(x)




