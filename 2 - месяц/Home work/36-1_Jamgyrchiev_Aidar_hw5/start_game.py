from play_round import load_settings, play_game


def start():
    money = load_settings()
    print(f"Ваш начальный капитал: {money}$")

    while True:
        bet = int(input("Введите ставку (от 1 до 30): "))
        if bet < 1 or bet > 30:
            print("Ставка должна быть от 1 до 30.")
            continue

        money = play_game(money, bet)

        if money <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break

        choice = input("Хотите ли вы сыграть еще? (да/нет): ").lower()
        if choice != 'да':
            print(f"Игра окончена. Ваш итоговый капитал: {money}$")
            break


if __name__ == "__main__":
    start()
