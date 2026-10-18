import os
import mysql.connector
from mysql.connector import Error


def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv(
                "DB_NAME",
                "api_security_db"
            )
        )

        if connection.is_connected():
            return connection

    except Error as error:
        print("Database connection failed:", error)

    return None
