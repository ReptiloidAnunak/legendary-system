'''Импрорт необходимых библиотек'''

import random

'''Глобальные переменные'''

users_score_base = {}
games_count = 0

'''Необходимые пользовательские функции'''


def mix_letters(word):
    '''Смешивает буквы в загаданном слове'''
    letters_list = []

    for letter in word:
        letters_list += letter
    random.shuffle(letters_list)
    hidden_word = ''.join(letters_list)

    return hidden_word


'''Основной модуль'''

while True:
    username = input('Введите ваше имя: ')
    users_score_base[username] = 0
    if username != '0':
        with open('words.txt', 'rt') as word_list:

            for word in word_list:
                word = word.rstrip('\n')
                word_for_question = mix_letters(word)
                print(f'Угадайте слово: {word_for_question}')
                answer = input('Ответ: ').lower()

                if answer == word:
                    users_score_base[username] += 10
                    print('Верно! Вы получаете 10 баллов!')
                else:
                    print(f'Неверно! Верный ответ - {word}')

            with open('history.txt', 'w') as file:
                file.write(str(users_score_base))
            games_count += 1
            print('Если хотите закончить игру, нажмите 0')

    else:
        break

###################################__Итоги игры__######################################################
with open('history.txt', 'r') as file:
    gamers_results = {}
    for line in file:
        gamers_results = eval(line)

    for key, value in gamers_results.items():
        print(f'{key} : {value}')

    max_result = max(gamers_results.values())

print(f'Всего игр сыграно: {games_count}\nМаксимальный рекорд: {max_result}')
########################################################################################################
