'''
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.
'''



class Alphabet:
    def __init__(self, language):
        self.language = language
        self.iterator = self.create_iter()

    def create_iter(self):
        if self.language == 'ru':
            return iter(range(1072, 1104))
        else:
            return iter(range(97, 123))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return chr(next(self.iterator))
        except StopIteration:
            self.iterator = self.create_iter()
            return chr(next(self.iterator))



