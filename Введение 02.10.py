# ============================ ЗАДАНИЕ 1 ============================
#
number = int(input("введите число для умножения:"))
print(f"\n таблица умножения для числа {number}")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
#
#  ============================ ЗАДАННИЕ 3 ==========================
print("\nКонвертер валют")
print("1. Рубли -> Доллары")
print("2. Доллары -> Рубли")

choice = int(input("Выберите вариант (1 или 2): "))

if choice == 1:
    rub = float(input("Введите сумму в рублях: "))
    usd = rub / 100  # курс условный: 1$ = 100 руб
    print(f"{rub} руб. = {usd:.2f} $")

elif choice == 2:
    usd = float(input("Введите сумму в долларах: "))
    rub = usd * 100
    print(f"{usd} $ = {rub:.2f} руб.")

else:
    print("Неверный выбор")


# ================== ЗАДАНИЕ 3 ==================

start = int(input("\nВведите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start

while True:
    num = int(input("Введите число из диапазона: "))
    if start <= num <= end:
        break
    else:
        print("Число вне диапазона. Попробуйте снова.")

for i in range(start, end + 1):
    if i == num:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")

print()


# ================== ЗАДАНИЕ 4 ==================

import random
import time

secret = random.randint(1, 500)
attempts = 0
print("\nЯ загадал число от 1 до 500. Попробуй угадать (0 - выход).")

start_time = time.time()

while True:
    guess = int(input("Ваш вариант: "))
    if guess == 0:
        print("Вы сдались. Игра окончена.")
        break

    attempts += 1

    if guess < secret:
        print("Моё число больше.")
    elif guess > secret:
        print("Моё число меньше.")
    else:
        end_time = time.time()
        print(f"Поздравляю! Вы угадали число {secret}")
        print(f"Количество попыток: {attempts}")
        print(f"Время игры: {round(end_time - start_time, 2)} секунд")
        break