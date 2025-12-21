# Задание 1
import random

# Создаём список из 20 случайных элементов в диапазоне от -10 до 10
initial_list = [random.randint(-10, 10) for _ in range(20)]

print("Начальный список:", initial_list)

# Разделяем список на две половины
mid = len(initial_list) // 2
left_half = initial_list[:mid]
right_half = initial_list[mid:]

# Сортируем левую половину по возрастанию, правую — по убыванию
left_half.sort()
right_half.sort(reverse=True)

# Объединяем половины
result_list = left_half + right_half

print("Результат сортировки:", result_list)



# Задание 2
import random

# Создаём список из 45 случайных элементов в диапазоне от -20 до 20
initial_list = [random.randint(-20, 20) for _ in range(45)]

print("Начальный список:", initial_list)

# Разделяем список на три части (по 15 элементов)
part1 = initial_list[:15]
part2 = initial_list[15:30]
part3 = initial_list[30:]

# 1/3 списка — только чётные элементы
even_elements = [x for x in part1 if x % 2 == 0]

# 2/3 — только max и min, которые чередуются
max_val = max(part2)
min_val = min(part2)
alternating = []
for i in range(15):  # заполняем 15 элементов
    if i % 2 == 0:
        alternating.append(max_val)
    else:
        alternating.append(min_val)

# 3/3 — только нечётные элементы
odd_elements = [x for x in part3 if x % 2 != 0]

# Дополняем списки до 15 элементов, если необходимо (например, случайными значениями из диапазона)
while len(even_elements) < 15:
    even_elements.append(random.choice([x for x in range(-20, 21) if x % 2 == 0]))

while len(odd_elements) < 15:
    odd_elements.append(random.choice([x for x in range(-20, 21) if x % 2 != 0]))

# Объединяем все части
result_list = even_elements + alternating + odd_elements

print("Результат сортировки:", result_list)