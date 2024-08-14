'''
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:

iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и
итератором.

Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс Cycle.
'''

class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

