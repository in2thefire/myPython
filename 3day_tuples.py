my_tuple = (1, 2, 3, "Python", True)

first = my_tuple[0]

my_list = list(my_tuple) # Перетворюємо кортеж у список
new_tuple = tuple(my_list) # Перетворюємо список у кортеж

print(f"Мій кортеж - {my_tuple}")
print(f"Список який був перетворений з кортежа - {my_list}")
print(f"Новий кортеж який ми перетворили з списка - {new_tuple}")

#1 Продукти з цінами

products = (("Хліб", 20),("Молоко", 35),("Сир", 41))

for product, price in products:
    print(f"Продукт - {product}, ціна - {price}")