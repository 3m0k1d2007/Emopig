# =============================== 1 задание =============================

start = int(input("введите начало диапазона: "))
end = int(input("введите конец диапазона: "))

if start > end:
    start, end = end, start
for num in range(start, end+1):
    if num % 7 == 0:
        print(num)


# =============================== 2 задание =============================
a = int(input("введите первое число:"))
b = int(input("введите второе число:"))
start = min(a, b)
end = max(a, b)

print("\n1. Все числа диапазона:")
for i in range(start, end + 1):
    print(i, end=" ")

print("\n\n2. Все числа в убывающем порядке:")
for i in range(end, start - 1, -1):
    print(i, end=" ")

print("\n\n3. Числа, кратные 7:")
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=" ")

print("\n\n4. Количество чисел, кратных 5:")
count = 0
for i in range(start, end + 1):
    if i % 5 == 0:
        count += 1
print(count)
# =============================== 3 задание ==============================

start = int(input("введите начало диапазона: "))
end = int(input("введите конец диапазона: "))
start, end = sorted((start, end))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)