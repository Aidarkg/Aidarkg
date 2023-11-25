# lambda функция, работа с исключениями.
# lambda arguments: expression
# try:
#     code
# except:
#     code
#     message
# finally:
#     message

from random import sample
students = [5, 16, 1, 13, 7, 8, 6, 20, 2, 15, 4, 14, 12, 9]
data = {}
while students:
    pair = sample(students, 2)
    name1_2 = input(f'enter name for {pair}: ').title()
    try:
        rate = int(input(f'enter rate for {name1_2}: '))
        if rate not in range(11):
            print('rate incorrect! must be 0 to 10')
            continue
    except:
        print('rate must be integer!')
        continue
    data[name1_2] = rate
    students.remove(pair[0])
    students.remove(pair[1])
    print(students)
    print(data)

print(sum(data.values()) / len(data))

# try:
#     print(2 + 4)
# except:
#     print('складывай числа!')
# finally:
#     print('проверка завершилась!')

# word = 'GEEKS'
#
# while True:
#     try:
#         index_in = int(input('enter index: '))
#         print(word[index_in])
#     except Exception as e:
#         print('что-то не так!', e)

    # except IndexError:
    #     print('нет такого!')
    # except ValueError:
    #     print('только числа!')

# data = []

# while True:
#     try:
#         temperature = int(input('inter temperature: '))
#     except:
#         print('вводите только числа!')
#         continue
#     data.append(temperature)
#     print(data)
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


# print([1, 2][6])
# print(int('ertds'))
# print(2 + '2')
# print(name)



# def nearest_num(numbers, target):
#     return max(numbers, key=lambda num: abs(target-num))


# print(nearest_num([111, 99, 15, 20], target=100))

# lambda_func = lambda num1, num2: num1 + num2

# def func_def(n1, n2):
#     return n1 + n2

# print(lambda_func(2, 3))
# print(func_def(4, 5))

# map, filter

# numbers = list(range(1, 16))
# print(numbers)

# mapped_nums = tuple(map(lambda num: num + 5, numbers))
# print(mapped_nums)

# filtered_nums = list(filter(lambda num: num > 10, numbers))
# print(filtered_nums)

# def up_letter(word: str):
#     return word.title()


# def show_words(func, list_words):
#     for i in list_words:
#         print(func(i))

# show_words(lambda word: word.title(), ['tokio', 'london', 'paris'])
# show_words(len, ['tokmok', 'karakol', 'bishkek'])
# show_words(up_letter, ['tokmok', 'karakol', 'bishkek'])
