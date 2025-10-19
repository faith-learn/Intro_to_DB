import mysql.connector
from mysql.connector import Error

def create_database():
    # Initialize connection and cursor to None
    connection = None
    cursor = None

    # 🚨 ACTION REQUIRED: Replace "AlxDatabase25!" with your actual MySQL root password
    MYSQL_PASSWORD = "AlxDatabase25!" 

    try:
        # Step 1: Connect to the MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=MYSQL_PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Step 2: Execute the command to create the database if it doesn't exist
            # This ensures the script does not fail if the DB is already present.
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Step 3: Print success message
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Step 4: Handle connection and execution errors
        print(f"❌ Error while connecting to MySQL: {err}")

    finally:
        # Step 5: Ensure resources are closed properly
        # Close cursor first
        if cursor:
            cursor.close()
            
        # Close connection second
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()