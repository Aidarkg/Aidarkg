"""1"""


# def even_odd(integer):
#     if (integer % 2) == 0:
#         return True
#     elif type(integer) != int:
#         return None
#     else:
#         return False
#
#
# print(even_odd(92))
# print(even_odd(2.5))

"""2"""


# def spelling(proposocal):
#     if proposocal[0].isupper() and proposocal[-1] == '.':
#         return 'True'
#     else:
#         return 'False'
#
#
# print(spelling('Меня зовут Айдар.'))

"""3"""


# def calculator(number1, operator, number2):
#     if operator == '+':
#         result = number1 + number2
#     elif operator == '-':
#         result = number1 - number2
#     elif operator == '*':
#         result = number1 * number2
#     elif operator == '/':
#         result = number1 / number2
#     elif operator == '**':
#         result = number1 ** number2
#     elif operator == '%':
#         result = number1 % number2
#     else:
#         return "Недопустимый оператор"
#
#     return result
#
#
# print(calculator(10, '**', 5))
# print(calculator(11, '+', 21.5))
# print(calculator(66, '%', 25))

"""4"""


# def find_closest_number(numbers, target=0):
#     if not numbers:
#         return None
#
#     closest = numbers[0]
#     min_difference = abs(target - closest)
#
#     for number in numbers:
#         difference = abs(target - number)
#         if difference < min_difference:
#             closest = number
#             min_difference = difference
#
#     return closest
#
#
# numbers1 = [2005, 1, 2, 21, 18]
# target1 = 47
# result1 = find_closest_number(numbers1, target1)
# print(result1)
#
# numbers2 = [2002, 20, 34, 1945, 1939]
# target2 = -1
# result2 = find_closest_number(numbers2, target2)
# print(result2)
