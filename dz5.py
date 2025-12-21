# Задание 1
# Запрос числа у пользователя
number = int(input("Введите число для таблицы умножения: "))

# Вывод таблицы умножения для этого числа (с 1 по 10)
print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")



# Задание 2
# Курсы валют (относительно рубля, примерные значения)
rates = {
    "USD": 90,
    "EUR": 100,
    "GBP": 115,
    "JPY": 0.75
}

print("Конвертер валют. Доступные валюты: USD, EUR, GBP, JPY")

while True:
    print("\nМеню:")
    print("1. Конвертировать из рублей")
    print("2. Конвертировать в рубли")
    print("3. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "3":
        print("До свидания!")
        break

    currency = input("Введите код валюты (например, USD): ").upper()
    if currency not in rates:
        print("Валюта не найдена!")
        continue

    amount = float(input("Введите сумму: "))

    if choice == "1":  # из рублей
        result = amount / rates[currency]
        print(f"{amount} RUB = {result:.2f} {currency}")
    elif choice == "2":  # в рубли
        result = amount * rates[currency]
        print(f"{amount} {currency} = {result:.2f} RUB")
    else:
        print("Неверный выбор!")



# Задание 3
# Ввод границ диапазона и числа
lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))
number = int(input(f"Введите число в диапазоне от {lower_bound} до {upper_bound}: "))

# Проверка, что число в диапазоне
while number < lower_bound or number > upper_bound:
    print(f"Число должно быть в диапазоне [{lower_bound}, {upper_bound}]!")
    number = int(input(f"Повторите ввод числа: "))

# Вывод диапазона с выделением числа
for i in range(lower_bound, upper_bound + 1):
    if i == number:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
print()  # Переход на новую строку



# Задание 4
import random
import time

# Загадываем число от 1 до 500
secret_number = random.randint(1, 500)
attempts = 0
start_time = time.time()

print("Игра 'Угадай число'!")
print("Я загадал число от 1 до 500. Угадайте его!")
print("Введите 0, если хотите выйти.")

while True:
    guess = int(input("Ваше предположение: "))
    attempts += 1

    if guess == 0:  # Выход по 0
        print("До свидания!")
        break

    if guess == secret_number:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
        print(f"Это заняло {elapsed_time:.2f} секунд.")
        break
    elif guess < secret_number:
        print("Моё число больше!")
    else:
        print("Моё число меньше!")