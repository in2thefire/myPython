my_dict = {"ім'я" : "Богдан", "вік" : 23, "країна" : "Україна"}
print(my_dict)

name = my_dict["ім'я"]
print(name)

my_dict["професія"] = ["Програміст"]
del my_dict["країна"]
print(my_dict)

if "вік" in my_dict:
    print("Ключ існує")

for key, value in my_dict.items():
    print(f"{key} : {value}")

#1  Список покупок із кількістю

shopping_dict = {"хліб": 1, "молоко": 2, "яйця": 10}

# Додаємо новий продукт
shopping_dict["сир"] = 1

# Видаляємо "хліб"
del shopping_dict["хліб"]

# Виводимо оновлений список покупок
for product, quantity in shopping_dict.items():
    print(f"{product}: {quantity} шт.")