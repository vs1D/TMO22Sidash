# вариант 18
# задание 1
g = (x for x in range(1, 6))
print(list(g))


# задание 2
def announce(func):
    def wrapper():
        print("Запуск")
        result = func()
        print("Готово")
        return result
    return wrapper


@announce
def hello():
    print("Привет!")


hello()
