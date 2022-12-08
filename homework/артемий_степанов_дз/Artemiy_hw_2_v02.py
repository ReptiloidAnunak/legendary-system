__version__ = '0.2'

'''Первоначальные данные'''
quetion_number = 3
score_count = 0
quetion_count = 0
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

'''Приветствие'''

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
start_answer = input()
corrtect_start_answer = 'ready'


while True:
    if start_answer == corrtect_start_answer:
        pass
    else:
        print('Кажется, вы не хотите играть. Очень жаль.')
        break
 

        '''Основная часть'''


    for num_q in range(len(questions)):


    	print(questions[num_q])
    	user_answer = input('Ответ: ')
	
    	if user_answer == answers[num_q]:
	    	print('Ответ верный!')
	    	quetion_count += 1
	    		

    	else:
		    print(f'Неправильно. Правильный ответ: {answers[num_q]}')
#######################################################################################
    pecent_correct = round(float(quetion_count / (quetion_number / 100)))
    print(f'\nВот и все! Вы ответили на {quetion_count} вопросов из {quetion_number} верно. Это {pecent_correct} процентов.')
    break
#######################################################################################



