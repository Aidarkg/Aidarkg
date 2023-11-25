while True:
    word = input('Введите слово: ')
    if word == "stop" or word == 'стоп':
        print('finish')
        break
    number_word = 0
    number_vovel = 0
    number_consonant = 0
    vovel_letter = 'ауоыиэяюёеaeiouy'
    consonant_letter = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
    for count in word.lower():
        number_word += 1
    print(f'Слово: {word}')
    print(f"Количество букв: {number_word}")
    for count_vovel in word.lower():
        if count_vovel in vovel_letter:
            number_vovel += 1
        else:
            number_consonant += 1
    percent_consonant = (number_consonant/number_word) * 100
    percent_vovel = (number_vovel/number_word) * 100
    print(f'Количество согласных букв: {number_consonant}')
    print(f'Количество гласных букв: {number_vovel}')
    print(f'Согласные/Гласные: {"%.1f" % percent_consonant}%/{"%.1f" % percent_vovel}%')
