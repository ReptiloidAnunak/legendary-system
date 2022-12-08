'''База данных и глобальные переменные'''
#Импорт необходимой библиотеки

import random

#Список слов и глобальные переменные

word_list = ['Beavis', 'Butthead', 'cornholio', 'dumpling', 'chicks']
answers = []
question_number = 0
max_questions = len(word_list)

#Словарь со значениями букв и цифр в азбуке Морзе

morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

#Необходимые пользовательские функции

def encode(word):
    '''
    Кодирует слова с помощью морзянки
    '''
    encoded_word = ''
    word = word.lower()
    
    for symbol in word:
        
        if symbol in morse_dict:
            encoded_word += (morse_dict[symbol] + ' ')
    return encoded_word



def get_word(list_):
    '''
    Выдает случайное слово из списка слов
    '''
    random_word = ''
    random_word = str(random.sample(list_, 1)[0])
    return random_word


def print_statistics(answers):
    '''
    Выводит статистику ответов пользователя
    '''
    
    correct_answers = 0
    incorrect_answers = 0
    
    for mark in answers:

        if mark == True:
            correct_answers += 1
        elif mark == False:
            incorrect_answers += 1
            
    print(f'\nВсего задачек: {question_number} \nОтвечено верно: {correct_answers} \nОтвечено неверно: {incorrect_answers}')


'''Основной блок с алгоритмом программы'''

#Вступление

print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
input('Нажмите Enter и начнём')

#Цикл вопросов

while question_number != max_questions:
    question_number += 1
    word_to_code = get_word(word_list)
    question = encode(word_to_code)
    
    
    print(f'\nСлово {question_number} {question}') 
    answer = input('\nОтвет: ')
    answer = answer.lower()
    
    
    if answer == word_to_code.lower():
        answers.append(True)
        print(f'Верно,{word_to_code}')
        
    
    else:
        answers.append(False)
        print(f'Неверно,{word_to_code}')
        
    continue

################################################### Подведение итогов ###################################################

print_statistics(answers)
    
#########################################################################################################################


