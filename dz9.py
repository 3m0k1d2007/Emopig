import re

# Функция для проверки, является ли текст кириллическим
def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

# Словари с очками за буквы
point_en = {
    1: 'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}

point_ru = {
    1: 'АВЕИНОСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗЧЦШ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}

# Функция подсчёта очков за слово
def calculate_points(word):
    word = word.upper()
    if isCyrillic(word):
        return sum(key for letter in word for key, value in point_ru.items() if letter in value)
    else:
        return sum(key for letter in word for key, value in point_en.items() if letter in value)

# Многопользовательский режим
def scrabble_game():
    num_players = int(input("Введите количество игроков (до 10): "))
    if num_players > 10:
        print("Максимальное количество игроков — 10!")
        return

    scores = {f"Игрок {i+1}": 0 for i in range(num_players)}
    rounds = int(input("Введите количество раундов (до 10): "))
    if rounds > 10:
        print("Максимальное количество раундов — 10!")
        return

    for round_num in range(1, rounds + 1):
        print(f"\nРаунд {round_num}:")
        for player in scores.keys():
            word = input(f"{player}, введите слово: ")
            points = calculate_points(word)
            scores[player] += points
            print(f"{player} набрал {points} очков за слово '{word}'. Текущий счёт: {scores[player]}")

    # Вывод итогового результата
    print("\nИтоговое положение:")
    for player, score in scores.items():
        print(f"{player}: {score} очков")

    # Определение победителя
    winner = max(scores, key=scores.get)
    print(f"\nПобедитель: {winner} с {scores[winner]} очками!")

# Запуск игры
if __name__ == "__main__":
    print("Добро пожаловать в игру Скрабл!")
    scrabble_game()