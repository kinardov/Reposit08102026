class User:


    def __init__(self, id, name, bday, payment):
        self.id = id
        self.name = name
        self.bday = bday
        self.payment = payment
        
    def __str__(self):
        return f"""class User [
        id = {self.id}
        name = {self.name}
        bday = {self.bday}
        payment = {self.payment}
]
"""



if __name__ == '__main__':
    u = User(1, 'Vasia', '2001-01-01', 10000.00)
    
    print(u)
    print(u.name)
        
        