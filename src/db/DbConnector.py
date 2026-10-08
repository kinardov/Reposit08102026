import sqlite3

class DbConnector:
    DB_NAME = '/home/student/DEV/eclipse-workspace--PyDev/IP419--DBv01/db/ip419--db-v01.sqlite3'

    def __init__(self):
        self.connection = sqlite3.connect(self.DB_NAME)
        self.cursor = self.connection.cursor()
        
    def commit(self):
        self.connection.commit()


    def close(self):
        self.connection.close()





if __name__ == '__main__':
    dbc = DbConnector()
    dbc.cursor.execute('SELECT * FROM users')
    rows = dbc.cursor.fetchall()
    dbc.close()

    for row in rows:
        print(row)








