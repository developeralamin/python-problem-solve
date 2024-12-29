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

#delete records
sql = "DELETE FROM users WHERE id = '4'"
cursor.execute(sql)
conn.commit()

print(cursor.rowcount, "record(s) deleted")


