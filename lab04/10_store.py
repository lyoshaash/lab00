#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

sofas_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
# или проще (/сложнее ?)
sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_quantity = sofas_item['quantity']
sofas_price = sofas_item['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
# или проще (/сложнее ?)
chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
