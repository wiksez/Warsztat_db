import psycopg2

settings = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'coderslab',
    'database': 'warsztat_db'
}


def connect():
    connection = psycopg2.connect(**settings)
    connection.autocommit = True
    return connection
