from config import connect

from psycopg2 import errors
try:
    connection = connect()
    cursor = connection.cursor()
except errors.OperationalError:
    print("Incorrect server connection. Check the settings")


try:
    query_1 = """
    CREATE DATABASE warsztat_db
    """
    cursor.execute(query_1)
    connection.close()
except errors.DuplicateDatabase:
    print("Database is already exist")


choice1 = input("Do you want to create a table USERS?\nyes - 1; no - 0: ")
try:
    if choice1 == '1':
        query_2 = """
        create table users 
        (
            id serial Primary key,
            username varchar(255),
            hashed_password varchar(80)
        ); 
        """
        cursor.execute(query_2)
        connection.close()
        print("The table was created!")
except errors.DuplicateTable:
    print("The table USERS is already exist")
choice2 = input("Do you want to create a table MESSAGES?\nyes - 1; no - 0: ")
try:
    if choice2 == '1':
        query_3 = """
        create table messages 
        (
            id serial Primary key,
            from_id integer,
            to_id integer,
            foreign key (from_id) references messages (id),
            foreign key (to_id) references messages (id),
            creation_date timestamp,
            text varchar(255)
        );
        """
        cursor.execute(query_3)
        connection.close()
        print("The table was created!")
except errors.DuplicateTable:
    print("The table MESSAGES is already exist")