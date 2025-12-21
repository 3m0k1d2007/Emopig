# Задание 1
number = int(input("Введите число от 1 до 100: "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Ошибка: число не в диапазоне от 1 до 100.")



# Задание 2
number = float(input("Введите число: "))
power = int(input("Введите степень (от 0 до 7): "))

if 0 <= power <= 7:
    result = number ** power
    print(f"Результат: {result}")
else:
    print("Ошибка: степень должна быть от 0 до 7.")



# Задание 3
# Стоимость разговора (в рублях)
cost = float(input("Введите стоимость разговора: "))

# Операторы (примерные коды)
operators = {
    1: "Оператор A",
    2: "Оператор B",
    3: "Оператор C"
}

print("Выберите оператора для звонка (отправителя):")
for key, value in operators.items():
    print(f"{key} - {value}")
sender = int(input("Ваш выбор: "))

print("Выберите оператора для приёма звонка:")
receiver = int(input("Ваш выбор: "))

# Тарифы на звонки между операторами (в процентах от стоимости разговора)
tariffs = {
    (1, 2): 1.1,  # на 10% дороже
    (1, 3): 1.2,  # на 20% дороже
    (2, 1): 1.15, # на 15% дороже
    (2, 3): 1.05, # на 5% дороже
    (3, 1): 1.25, # на 25% дороже
    (3, 2): 1.1   # на 10% дороже
}

# Базовая стоимость (если операторы совпадают)
if sender == receiver:
    final_cost = cost
else:
    tariff_key = (sender, receiver)
    if tariff_key in tariffs:
        final_cost = cost * tariffs[tariff_key]
    else:
        print("Нет данных о тарифе для этого направления.")
        exit()

print(f"Стоимость разговора: {final_cost:.2f} руб.")



# Задание 4
def calculate_salary(sales):
    base_salary = 200  # базовая зарплата
    if sales <= 500:
        bonus = sales * 0.03  # 3% от продаж
    elif 500 < sales <= 1000:
        bonus = sales * 0.05  # 5% от продаж
    else:
        bonus = sales * 0.08  # 8% от продаж
    return base_salary + bonus

# Ввод данных о продажах трёх менеджеров
sales1 = float(input("Введите уровень продаж первого менеджера: "))
sales2 = float(input("Введите уровень продаж второго менеджера: "))
sales3 = float(input("Введите уровень продаж третьего менеджера: "))

# Расчёт зарплат
salary1 = calculate_salary(sales1)
salary2 = calculate_salary(sales2)
salary3 = calculate_salary(sales3)

# Определение лучшего менеджера (с максимальными продажами)
best_manager = max(sales1, sales2, sales3)
if best_manager == sales1:
    salary1 += 200  # премия лучшему менеджеру
elif best_manager == sales2:
    salary2 += 200
else:
    salary3 += 200

# Вывод результатов
print(f"Зарплата первого менеджера: {salary1} ")