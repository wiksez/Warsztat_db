from config import connect

from psycopg2 import errors
connection = connect()
cursor = connection.cursor()
try:
    query_1 = """
    CREATE DATABASE warsztat_db
    """
    cursor.execute(query_1)
    connection.close()
except errors.DuplicateDatabase:
    print("Database is already exist")

