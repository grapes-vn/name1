class Client:
    def __init__(self, name, surname, city, balance = 0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'
    def get_client(self):
        return f'{self.name} {self.surname}, г. {self.city}'

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Василий', 'Ребров', 'Симферополь', 40)
client_3 = Client('Виктор', 'Титов', 'Краснодар', 55)
client_list = [client_1, client_2, client_3]
print(client_1)
print()
for client in client_list:
    print(client.get_client())

