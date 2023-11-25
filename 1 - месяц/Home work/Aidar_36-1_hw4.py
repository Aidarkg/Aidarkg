data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

letters.extend(data_tuple)
numbers.extend(data_tuple)
for i in data_tuple:
    letters = [i for i in data_tuple if type(i) not in (int, float)]
    numbers = [i for i in data_tuple if type(i) in (float, int)]

numbers.remove(6.13)
numbers[1:1] = [2]
numbers.sort()
numbers[0] = (1 ** 2)
numbers[1] = (2 ** 2)
numbers[2] = (3 ** 2)
a = letters.pop(4)
letters.append(a)
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
