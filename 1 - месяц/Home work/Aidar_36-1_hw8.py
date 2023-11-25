with open('results.txt', 'r') as file:
    lines = file.readlines()

results = {}
total_rate = 0
num_students = 0
for line in lines[1:]:
    parts = line.split()
    name, rate = parts[0], parts[1]
    results[name] = int(rate)
    total_rate += int(rate)
    num_students += 1

sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
print(sorted_results)

print('Топ 3 ученика: ')
for student, (name, rate) in enumerate(sorted_results[:3], 1):
    print(f'{student}. Name: {name}, Rate: {rate}')

print(f'Средняя оценка студентов: {total_rate // num_students}')

with open('sorted_results.txt', 'w') as file:
    file.write('sorted results test group 36-1\n'.upper())
    for name, rate in sorted_results:
        file.write(f'{name}: {rate}\n')
