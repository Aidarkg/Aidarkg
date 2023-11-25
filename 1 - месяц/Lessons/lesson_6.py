# Функции, аргументы: *args, **kwargs.
# DRY - don't repeat yourself
# def - define


def menu(**kwargs):
    return menu


# def plus(*args):
#     return sum(args)
#
#
# print(plus(1, 5, 8))

# numbers = [1, 5, 4, 3, 6, 7, 8, 9, 2]
#
#
# def max1(sequence):
#     max_value = sequence[0]
#     for num in sequence:
#         if num > max_value:
#             max_value = num
#     return max_value
#
#
# print(max1(numbers))


"""
определение наименование(параметры):
    тело функции
    возвращение результата

вызов функции
наименование(аргументы)
"""


# def get_fullname(name='Неизвестно', surname='Неизвестно'): # name - обезательный позицинонный параметр
#     return f'name: {name.capitalize()} surname: {surname.capitalize()}'


# print(get_fullname('Aidar', 'Jamgyrchiev')) # Aidar - обезтельный позиционный аргумент
# print(get_fullname(surname='Володьев', name='Кеша')) # - keyword arguments (ключевой аргумент)
# print(get_fullname('Grigoriy', 'Лепс'))
# print(get_fullname())


# def get_square(width: int, lenght: int):
#     """
#     Мы создали функцию get_square которая принимает два параметра: длину и ширину.
#     С помощью result мы находим площадь объекта.
#     """
#     result = width * lenght
#     return result


# print(help(get_square(2, 5)))
# print(type(get_square(2, 5)))
# print(get_square.__doc__)

# square_2 = get_square(5, 8)
# square_victory = get_square(200, 500)
# print(square_2, square_victory, sep='\n')


# width = 5
# lenght = 8
# square2 = width * lenght
# print(square2)
#
# width = 200
# lenght = 500
# square_victory = width * lenght
# print(square_victory)

# print(len(nambers))
# print(len.__doc__)
# print(help(len))
