per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую Вы планируете положить под проценты: "))

deposit = [i*money/100 for i in per_cent.values()]

print(list(map(int, deposit)))

print("Максимальная сумма, которую вы можете заработать - ", int(max(deposit)))
