my_list = [1, 2, 3, "Python", True]

my_list.append("Last element") # Додає елемент у кінець списку
my_list.insert(2, "new") # Додає елемент на певну позицію, в даному випадку на третю
my_list.remove("Python") # Видаляє перший знайдений елемент
removed = my_list.pop() # Видаляє останній елемент і повертає його

first = my_list[0] # Перший елемент
last = my_list[-1] # Останній елемент
sub_list = my_list[0:4] # Елементи з індекса 0 до 3

print(f"Список {my_list}, видалений елемент - {removed}")
print(f"Перший елемент списку {first}, а останній {last}")
print(f"Елементи з першого по третій {sub_list}")

#1 Список покупок

shopping_list = ["apple", "meat", "milk", "juice", "pineapple"]

shopping_list.append("Cheese")
shopping_list.insert(0, "Bread")

print(f"Список продуктів - {shopping_list}")

shopping_list.remove("milk")
last_element = shopping_list.pop()

print(f"Оновлений список - {shopping_list}")
print(f"Видаленний елемент - {last_element}")

for item in shopping_list:
    print(f"Треба купити - {item}")