# Логический тип данных - bool, условные конструкции и операторы.
# print(type(False))
# print(type(True))
# схема срезов - [start:stop:step]


""" САМОСТОЯТЕЛЬНОЕ ЗАДАНИЕ
Дополнить ДЗ 1

если сумма расходов превысило 20000, вывести в консоль "потрачено много!"
если сумма расходов от 10000 до 20000, вывести в консоль "потрачено средне!"
если сумма расходов от 1 до 10000, вывести в консоль "потрачено мало!"
в ином случае вывести в консоль "не потрачено ничего!"
"""

# total_expenses = 178499
#
# if total_expenses >= 20000:
#     print('потрачено много!')
# elif total_expenses >= 10000 and total_expenses < 20000:
#     print('потрачено средне!')
# elif total_expenses >= 1 and total_expenses < 10000:
#     print('потрачено мало!')
# else:
#     print('не потрачено ничего!')

# age = int(input('enter age: '))

# if age >= 18:
#     print('welcome')
# else:
#     print(f'вход запрещён! приходите через {18 - age} лет')
#


# word = 'конфигурация'
#
# print(word)
# print(word[::-1])
# print(word[-1])
# print(word[0:3])
# print(word[::4])
# print(word[0])
# print(word[5])

# print('АНАТОЛИЙ'.lower())

"""операторы назначения"""
# number = 5
# # number = number + 10
# number += 10
# print(number)

"""логический оператор"""
# or, and, not

# word = 'GEEKS'
# print('not' if 'E' not in word else 'yes')
# print(not False)
# print(not True)

"""операторы сравнения"""
# print(2 < 7 and 7 > 5)
# print(2 < 7 > 5)
# print(2 < 4 or 2 == 4)
# print(2 <= 4)
# print(5 < 8)
# print(2 > 3)
# print(2 == 3)
# print(2 != 3)

# time = input('введите время суток: ').lower()
#
# if time == 'утро' or time == 'morning':
#     print("доброе утро")
# elif time == 'день' or time == 'day':
#     print("добрый день")
# elif time == 'вечер' or time == 'evening':
#     print("добрый вечер")
# else:
#     print('Здравствуйте! (точное время суток неопределено!)')

temperature = int(input('inter temperature: '))

if temperature >= -50 and temperature <= 0:
    print('cold')
elif temperature >= 1 and temperature <= 10:
    print('cool')
elif temperature >= 11 and temperature <= 25:
    print('warm')
elif temperature >= 26 and temperature <= 50:
    print('heat')
else:
    print('ты умрешь! не выходи! смертЪ')


