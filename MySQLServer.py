# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_alx_book_store_database():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    """
    connection = None
    cursor = None
    try:
        # Establish the connection to the MySQL server
        # Replace with your MySQL server details
        connection = mysql.connector.connect(
            host='localhost',    # Your MySQL host
            user='your_user',    # Your MySQL username
            password='your_password' # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL statement to create the database if it doesn't exist
            # IF NOT EXISTS ensures the script does not fail if the DB already exists
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except Error as e:  # Corrected: Explicitly catching mysql.connector.Error
        # Handle connection and execution errors
        print(f"Error: Failed to connect to the database or create it. {e}")

    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_alx_book_store_database()
