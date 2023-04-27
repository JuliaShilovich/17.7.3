per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите вкладываемую сумму: "))

deposit = [i/100*money for i in per_cent.values()]

print(list(map(round, deposit)))

print("Максимальная сумма, которую вы можете заработать — ", max(deposit))