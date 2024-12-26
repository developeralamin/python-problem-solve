import mysql.connector

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",   # Use the correct format for the host
        port=3306,          # Specify the port separately if it's not default
        user="root",
        password="",
        database=""  # Optional: Include this if connecting to a specific database
    )
    if connection.is_connected():
        print("Successfully connected to MySQL database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
