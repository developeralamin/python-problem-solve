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

# Insert data
data_to_insert = [
    ("Alice", 30),
    ("Alamin", 50),
    ("Rafiq", 10),
    ("Kalam", 20)
]
cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", data_to_insert)
conn.commit()
print("Data inserted successfully!")