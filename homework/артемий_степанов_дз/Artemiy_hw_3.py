'''Глобальные переменные'''
words = {}
answers = {}
count = 0

'''Словари с данными'''
levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

'''Словарь для доступа к базам данных в зависимости от выбранного уровня'''
difficulty_levels = {
    'легкий' : words_easy, 
    'средний' : words_medium, 
    'сложный' : words_hard
}

'''Стартовый блок с выбором уровня сложности'''

while True:
    print('Выберите уровень сложности:')
    print('Лёгкий, средний, сложный')
    level_choice = input()
    level_choice = level_choice.lower()
    level_choice = level_choice.replace('ё','е')
    
    if level_choice in difficulty_levels.keys():
        break
    else:
        continue



words = difficulty_levels[level_choice]

'''Основной блок'''
    
for k,v in words.items():
    print('\nНажмите Enter.')
    input()
    print(f'{k}, {len(v)} букв, начинается на {v[0]}...')
    user_answer = input()
    user_answer.lower()
        
    if user_answer == v:
        answers[k] = True
        count += 1
        print(f'Верно, {k.capitalize()} это {v}.')
            
    else:
        answers[k] = False
        print(f'Неверно. {k.capitalize()} это {v}')
               

'''Подведение итогов'''
    
print('\nПравильно отвеченные слова:')
for k,v in answers.items():
    if answers[k] == True:
        print(k)

print('\nНеравильно отвеченные слова:')
for k,v in answers.items():
    if answers[k] == False:
        print(k)

print(f'\nВаш ранг:\n{levels[count]}')



