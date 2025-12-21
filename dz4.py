# Задание 1
# Ввод диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Вывод чисел, кратных 7
print("Числа, кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")



# Задание 2
# Ввод диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# 1. Все числа диапазона
print("1. Все числа диапазона:")
for num in range(start, end + 1):
    print(num, end=" ")
print()  # Переход на новую строку

# 2. Все числа диапазона в убывающем порядке
print("2. Все числа диапазона в убывающем порядке:")
for num in range(end, start - 1, -1):
    print(num, end=" ")
print()  # Переход на новую строку

# 3. Все числа, кратные 7
print("3. Все числа, кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")
print()  # Переход на новую строку

# 4. Количество чисел, кратных 5
count = 0
for num in range(start, end + 1):
    if num % 5 == 0:
        count += 1
print(f"4. Количество чисел, кратных 5: {count}")



# Задание 3
# Ввод диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Анализ чисел в диапазоне
for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)