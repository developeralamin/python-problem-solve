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

#insert multiple data
# data_insert = [
#     (1,'Alamin',"alamincse@gmail.com"),
#     (2,'incse',"incse@gmail.com"),
#     (3,'tipu',"tipu@gmail.com"),
#     (4,'dany',"dany@gmail.com")
# ]

cursor.execute("""
               INSERT INTO employee(id,name,email) VALUES 
               (1,'Alan Walker','awalker@gmail.com'), 
               (2,'Steve Jobs','sjobs@gmail.com'),
               (3,'Alan DWalker','awarawalker@gmail.com'), 
               (4,'Steve DJobs','dessjobs@gmail.com')
               """)
conn.commit()
conn.close()
print("Data inserted successfully")
