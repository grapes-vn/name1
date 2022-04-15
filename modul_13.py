ticket = int(input('Введите количество билетов: '))
S = 0 # переменная счётчик, в которой считаем сумму
for i in range(ticket):
    age = int(input('Возраст посетителя: '))
    if 0 <= age < 18:
        S += 0
    elif 18 <= age < 25:
        S += 990
    elif 25 <= age <= 130:
        S += 1390
    else:
        print('Тебе не может быть столько лет')
        break
if ticket > 3:
    S *= 0.9
else:
    S *= 1
print('Сумма к оплате: ', int(S))