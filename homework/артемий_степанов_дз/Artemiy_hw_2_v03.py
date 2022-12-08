__version__ = '0.3'

'''Инициализация основных переменных'''

quetion_number = 3
score_count = 0
quetion_count = 0
questions = ["\nMy name ___ Vova", "\nI ___ a coder", "\nI live ___ Moscow"]
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

        attemps_count = 0
        max_attemps = 3
        
        print(questions[num_q])
        user_answer = input('\nОтвет: ')

        attemps_count += 1
        quetion_count += 1

        #Верный ответ с первого раза
    
        if user_answer == answers[num_q] and attemps_count == 1:
            print('Ответ верный!')
            score_count += 3


        else: #Ответы с нескольких попыток

            while user_answer != answers[num_q]:
                remaining_attemps = max_attemps - attemps_count
                if remaining_attemps > 0:
                    print(f'Осталось попыток: {remaining_attemps}, попробуйте еще раз!')
                    user_answer = input('\nОтвет: ')
                    attemps_count += 1
                    
                else:
                     quetion_count -= 1
                     print(f'Увы, но нет. Правильный ответ: {answers[num_q]}')
                     break


                
            if user_answer == answers[num_q] and attemps_count == 2:
                print('Ответ верный!')
                score_count += 2
                    

            elif user_answer == answers[num_q] and attemps_count == 3:
                        print('Ответ верный!')
                        score_count += 1
                       
                  
            
######################################Результат#########################################
    pecent_correct = round(float(quetion_count / (quetion_number / 100)))
    print(f'\nВот и все! Вы ответили на {quetion_count} вопросов из {quetion_number} верно, вы набрали {score_count} баллов.')
    break
########################################################################################

