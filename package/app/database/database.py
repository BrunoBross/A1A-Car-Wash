import sqlite3
from sqlite3 import Error


def initializeDataBase(dbName):
    print(f'Inicializando banco no diretório: {dbName}')
    connection = None
    try:
        connection = sqlite3.connect(dbName)
        createTable(connection.cursor())
        dbInfo()
    except Error as e:
        print(f"Erro: {e}")
    finally:
        if connection:
            connection.close()


def createTable(cursor):
    cursor.execute("CREATE TABLE initial(name)")


def dbInfo():
    print(sqlite3.version)
    print(sqlite3.version_info)
    print(sqlite3.sqlite_version_info)


if __name__ == '__main__':
    dbName = "./db/pythonDataBase.db"
    initializeDataBase(dbName)
