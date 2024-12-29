import psycopg2

# Connection details
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER
        );
    """)
    conn.commit()
    print("Table created successfully!")

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
    conn.commit()
    print("Data inserted successfully!")

    # Query data
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Update data
    cursor.execute("UPDATE users SET age = %s WHERE name = %s", (31, "Alice"))
    conn.commit()
    print("Data updated successfully!")

    # Delete data
    cursor.execute("DELETE FROM users WHERE name = %s", ("Alice",))
    conn.commit()
    print("Data deleted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
