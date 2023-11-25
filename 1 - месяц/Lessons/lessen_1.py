# Введение в Python: Встроенные функции, переменные, комментарии.
# Базовые типы данных: строки, целые и дробные числа.
# you're, isn't
# str - string (строка)
# int - integer (целое)
# float - floating (дробное)

# print(type(5))
# print(type(5.5))

# name = 'Sam'
# name = input('введите имя: ')
# # age = 18  # возраст
# age = int(input('укажите возраст: '))
# current_year = 2023
# born = (current_year - age)

# print(f'имя {name} возраст: {age} год рождения: {born}')


# name = "jack \"mad\""
# surname = "o'neil".upper()
# age = 21
# print(type(name))

# print(f'name: {name} surname {surname}')
# print('name: ', name, 'surname', surname)
# print('name' + name + 'surname' + surname)
# print('name: {} surname: {}'.format(name, surname))

# print(name)
# print('name')

# как можно
# good = 5
# good_one = 5
# goodOne = 5
# Good = 5
# good_1 = 5

# как нельзя
# 23bad = 0
# bad?*) = 0
# break = 0

# print('Hello World')

# number_1 = 10
# number_2 = 2
#
# print(number_2 + number_1 * 3)
# print((number_2 + number_1) * 3)

# print(20 % 6)
# print(20 // 6)
# print(20 / 6)

# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 * number_2)
# print(number_1 / number_2)
# print(number_1 // number_2)
# print(number_1 ** number_2)
# print(number_1 % number_2)


sum_ages = 23 + 23 + 25 + 19 + 26 + 24 + 17 + 17 + \
           13 + 17 + 24 + 17 + 18 + 22 + 19 + 19 + 18 + 15
students_amount = 18
average_age = sum_ages / students_amount
print('%.2f' % average_age)
print(round(average_age, 2))
