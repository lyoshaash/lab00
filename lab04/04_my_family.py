#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['babushka', 'papa', 'mama', 'dyadya', 'brat1', 'brat2', 'ya', 'brat3']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['babuska', 160],
    ['papa', 165],
    ['mama', 175],
    ['dyadya', 185],
    ['brat1', 180],
    ['brat2', 185],
    ['ya', 167],
    ['brat3', 180],
]
sum = 0
for person in my_family_height:
    sum+= person[1]
print(my_family_height[1][1])
print(sum)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
