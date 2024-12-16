#1 Друк чисел від 1 до 5
count = 1

while count <= 10:
    print(count)
    count += 1 # Збільшуємо змінну на 1

#2 Нескінченний цикл (завершення через break)

while True:  # Нескінченний цикл
    user_input = input("Введіть 'стоп' для завершення: ")
    if user_input.lower() == "стоп":
        print("Цикл завершено")
        break  # Завершує цикл

#3 Пропуск ітерації (continue)

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue  # Пропускає парні числа
    print(number)  # Виведе 1, 3, 5, 7, 9