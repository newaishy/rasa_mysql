import mysql.connector

def get_db_connection():
    DB_CONFIG = {
        "host": "your_db_host",
        "user": "your_db_user",
        "password": "your_db_password",
        "database": "your_db_name"
    }

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print("Error connecting to database:", e)
        return None
