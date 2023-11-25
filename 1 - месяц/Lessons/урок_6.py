# Функции, аргументы: *args, **kwargs.
# DRY - don't repeat yourself
# def - define

"""
определение наименование(параметры):
    тело функции
    возвращение результата

вызов функции
наименование(аргументы)
"""

# data = ('bir', 'eki', 'uch', '1', '2', '3')
#
# designations = []
# codes = []
#
# for i in data:
#     if i.isdigit():
#         codes.append(i)
#     else:
#         designations.append(i)
#
# operators = {}
#
# counter = 0
# while counter != len(codes):
#     operators[designations[counter]] = {codes[counter]}
#     counter += 1
#
# print(designations, codes, sep='\n')
#
# operators['bir'].update(['I', 'one', 'uno', 'bir ta'])
# print(operators)


# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat='pizza', drink='cola', sdf='345', dfgh=3453)
# print(monday)

# def plus(*args):
#     return sum(args)
#
# print(plus(5, 4, 1, 2, 45, 12, 34))

# def get_fullname(name, surname='Белгисиз'):  # name - обязательный позиционный параметр surname - необязательный позиционный параметр(по умолчанию)
#     return f'имя: {name.upper()} фамилия: {surname.upper()}'
#
#
# print(get_fullname("Erkin", 'Sotuev'))  # Erkin - обязательный позиционный аргумент
# print(get_fullname("Karl", 'Karlsson'))
# print(get_fullname(surname='Володьев', name="Кеша"))  # - keyword arguments (Ключевые аргументы)
# print(get_fullname('Grigoriy'))


# def get_square(width: int, length: int):
#     """
#     Принимает ширину и длину, возвращает произведение(площадь).
#     """
#     result = width * length
#     return result

# print(get_square.__doc__)
# print(help(get_square))

# numbers = [-1, -9, -2, -8, -3, -7, -4, -6, -5]
#
# """написать код, который подсчитает максимальное число из чисел списка"""
#
# def max1(sequence):
#     max_value = sequence[0]
#     for num in sequence:
#         print(num, max_value)
#         if num > max_value:
#             max_value = num
#     return max_value
#
# print(max1(numbers))


# counter = 0
# for i in numbers:
#     print(f'{counter} + {i} = {counter + i}')
#     counter += i
# print(counter)

#
# print(len(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(sorted(numbers))

# print(len.__doc__)
# print(help(len))

# square_2 = get_square(5, 8)
# square_victory = get_square(200, 500)
# print(square_2, square_victory, sep='\n')

# width = 5
# length = 8
# square_2 = width * length
# print(square_2)
#
# width = 200
# length = 500
# square_victory = width * length
# print(square_victory)
