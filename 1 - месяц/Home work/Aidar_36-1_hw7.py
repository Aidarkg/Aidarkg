"""1"""


def find_closest_number(numbers, target=0):
    if not numbers:
        return None

    closest = numbers[0]
    min_difference = abs(target - closest)

    for number in numbers:
        difference = abs(target - number)
        if difference < min_difference:
            closest = number
            min_difference = difference

    sorted_numbers = sorted(numbers, key=lambda x: abs(target - x))  # Вот так я расширил функцию

    return closest, sorted_numbers


numbers1 = [2005, -1, 2, 21, 18]
target1 = -47
result1 = find_closest_number(numbers1, target1)
print(result1)


numbers2 = [2002, 20, 34, 1945, 1939]
target2 = -1
result2 = find_closest_number(numbers2, target2)
print(result2)


"""2"""


# def element(iterable):
#     while True:
#         try:
#             user_input = input(f'Введите индекс элемента - {iterable}: ')
#             if user_input == 'стоп' or user_input == 'stop':
#                 break
#             else:
#                 index = int(user_input)
#                 print(iterable[index])
#         except:
#             print(f'Введите индекс от 0 до {len(iterable) - 1}')
#
#
# my_list = [1, 2, 3, 6]
# my_tuple = ('iphone', 'samsung', 'xiaomi')
# word = 'aidar'
# element(my_list)

"""3"""

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# map_numbers = list(map(lambda x: x ** 3, numbers))
# print(filter_numbers, map_numbers, sep='\n')
