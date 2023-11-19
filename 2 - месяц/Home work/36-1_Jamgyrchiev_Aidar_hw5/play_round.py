from random import randint
from decouple import config


def load_settings():
    commented = config('MY_MONEY', default=0, cast=int)
    return commented


def play_game(money, bet):
    winning_slot = randint(1, 30)
    print(f"Выпавшее число: {winning_slot}")
    if bet == winning_slot:
        money *= 2
        print(f"Вы выиграли! Ваш выигрыш составил {bet}$. Ваш капитал теперь {money}$")
    else:
        money -= bet
        print(f"Вы проиграли! Потеряли {bet}$. Ваш капитал теперь {money}$")
    return money
