# Циклы.
# i - item, index, iterable

# eng = 'qwerty'
# rus = 'йцукен'

# found_index = eng.index('e')
# print(found_index)
# print(rus[found_index])
# print(rus[eng.index('e')])


# ghjuhfvvbnhjdfybt yf gfqnjy
# зкщпефььштп щт знерщт


# cash = 100
# percents = 0.2
# years = 10
#
# for year in range(1, years+1):
#     cash += cash * percents
#     print(f'{year}) {"%.2f" % cash}')

# for outer in range(1, 4):
#     for inner in range(1, 4):
#         print(outer, inner)

# for attempt in range(1, 5+1):
#     print(f'осталось попыток: {attempt}')
#     temperature = int(input('inter temperature: '))
#
#     if temperature >= -50 and temperature <= 0:
#         print('cold')
#     elif temperature >= 1 and temperature <= 10:
#         print('cool')
#     elif temperature >= 11 and temperature <= 25:
#         print('warm')
#     elif temperature >= 26 and temperature <= 50:
#         print('heat')
#     else:
#         print('ты умрешь! не выходи! смертЪ')

# for number in range(1, 11):
#     if number % 2 == 0:
#         continue
#     print(number)

# word = 'Geeks'
#
# for letter in word:
#     print(letter)


# number = int(input('enter number: '))
# start = 1
# end = 10
# right_counter, wrong_counter = 0, 0
#
# while start != end:
#     if wrong_counter == 5:
#         print('Вы превысили лимит ошибок!')
#         break
#     right_answer = (start * number)
#     user_answer = int(input(f'сколько будет {number} * {start} = '))
#     if user_answer == right_answer:
#         print('Правильно!')
#         right_counter += 1
#     else:
#         print(f"Неверный ответ! правильный ответ {right_answer}")
#         wrong_counter += 1
#         continue
#
#     start += 1
#
# print(
#     f'right: {right_counter}\n'
#     f'wrong: {wrong_counter}'
# )


# counter = 5
# while counter > 0:
#     # temperature = input('inter temperature: ')
#     # if temperature == 'stop':
#     #     print('exit...')
#     #     break
#     # temperature = int(temperature)
#     print(f'осталось {counter} попыток! ')
#     temperature = int(input('enter temp: '))
#     if temperature >= -50 and temperature <= 0:
#         print('cold')
#     elif temperature >= 1 and temperature <= 10:
#         print('cool')
#     elif temperature >= 11 and temperature <= 25:
#         print('warm')
#     elif temperature >= 26 and temperature <= 50:
#         print('heat')
#     else:
#         print('ты умрешь! не выходи! смертЪ')
#     counter -= 1

# counter = 0
#
# while counter != 1_000_000:
#     print('Geeks', counter)
#
#     if counter == 250:
#         print('finish')
#         break
#     counter += 1

# n = 5
#
# while n > 0:
#     print(n)
#     n -= 1
