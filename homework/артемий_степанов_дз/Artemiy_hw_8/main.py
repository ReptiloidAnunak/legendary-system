# Импорт библиотек и модулей
import json
import requests
import random

from classes import Question

questions = requests.get ('https://www.jsonkeeper.com/b/PW2F')
total_count = 0

# Загрузка данных из файла


questions = questions.text
questions = json.loads (questions)

# Основной блок

questions_ex = []

for element in questions:
    '''Записывает экземпляры в класс Question'''

    element = Question (element['q'], element['d'], str (element['a']), False, '', 0)
    element.points = element.get_points ()
    questions_ex.append (element)

    random.shuffle (questions_ex)

for element in questions_ex:
    '''Выдеет вопрос, выдает ответ и оценивает его'''
    print (f'\nВопрос: {element.text} \nСложность: {element.difficulty}')
    if element.asked == False:
        element.asked = True
        user_anwer = input ('Ответ: ')
        element.user_answer = user_anwer

        if user_anwer == str (element.correct_unswer):

            total_count += element.points
            print (element.build_positive_feedback ())
        else:
            print (element.build_negative_feedback ())
            element.points = 0


def count_correct(questions_ex):
    '''Вычисляет количество правильных ответов'''

    correct_count = 0

    for element in questions_ex:
        if element.is_correct () == True:
            correct_count += 1
    return correct_count


count_correct = count_correct (questions_ex)

##################################################_ИТОГИ_#############################################################

print (f'\nВот и всё!\nОтвечено на {count_correct} вопроса из {len (questions)}\nНабрано балов: {total_count}')
