import psycopg2

# Connection details
db_config = {
    # 'dbname': 'postgres',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}
conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
databases = cursor.fetchall()

print("Databases:")
for db in databases:
    print(db[0])