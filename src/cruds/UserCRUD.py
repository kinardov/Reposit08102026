from db.DbConnector import DbConnector
from model.User import User


class UserCRUD:
    
    
    def __init__(self):
        self.dbc = DbConnector()

    def select_all(self):
        self.dbc.cursor.execute('SELECT * FROM users')
        rs = self.dbc.cursor.fetchall()

        rows = []
        for row in rs:
            u = User(*row)
            rows.append(u)
        
        return rows

if __name__ == '__main__':
    uc = UserCRUD()
    items = uc.select_all()
    
    
    for item in items:
        print(item)




