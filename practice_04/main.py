# Вариант 18


# Задание 1. Область видимости

x = 28

def show():
    x = 18
    print(x)

show()
print(x)

#Вывод:
# 18
# 28

# Задание 2. Args

def total(*args):
    return sum(args)

print(total(18, 19, 20))


# Задание 3. Kwargs

def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Лиза", age=19))


# Задание 4. Функция как параметр

def increase(x):
    return x + 3

def apply(func, value):
    return func(value)

print(apply(increase, 3))


# Задание 5. Рекурсия

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(3)