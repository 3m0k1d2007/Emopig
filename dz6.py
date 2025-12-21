# Задание 1
def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Пример использования
my_list = [1, 2, 3, 4, 5]
result = calculate_product(my_list)
print(f"Произведение элементов списка: {result}")



# Задание 2
def find_minimum(numbers):
    if not numbers:  # Проверка на пустой список
        return None
    minimum = numbers[0]  # Предполагаем, что первый элемент — минимальный
    for number in numbers[1:]:  # Сравниваем с остальными элементами
        if number < minimum:
            minimum = number
    return minimum

# Пример использования
my_list = [5, 2, 8, 1, 9]
min_value = find_minimum(my_list)
print(f"Минимальное значение в списке: {min_value}")



# Задание 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count

# Пример использования
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_count = count_primes(my_list)
print(f"Количество простых чисел в списке: {prime_count}")



# Задание 4
def remove_number(numbers, target):
    count = 0
    while target in numbers:
        numbers.remove(target)
        count += 1
    return count

# Пример использования
my_list = [1, 2, 3, 2, 4, 2, 5]
target_number = 2
removed_count = remove_number(my_list, target_number)
print(f"Удалено элементов: {removed_count}")
print(f"Обновлённый список: {my_list}")



# Задание 5
def merge_lists(list1, list2):
    return list1 + list2

# Пример использования
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print(f"Объединённый список: {merged_list}")



# Задание 6
def power_list(numbers, exponent):
    return [number ** exponent for number in numbers]

# Пример использования
my_list = [1, 2, 3, 4]
exponent = 2
powered_list = power_list(my_list, exponent)
print(f"Список после возведения в степень {exponent}: {powered_list}")