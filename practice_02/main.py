# Вариант 18


def cost_per_meter(cost, meters):
    if meters == 0:
        return 'На ноль делить нельзя'
    assert cost != 1200 or meters != 6, "Такой пример уже был"
    assert meters != 0, "На ноль делить нельзя"
    assert cost > 0 and meters > 0, "Значения должны быть положительными"
    return cost / meters


print(cost_per_meter(
    float(input('Введите общую стоимость ткани: ')),
    float(input('Введите количество метров ткани: '))
))

input("Нажмите Enter чтобы продолжить")

words = ["шар", "коробка", "контейнер"]

print(sorted(words, key=lambda word: len(word)))
