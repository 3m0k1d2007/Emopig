# Задание 1
import random

class Number:
    def __init__(self, length=15):
        # Создаём список случайных целых чисел
        self.numbers = [random.randint(-100, 100) for _ in range(length)]

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

    def sort_list(self):
        avg = self.calculate_average()
        n = len(self.numbers)

        # Определяем границы для первой трети и двух третей
        third = n // 3
        two_thirds = 2 * third

        if avg > 0:
            # Сортируем первые две трети по возрастанию
            self.numbers[:two_thirds] = sorted(self.numbers[:two_thirds])
            # Остальную часть располагаем в обратном порядке
            self.numbers[two_thirds:] = self.numbers[two_thirds:][::-1]
        else:
            # Сортируем только первую треть по возрастанию
            self.numbers[:third] = sorted(self.numbers[:third])
            # Остальную часть располагаем в обратном порядке
            self.numbers[third:] = self.numbers[third:][::-1]

    def get_list(self):
        return self.numbers

# Пример использования
num = Number()
print("Исходный список:", num.get_list())
num.sort_list()
print("Отсортированный список:", num.get_list())



# Задание 2
def main():
    # Инициализация списка оценок (10 оценок от 1 до 12)
    grades = [random.randint(1, 12) for _ in range(10)]

    while True:
        print("\nМеню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Проверка на стипендию")
        print("4. Сортировка оценок")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("Оценки студента:", grades)

        elif choice == "2":
            index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
            if 0 <= index < 10:
                new_grade = int(input("Введите новую оценку (1-12): "))
                if 1 <= new_grade <= 12:
                    grades[index] = new_grade
                    print("Оценка обновлена.")
                else:
                    print("Ошибка: оценка должна быть от 1 до 12.")
            else:
                print("Ошибка: неверный номер оценки.")

        elif choice == "3":
            average = sum(grades) / len(grades)
            if average >= 10.7:
                print(f"Средний балл: {average:.2f}. Стипендия положена!")
            else:
                print(f"Средний балл: {average:.2f}. Стипендия не положена.")

        elif choice == "4":
            sort_order = input("Введите 'возр' для сортировки по возрастанию или 'убыв' для убывания: ")
            if sort_order == "возр":
                grades.sort()
            elif sort_order == "убыв":
                grades.sort(reverse=True)
            else:
                print("Ошибка: неверный порядок сортировки.")
            print("Отсортированные оценки:", grades)

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Ошибка: неверный пункт меню.")

if __name__ == "__main__":
    main()



# Задание 3
def bubble_sort_advanced(arr):
    n = len(arr)
    for i in range(n):
        swaps = 0  # Счётчик перестановок
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  # Увеличиваем счётчик при перестановке
        if swaps == 0:  # Если перестановок не было, список отсортирован
            print("Список уже отсортирован, дальнейшая сортировка не требуется.")
            break
    return arr

# Пример использования
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", unsorted_list)
sorted_list = bubble_sort_advanced(unsorted_list.copy())
print("Отсортированный список:", sorted_list)