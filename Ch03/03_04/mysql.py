from mysql.connector import (connection)
if __name__ == '__main__':
    try:
        db = sql.connect(
            host='localhost',
            user='root',
            password='juancito',
            database='projects')
    except Error as e:
        print(e)