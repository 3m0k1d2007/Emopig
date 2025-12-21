# Задание 1
basketball_players = {}

def add_player():
    name = input("Введите ФИО баскетболиста: ")
    height = int(input("Введите рост баскетболиста (в см): "))
    basketball_players[name] = height
    print(f"Баскетболист {name} добавлен в список!")

def delete_player():
    name = input("Введите ФИО баскетболиста для удаления: ")
    if name in basketball_players:
        del basketball_players[name]
        print(f"Баскетболист {name} удалён из списка!")
    else:
        print(f"Баскетболист {name} не найден в списке!")

def search_player():
    name = input("Введите ФИО баскетболиста для поиска: ")
    if name in basketball_players:
        print(f"Баскетболист {name} найден! Его рост: {basketball_players[name]} см")
    else:
        print(f"Баскетболист {name} не найден в списке!")

def replace_player():
    name = input("Введите ФИО баскетболиста для замены: ")
    if name in basketball_players:
        new_height = int(input("Введите новый рост баскетболиста (в см): "))
        basketball_players[name] = new_height
        print(f"Информация о баскетболисте {name} обновлена!")
    else:
        print(f"Баскетболист {name} не найден в списке!")

def print_players():
    print("Список баскетболистов:")
    for name, height in basketball_players.items():
        print(f"{name} — {height} см")

while True:
    print("\nМеню:")
    print("1. Добавить баскетболиста")
    print("2. Удалить баскетболиста")
    print("3. Найти баскетболиста")
    print("4. Заменить информацию о баскетболисте")
    print("5. Вывести список баскетболистов")
    print("6. Выход")
    choice = int(input("Выберите пункт меню: "))
    if choice == 1:
        add_player()
    elif choice == 2:
        delete_player()
    elif choice == 3:
        search_player()
    elif choice == 4:
        replace_player()
    elif choice == 5:
        print_players()
    elif choice == 6:
        break
    else:
        print("Неверный выбор!")



# Задание 2
dictionary = {}

def add_word():
    english_word = input("Введите слово на английском: ")
    french_translation = input("Введите перевод на французский: ")
    dictionary[english_word] = french_translation
    print(f"Слово '{english_word}' добавлено в словарь!")

def delete_word():
    english_word = input("Введите английское слово для удаления: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово '{english_word}' удалено из словаря!")
    else:
        print(f"Слово '{english_word}' не найдено в словаре!")

def search_word():
    english_word = input("Введите английское слово для поиска: ")
    if english_word in dictionary:
        print(f"Перевод слова '{english_word}': {dictionary[english_word]}")
    else:
        print(f"Слово '{english_word}' не найдено в словаре!")

def replace_word():
    english_word = input("Введите английское слово для замены: ")
    if english_word in dictionary:
        new_translation = input("Введите новый перевод: ")
        dictionary[english_word] = new_translation
        print(f"Перевод слова '{english_word}' обновлён!")
    else:
        print(f"Слово '{english_word}' не найдено в словаре!")

def print_dictionary():
    print("\nАнгло-французский словарь:")
    for word, translation in dictionary.items():
        print(f"{word} — {translation}")

while True:
    print("\nМеню:")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Найти слово")
    print("4. Заменить перевод")
    print("5. Вывести словарь")
    print("6. Выход")
    choice = int(input("Выберите пункт меню: "))
    if choice == 1:
        add_word()
    elif choice == 2:
        delete_word()
    elif choice == 3:
        search_word()
    elif choice == 4:
        replace_word()
    elif choice == 5:
        print_dictionary()
    elif choice == 6:
        break
    else:
        print("Неверный выбор!")



# Задание 3
employees = {}

def add_employee():
    name = input("ФИО: ")
    phone = input("Телефон: ")
    email = input("Рабочий email: ")
    position = input("Название должности: ")
    office_number = input("Номер кабинета: ")
    skype = input("MAX(skype): ")
    employees[name] = {
        "телефон": phone,
        "email": email,
        "должность": position,
        "кабинет": office_number,
        "skype": skype
    }
    print(f"Сотрудник {name} добавлен!")

def delete_employee():
    name = input("ФИО сотрудника для удаления: ")
    if name in employees:
        del employees[name]
        print(f"Сотрудник {name} удалён!")
    else:
        print(f"Сотрудник {name} не найден!")

def search_employee():
    name = input("ФИО сотрудника для поиска: ")
    if name in employees:
        emp = employees[name]
        print(f"\n{name}:")
        print(f"Телефон: {emp['телефон']}")
        print(f"Email: {emp['email']}")
        print(f"Должность: {emp['должность']}")
        print(f"Кабинет: {emp['кабинет']}")
        print(f"Skype: {emp['skype']}")
    else:
        print(f"Сотрудник {name} не найден!")

def replace_employee():
    name = input("ФИО сотрудника для обновления: ")
    if name in employees:
        phone = input("Новый телефон: ")
        email = input("Новый email: ")
        position = input("Новая должность: ")
        office_number = input("Новый номер кабинета: ")
        skype = input("Новый MAX(skype): ")
        employees[name] = {
            "телефон": phone,
            "email": email,
            "должность": position,
            "кабинет": office_number,
            "skype": skype
        }
        print(f"Данные сотрудника {name} обновлены!")
    else:
        print(f"Сотрудник {name} не найден!")

def print_employees():
    print("\nСписок сотрудников:")
    for name, data in employees.items():
        print(f"{name} — {data['должность']}")

while True:
    print("\nМеню:")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Найти сотрудника")
    print("4. Обновить данные сотрудника")
    print("5. Вывести список сотрудников")
    print("6. Выход")
    choice = int(input("Выберите пункт меню: "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        delete_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        replace_employee()
    elif choice == 5:
        print_employees()
    elif choice == 6:
        break
    else:
        print("Неверный выбор!")



# Задание 4
books = {}

def add_book():
    title = input("Название книги: ")
    author = input("Автор: ")
    genre = input("Жанр: ")
    year = input("Год выпуска: ")
    pages = input("Количество страниц: ")
    publisher = input("Издательство: ")
    books[title] = {
        "автор": author,
        "жанр": genre,
        "год": year,
        "страницы": pages,
        "издательство": publisher
    }
    print(f"Книга '{title}' добавлена!")

def delete_book():
    title = input("Название книги для удаления: ")
    if title in books:
        del books[title]