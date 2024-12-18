#1 Ітерація через діапазон чисел

for i in range(1, 6): # range(start, stop), де stop не включається
    print(i)

#2 Ітерація через список

fruits = ["apple", "banana", "peach", "grape", "pear"]

for fruit in fruits:
    print(f"Фрукт {fruit}")

#3 Ітерація через рядок

text = "Python"
for char in text:
    print(char)

#4 Використання break та continue
for num in range(1, 11):
    if num == 5: # Завершує цикл при досягненні значення 5
        break
    elif num % 2 == 0: # Пропускає ітерації для парних чисел
        continue 
    print(num)
