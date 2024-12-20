#1 Функція без аргументів і повернення

def greet():
    print("Hello!")
# Виклик функції:
greet()

#2 Функція з аргументами

def hello(name):
    print(f"Привіт {name}")

hello(input("Введіть ім'я "))

#3 Функція з поверненням значення

def add(a, b):
    return a + b
# Виклик функції
result = add(1, 4)
print(f"Результат - {result}")

#4 Аргументи за замовчуванням

def hi(name="госте"):
    print(f"Привіт, {name}!")

hi() # Привіт, госте!
hi("Bohdan") # Привіт, Bohdan!

#5 Функція для обчислення площі і периметра прямокутника

def rectangle_area(width, height):
    """Обчислює площу прямокутника."""
    return width * height

def rectangle_perimeter(width, height):
    """Обчислює периметр прямокутника."""
    return 2 * (width + height)

# Вводимо ширину та висоту
width = float(input("Введіть ширину прямокутника: "))
height = float(input("Введіть довжину прямокутника: "))

# Обчислюємо площу
area = rectangle_area(width, height)
perimeter = rectangle_perimeter(width, height)

# Виводимо результат
print(f"Ширина і довжина прямокутника : {width} і {height}. Площа прямокутника дорівнює {area}. Периметр дорівнює: {perimeter}")