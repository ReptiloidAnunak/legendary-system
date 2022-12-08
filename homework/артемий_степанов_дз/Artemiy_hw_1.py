__version__ = '0.1'

'''Первоначальные данные'''
quetion_number = 3
score_count = 0
quetion_count = 0


'''Приветствие'''
print('\nПривет! Предлагаю проверить свои знания английского!\nРасскажи, как тебя зовут!')
user_name = input('\nИмя: ')

print(f'\nПривет, {user_name}, начинаем тренировку!')


'''Код-блоки вопросов'''

quetion_1 = 'My name ___ Vova'
print ('\n1. ' + quetion_1)
answer = input('\nОтвет: ')
correct_answer_1 = 'is'


if answer == correct_answer_1:
	print('\nОтвет верный!\nВы получаете 10 баллов!')
	score_count += 10
	quetion_count += 1
else:
	print(f'\nНеправильно.\nПравильный ответ: {correct_answer_1}')



quetion_2 = 'I ___ a coder'
print ('\n2. ' + quetion_2)
answer = input('\nОтвет: ')
correct_answer_2 = 'am'


if answer == correct_answer_2:
	print('\nОтвет верный!\nВы получаете 10 баллов!')
	score_count += 10
	quetion_count += 1
else:
	print(f'\nНеправильно.\nПравильный ответ: {correct_answer_2}')



quetion_3 = 'I live ___ Moscow'
print ('\n3. ' + quetion_3)
answer = input('\nОтвет: ')
correct_answer_3 = 'in'


if answer == correct_answer_3:
	print('\nОтвет верный!\nВы получаете 10 баллов!')
	score_count += 10
	quetion_count += 1
else:
	print(f'\nНеправильно.\nПравильный ответ: {correct_answer_3}')

'''Результаты'''

#######################################################################################
print(f'\nВот и все, {user_name}!\nВы ответили на {quetion_count} вопросов из 3 верно.')
print(f'\nВы заработали {score_count} баллов.')
pecent_correct = round(float(quetion_count / (quetion_number / 100)), 2)
print(f'Это {pecent_correct} процентов.')
#######################################################################################