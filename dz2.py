# Задание 1
# Ввод трёх чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Запрос выбора пользователя (1 — сумма, 2 — произведение)
choice = int(input("Выберите операцию: 1 — сумма, 2 — произведение: "))

# Проверка выбора и вывод результата
if choice == 1:
    result = a + b + c
    print(f"Сумма трёх чисел: {result}")
elif choice == 2:
    result = a * b * c
    print(f"Произведение трёх чисел: {result}")
else:
    print("Неверный выбор!")



# Задание 2
# Ввод трёх чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Запрос выбора пользователя (1 — максимум, 2 — минимум, 3 — среднее арифметическое)
choice = int(input("Выберите операцию: 1 — максимум, 2 — минимум, 3 — среднее арифметическое: "))

# Проверка выбора и вывод результата
if choice == 1:
    result = max(a, b, c)
    print(f"Максимум из трёх чисел: {result}")
elif choice == 2:
    result = min(a, b, c)
    print(f"Минимум из трёх чисел: {result}")
elif choice == 3:
    result = (a + b + c) / 3
    print(f"Среднее арифметическое трёх чисел: {result}")
else:
    print("Неверный выбор!")



# Задание 3
# Коэффициент перевода
METERS_TO_MILES = 0.000621371  # 1 метр = 0.000621371 мили
METERS_TO_INCHES = 39.3701       # 1 метр = 39.3701 дюймов
METERS_TO_YARDS = 1.09361        # 1 метр = 1.09361 ярда

# Ввод количества метров
meters = float(input("Введите количество метров: "))

# Запрос выбора пользователя (1 — в мили, 2 — в дюймы, 3 — в ярды)
choice = int(input("Выберите единицу измерения: 1 — мили, 2 — дюймы, 3 — ярды: "))

# Проверка выбора и вывод результата
if choice == 1:
    result = meters * METERS_TO_MILES
    print(f"{meters} метров = {result} миль")
elif choice == 2:
    result = meters * METERS_TO_INCHES
    print(f"{meters} метров = {result} дюймов")
elif choice == 3:
    result = meters * METERS_TO_YARDS
    print(f"{meters} метров = {result} ярдов")
else:
    print("Неверный выбор!")