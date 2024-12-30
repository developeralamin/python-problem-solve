import psycopg2

DB_NAME = "python_crud"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Database connected successfully")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    
#create table 
cursor.execute("""
	CREATE TABLE Employee
	(
		ID INT   PRIMARY KEY NOT NULL,
		NAME TEXT NOT NULL,
		EMAIL TEXT NOT NULL
	)
	""")
conn.commit()
print("Table created successfully")

