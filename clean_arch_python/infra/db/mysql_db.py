from mysql import connector


def connect() -> connector.MySQLConnection:
    return connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="clean_arch",
    )
