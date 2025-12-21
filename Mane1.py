# Задание 1
# Ввод трёх чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Вычисление суммы и произведения
sum_result = a + b + c
product_result = a * b * c

# Вывод результатов
print("Сумма чисел:", sum_result)
print("Произведение чисел:", product_result)



# Задание 2
# Ввод трёх чисел от пользователя
salary = float(input("Введите зарплату за месяц: "))
credit_payment = float(input("Введите сумму месячного платежа по кредиту: "))
utility_debt = float(input("Введите задолженность за коммунальные услуги: "))

# Вычисление общей суммы выплат
total_payments = credit_payment + utility_debt

# Вычисление остатка средств
remaining_amount = salary - total_payments

# Вывод результата
print("Сумма, которая останется у пользователя после всех выплат:", remaining_amount)



# Задание 3
# Ввод длин диагоналей от пользователя
d1 = float(input("Введите длину первой диагонали (d1): "))
d2 = float(input("Введите длину второй диагонали (d2): "))

# Вычисление площади ромба
area = (d1 * d2) / 2

# Вывод результата
print("Площадь ромба:", area)



# Задание 4
print("To be\nor not\nto be")



# Задание 5
print("“Life is what happens \nwhen \nyou’re busy making other plans” \nJohn Lennon.")