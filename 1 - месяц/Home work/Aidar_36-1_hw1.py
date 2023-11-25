consumption_mondey = int(input("Введите расход за понедельник: "))
consumption_tuesday = int(input("Введите расход за вторник: "))
consumption_wednesday = int(input("Введите расход за среду: "))
consumption_thursday = int(input("Введите расход за четверг: "))
consumption_friday = int(input("Введите расход за пятницу: "))
consumption_saturday = int(input("Введите расход за суботту: "))
consumption_sunday = int(input("Введите расход за воскресенье: "))
list_consumption = [consumption_mondey, consumption_tuesday, consumption_wednesday, consumption_thursday,
                    consumption_friday, consumption_saturday, consumption_sunday]
sum_consumption = sum(list_consumption)
average_consumption = sum_consumption / len(list_consumption)
print(f"Расход за неделю: {sum_consumption}")
print(f"Средний расход в день: {round(average_consumption, 1)}")
print(f'Самая большая сумма потраченное за день: {max(list_consumption)}')
print(f'Самая маленькая сумма потраченное за день: {min(list_consumption)}')
if sum_consumption >= 20000:
    print("Потрачено много!")
elif 10000 < sum_consumption < 20000:
    print("Потрачено средно!")
elif 1 <= sum_consumption < 10000:
    print("Потрачено мало!")
else:
    print("Не потрачено ничего")
