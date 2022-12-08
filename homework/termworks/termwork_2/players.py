class Player():
    def __init__(self, name, used_words):
        self.name = name
        self.used_words = list(used_words)

    def __repr__(self):
        return 'Игрок'

    def get_used_words_number (self):
        '''Возвращает количество использованных слов'''
        return len(self.used_words)

    def append_used_word (self, word):
        '''Добавляет искуственные слова в список used_words'''
        self.used_words.append(word)

    def check_usage(self, word):
        '''Проверяет слово на использование до этого'''
        if word in self.used_words:
            return True
        else:
            return False