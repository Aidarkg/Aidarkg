count = 5

while count > 0:
    # birthday = input('Введите день рождения: ')
    # if birthday == 'stop':
    #     print('finish')
    #     break
    # birthday = int(birthday)
    print(f'У вас есть {count} попыток')
    birthday = int(input('Введите день рождения: '))
    birth_month = int(input('Введите месяц рождения: '))
    if 21 <= birthday <= 31 and birth_month == 3 or 1 <= birthday <= 20 and birth_month == 4:
        print('Овен')
    elif 21 <= birthday <= 30 and birth_month == 4 or 1 <= birthday <= 21 and birth_month == 5:
        print('Телец')
    elif 22 <= birthday <= 31 and birth_month == 5 or 1 <= birthday <= 21 and birth_month == 6:
        print('Близнецы')
    elif 22 <= birthday <= 30 and birth_month == 6 or 1 <= birthday <= 22 and birth_month == 7:
        print('Рак')
    elif 23 <= birthday <= 31 and birth_month == 7 or 1 <= birthday <= 21 and birth_month == 8:
        print('Лев')
    elif 22 <= birthday <= 31 and birth_month == 8 or 1 <= birthday <= 23 and birth_month == 9:
        print('Дева')
    elif 24 <= birthday <= 30 and birth_month == 9 or 1 <= birthday <= 23 and birth_month == 10:
        print('Весы')
    elif 24 <= birthday <= 31 and birth_month == 10 or 1 <= birthday <= 22 and birth_month == 11:
        print('Скорпион')
    elif 23 <= birthday <= 30 and birth_month == 11 or 1 <= birthday <= 22 and birth_month == 12:
        print('Стрелец')
    elif 23 <= birthday <= 31 and birth_month == 12 or 1 <= birthday <= 20 and birth_month == 1:
        print('Козерог')
    elif 21 <= birthday <= 30 and birth_month == 1 or 1 <= birthday <= 19 and birth_month == 2:
        print('Водолей')
    elif 20 <= birthday <= 29 and birth_month == 2 or 1 <= birthday <= 20 and birth_month == 3:
        print('Рыбы')
    else:
        print('Ошибка! Введите день рождения от 1 до 31 и месяц рождения от 1 до 12!')
    count -= 1
