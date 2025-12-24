# ========================================= 1 ================================
from random import randint
n = 10
mylist = []
for i in range (n):
   mylist.append(randint(1,99))
print(f"неотсортированный список: {mylist}")
i = 0 # первая ячейка
while i < n - 1: # пока i меньше последнего элемента
    m = i # индекс ячейки с минимальным значением
    j = i + 1 # поиск осуществляем со следующей ячейки
    while j < n:
        if mylist [j] < mylist [m]:
            m = j # сохраняем в m номер найденного минимума
        j += 1
    mylist[i] , mylist[m] =  mylist[m] , mylist[i]
    i += 1
print(f"отсортированный список: {mylist}")

# ========================================= 2 ================================

mylist = ["apple" , "banana" , "cherry" , "date" , "apricot"]
print(f"неотсортированный список: {mylist}")
from random import randint

# ========================================= 3 ================================
print("Задание №3: ")
N = 15
mylist = [randint(1, 100) for _ in range(N)]
print(f"Неотсортированный список: {mylist}")

iterations = 0

for i in range(1, N):
    key = mylist[i]
    j = i - 1
    while j >= 0 and mylist[j] < key:
        mylist[j + 1] = mylist[j]
        j -= 1
        iterations += 1
    mylist[j + 1] = key
    iterations += 1

print(f"Отсортированный список (по убыванию): {mylist}")
print(f"Количество итераций: {iterations}")
print("--"*50)

# ========================================= 4 ================================
print("ЗАДАНИЕ 4:")

words = ["apple", "banana", "cherry", "date", "apricot"]
print("Исходный список:", words)

n = len(words)
j = 0
for i in range(1, n):
    key = words[i]#apple
    j = i - 1#1-1 0
    # Сдвигаем элементы вправо, пока они больше key
    while j >= 0 and words[j] > key:
        words[j + 1] = words[j]
        j -= 1
    words[j + 1] = key

print("Отсортированный список:", words)
print("--"*50)

# ========================================= 5 ================================
print("ЗАДАНИЕ 5:")
arr = [10, 3, 8, 1, 7, 5, 9, 2, 6, 4]
k = 3

print("Исходный массив:", arr)
fixed_value = arr[k]
print(f"Фиксируем элемент на индексе {k}: {fixed_value}")

other_elements = []
for i in range(len(arr)):
    if i != k:
        other_elements.append(arr[i])

n = len(other_elements)
for i in range(n):
    for j in range(0, n - i - 1):
        if other_elements[j] > other_elements[j + 1]:
            other_elements[j], other_elements[j + 1] = other_elements[j + 1], other_elements[j]

left_part = other_elements[:k]
right_part = other_elements[k:]

result = left_part + [fixed_value] + right_part

print("Результат:", result)