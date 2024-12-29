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

sql = "UPDATE users SET age=50 where age = 30"
#select data
cursor.execute(sql)
conn.commit()

print(f"Rows updated: {cursor}")




