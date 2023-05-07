per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 5.28, 'СБЕР': 4.0}
money = int(input('Введите сумму в рублях, которую вы хотите положить на вклад:'))
deposit = []
deposit.append(int(per_cent['ТКБ'] * money / 100))
deposit.append(int(per_cent['СКБ'] * money / 100))
deposit.append(int(per_cent['ВТБ'] * money / 100))
deposit.append(int(per_cent['СБЕР'] * money / 100))
print('Сумма, которую вы получите в каждом банке:', ','.join(per_cent.keys()), '\b,', 'если вложите', money, 'за один год соответственно:', ','.join(map(str, deposit)), 'рублей.')
print('Максимальная сумма составит:', max(deposit), 'рублей.')
