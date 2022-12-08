class BasicWord():
    def __init__(self, original, possible):
        self.original = original
        self.possible = possible

    def __repr__(self):
        return 'Вопрос'


    def count_subwords(self):
        '''Получение количества использованных слов (возвращает int)'''
        return len(self.possible)
