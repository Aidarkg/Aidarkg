# Работа с файлами.
# w - write
# a - add
# x - create new unique file
# r - read

students = [5, 16, 11, 13, 1, 6, 19, 15, 4, 20, 12, 9, 2, 10, 17, 8]

with open('results.txt', 'x') as new_file:
    new_file.write('results test №1 group 36-1\n\n'.upper())

while students:
    name = input(f'введите имя студента под номером {students[0]}').title()
    rate = input(f'введите оценку {name}: ')
    with open('results.txt', 'a') as results:
        results.write(f'{name} {rate}\n')
    del students[0]
    print(students)




# file = open('new_file.txt', 'w', encoding='UTF-8')
# file.write('Какая-то информация! (писать на кириллице)')
# file.close()

# with open('new_file.txt', 'a', encoding='UTF-8') as file:
#     file.write('\nsecond string #2 (vtoraya stroka)')

# with open('new_file2.txt', 'x') as file:
#     file.write('new data!')
# from time import sleep
#
# with open('new_file.txt', 'r') as file:
#     for i in file.readlines():
#         sleep(2)
#         print(i, end='')

    # print(file.read())
    # print(file.readlines()[0])
