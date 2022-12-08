def load_random_word(link):
    '''Получит список слов с внешнего ресурса,
- выберет случайное слово,
- создаст экземпляр класса `BasicWord`,
- вернет этот экземпляр'''

    import requests
    import json
    import random
    from basic_word import BasicWord
    words_list = requests.get(link).text
    words_list = json.loads(words_list)
    random_word = random.sample(words_list, 1)[0]

    random_word = BasicWord(random_word['word'], random_word['subwords'])
    return random_word


def chec_len(user_answer):
    '''Проверяет длину введенного слова'''
    if len(str(user_answer)) < 3:
        return False

def escape(user_answer):
    if user_answer == 'stop':
        exit()

