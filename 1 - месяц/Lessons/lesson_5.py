# Структуры данных: словари - dict, множествo - set.
# numbers = [1, 'python', 6.9, True, (1, 2, 3), [4, 8, 5]]
# {key:value}

# [2, 5, 6] > [4, 6, 2, 3, 5]

# print({2, 1, 6}.issubset([4, 6, 2, 3, 5]))
# print({2, 5, 6, 4, 3}.issuperset([4, 2]))

# time = set(input('enter temperature: ').lower())
#
# if time.issubset('утро morning'):
#     print("доброе утро")
# elif time == 'день' or time == 'day':
#     print("добрый день")
# elif time == 'вечер' or time == 'evening':
#     print("добрый вечер")
# else:
#     print('Просто Здравствуйте, я точно не знаю какое сейчас время суток!')


# beshbarmak = {'мясо', 'лук', "лапша"}
# plov = {'рис', "морковь", "мясо"}
#
# print(beshbarmak.union(plov))
# print(beshbarmak | plov)
#
# print(beshbarmak.difference(plov))
# print(beshbarmak - plov)
#
# print(beshbarmak.intersection(plov))
# print(beshbarmak & plov)
#
# print(beshbarmak.symmetric_difference(plov))
# print(beshbarmak ^ plov)

# numbers = [1, 2, 3, 1, 4, 5, 2, 3]
# numbers2 = {1, 2, 3, 1, 4, 5, 2, 3}
#
# print(numbers)
# print(numbers2)
# print(type(numbers2))


# print(dict(enumerate('python')))
# new_student = dict(name='Jack', surname='Sparrow', age=21, country='USA')
# # print(new_student)
#
# students = {
#     'name': 'Anna',
#     'age': 19,
#     'height': 1.6,
#     'married': False,
#     'hobby': ['chess', 'english', 'books'],
#     'education': ('school', 'english C1', 'Python')
# }
#
# for key, value in students.items():
#     print(f'{key} ==> {value}')

# print(students.keys())
# print(students.values())
# print(students.items())

# found = students.get('ag', 'not found!')
# print(type(found))
# print(students.get('age', 'нет такого ключа'))
# print(students['ag'])


"""delete"""
# students.pop('height')
# del students['married']

"""edit"""
# students['height'] = 1.7
# students['education'] = list(students['education'])
# students['hobby'][0] = 'football'

"""add"""
# students['surname'] = 'Walker'
# students['hobby'].append('boxing')
# students.update(new_student)

# for i in students:
#     print(i, '>', students[i])

# print(students)
# print(students['name'])
# print(students['hobby'][1])
# print(type(students))
