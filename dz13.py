# Задание 1
# Исходные четыре списка целых чисел
list1 = [1, 5, 3, 9]
list2 = [2, 6, 8, 4]
list3 = [7, 3, 5, 1]
list4 = [9, 2, 6, 7]

# Объединение четырёх списков в пятый
combined_list = list1 + list2 + list3 + list4

# Вывод объединённого списка
print("Объединённый список:", combined_list)

# Запрос у пользователя порядка сортировки
sort_choice = input("Выберите порядок сортировки: 'возр' для возрастания, 'убыв' для убывания: ")

# Сортировка списка в зависимости от выбора пользователя
if sort_choice == "возр":
    combined_list.sort()
    print("Список, отсортированный по возрастанию:", combined_list)
elif sort_choice == "убыв":
    combined_list.sort(reverse=True)
    print("Список, отсортированный по убыванию:", combined_list)
else:
    print("Неверный выбор. Список не отсортирован.")

# Линейный поиск значения, введённого пользователем
search_value = int(input("Введите значение для поиска: "))
found = False

for i, value in enumerate(combined_list):
    if value == search_value:
        print(f"Значение {search_value} найдено на позиции {i}.")
        found = True
        break

if not found:
    print(f"Значение {search_value} не найдено в списке.")



# Задание 2
# Исходные четыре списка целых чисел
list1 = [1, 5, 3, 9]
list2 = [2, 6, 8, 4]
list3 = [7, 3, 5, 1]
list4 = [9, 2, 6, 7]

# Объединение уникальных элементов из четырёх списков
unique_elements = []

# Добавляем элементы из list1, которых нет в других списках
for item in list1:
    if item not in list2 and item not in list3 and item not in list4:
        unique_elements.append(item)

# Добавляем элементы из list2, которых нет в list1, list3 и list4
for item in list2:
    if item not in list1 and item not in list3 and item not in list4:
        unique_elements.append(item)

# Повторяем для list3 и list4
for item in list3:
    if item not in list1 and item not in list2 and item not in list4:
        unique_elements.append(item)

for item in list4:
    if item not in list1 and item not in list2 and item not in list3:
        unique_elements.append(item)

print("Уникальные элементы:", unique_elements)

# Запрос у пользователя порядка сортировки
sort_choice = input("Выберите порядок сортировки: 'возр' для возрастания, 'убыв' для убывания: ")

# Сортировка списка в зависимости от выбора пользователя
if sort_choice == "возр":
    unique_elements.sort()
    print("Уникальные элементы, отсортированные по возрастанию:", unique_elements)
elif sort_choice == "убыв":
    unique_elements.sort(reverse=True)
    print("Уникальные элементы, отсортированные по убыванию:", unique_elements)
else:
    print("Неверный выбор. Список не отсортирован.")

# Бинарный поиск значения, введённого пользователем
search_value = int(input("Введите значение для поиска: "))

# Бинарный поиск работает только на отсортированном списке, поэтому сортируем
unique_elements.sort()

left, right = 0, len(unique_elements) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if unique_elements[mid] == search_value:
        print(f"Значение {search_value} найдено на позиции {mid}.")
        found = True
        break
    elif unique_elements[mid] < search_value:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print(f"Значение {search_value} не найдено в списке.")