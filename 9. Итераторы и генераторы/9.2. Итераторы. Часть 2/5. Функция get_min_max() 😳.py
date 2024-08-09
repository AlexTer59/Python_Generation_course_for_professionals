'''
Реализуйте функцию get_min_max(), которая принимает один аргумент:

iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта
iterable, вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст, функция
должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код,
вызывающий ее.
'''

def get_min_max(iterible):
    iterator = iter(iterible)
    try:
        minimum = maximum = next(iterator)
    except StopIteration:
        return None
    for i in iterator:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum
