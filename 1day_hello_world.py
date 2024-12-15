import datetime

#1
a = "world"
print(f"hello, {a}")

#2
name = input("Введіть своє ім'я ")
age = input("Введіть свій вік ")
city = input("Введіть з якого ви міста ")

print(f"Привіт {name}, я вже знаю, що тобі {age} і що ти родом з {city}")

#3
name = input("Введіть своє ім'я ")
current_hour = datetime.datetime.now().hour  # Отримуємо поточну годину

if 5 <= current_hour < 12:
    greetings = "Добрий ранок"
elif 12 <= current_hour < 18:
    greetings = "Добрий день"
else: 
    greetings = "Добрий вечір"

print(f"{greetings},{name}!")

