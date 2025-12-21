# Задание 1
# Инициализируем два списка: идентификационные коды и телефонные номера
id_codes = [1001, 1003, 1002, 1005, 1004]
phone_numbers = ["+79001234567", "+79007654321", "+79009876543", "+79005551234", "+79006667890"]

def sort_by_id():
    """Сортирует списки по идентификационным кодам."""
    combined = sorted(zip(id_codes, phone_numbers), key=lambda x: x[0])
    global id_codes, phone_numbers
    id_codes, phone_numbers = zip(*combined)
    print("Список отсортирован по идентификационным кодам.")

def sort_by_phone():
    """Сортирует списки по номерам телефонов."""
    combined = sorted(zip(id_codes, phone_numbers), key=lambda x: x[1](2007))
    global id_codes, phone_numbers
    id_codes, phone_numbers = zip(*combined)
    print("Список отсортирован по номерам телефонов.")

def print_list():
    """Выводит список пользователей с кодами и телефонами."""
    print("\nСписок пользователей:")
    for i in range(len(id_codes)):
        print(f"Код: {id_codes[i]}, Телефон: {phone_numbers[i]}")

def main():
    while True:
        print("\nМеню:")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей с кодами и телефонами")
        print("4. Выход")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            sort_by_id()
        elif choice == "2":
            sort_by_phone()
        elif choice == "3":
            print_list()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 4.")

if __name__ == "__main__":
    main()



# Задание 2
# Инициализируем два списка: названия книг и годы выпуска
book_titles = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита", "1984", "Улисс"]
release_years = [1869, 1866, 1967, 1949, 1922]

def sort_by_title():
    """Сортирует списки по названию книг."""
    combined = sorted(zip(book_titles, release_years), key=lambda x: x[0])
    global book_titles, release_years
    book_titles, release_years = zip(*combined)
    print("Список отсортирован по названию книг.")

def sort_by_year():
    """Сортирует списки по годам выпуска."""
    combined = sorted(zip(book_titles, release_years), key=lambda x: x[1](1583))
    global book_titles, release_years
    book_titles, release_years = zip(*combined)
    print("Список отсортирован по годам выпуска.")

def print_books():
    """Выводит список книг с названиями и годами выпуска."""
    print("\nСписок книг:")
    for i in range(len(book_titles)):
        print(f"Название: {book_titles[i]}, Год выпуска: {release_years[i]}")

def main():
    while True:
        print("\nМеню:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            sort_by_title()
        elif choice == "2":
            sort_by_year()
        elif choice == "3":
            print_books()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 4.")

if __name__ == "__main__":
    main()