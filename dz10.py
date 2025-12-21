# Задание 1
def display_quote():
    quote = """“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates"""
    print(quote)

# Вызов функции
display_quote()



# Задание 2
def print_even_numbers(start, end):
    # Сортируем числа, чтобы start всегда было меньше или равно end
    start, end = sorted((start, end))
    # Создаём список чётных чисел в диапазоне
    even_numbers = [str(num) for num in range(start, end + 1) if num % 2 == 0]
    # Выводим числа через пробел
    print(" ".join(even_numbers))

# Пример использования
print_even_numbers(1, 10)  # Выведет: 2 4 6 8 10
print_even_numbers(10, 1)   # Тоже выведет: 2 4 6 8 10 (функция работает независимо от порядка чисел)



# Задание 3
def draw_square(side_length, symbol, filled):
    # Проверяем, что длина стороны не меньше 1
    if side_length < 1:
        print("Длина стороны должна быть как минимум 1.")
        return

    # Рисуем квадрат
    for i in range(side_length):
        if filled or i == 0 or i == side_length - 1:
            # Если квадрат заполненный или это первая/последняя строка — печатаем строку из символов
            print(symbol * side_length)
        else:
            # Для пустых квадратов: печатаем символ, затем пробелы, затем символ
            print(symbol + " " * (side_length - 2) + symbol)


# Примеры использования:
draw_square(5, "*", True)  # Заполненный квадрат 5x5 из звёздочек
print()  # Пустая строка для разделения примеров
draw_square(5, "#", False)  # Пустой квадрат 5x5 из решёток