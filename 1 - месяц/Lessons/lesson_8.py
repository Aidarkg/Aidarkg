# работа с файлами
# w - запись, write
# a - add
# x - crate new unique file

students = [5, 16, 11, 13, 1, 6, 19, 15, 4, 20, 12, 9, 2, 10, 17]

with open('results.txt', 'x') as new_file:
    new_file.write('results test №1 grop 36-1\n\n'.upper())

while students:
    name = input(f'введите имя студента под номером {students[0]}: ').title()
    rate = input(f'введите оценку {name}: ')
    with open('results.txt', 'a') as results:
        results.write(f'{name} {rate}\n')
    del students[0]
    print(students)




# with open('new_file.txt', 'r') as file:
#     print(file.read())
#     print(file.readline())

# file = open('new_file.txt', 'w')
# file.write('Какая то информация! (писать на кирилице)')
# file.close()

# with open('new_file.txt', 'a') as file:
#     file.write('\nsecond string #2 (vtoray stroka)')

# with open('new_file2.txt', 'x') as file:
#     file.write('new data')

# with open('topics.txt', 'r') as file:
#     print(file.read())
