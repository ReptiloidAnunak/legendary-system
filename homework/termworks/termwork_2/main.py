# Импорт модулей
from players import Player
from utils import load_random_word, chec_len, escape

# Глобальные переменные
array_link = 'https://www.jsonkeeper.com/b/YHZK'
word = load_random_word(array_link)
stages = 0
print (word.possible)

# Стартовая логика
print('Введите имя игрока:')
player = input()
player = Player(player, [])
print (f'Привет, {player.name}!')

print(f'Составьте {word.count_subwords ()} слов из слова {str (word.original).upper ()}\nСлова должны быть не короче 3 букв')
print ('Чтобы закончить игру, угадайте все слова или напишите "stop"\nПоехали, ваше первое слово?')

# Основной блок

while stages != word.count_subwords():
    user_answer = input().lower()

    if chec_len(user_answer) == False:
        print('слишком короткое слово')
        continue

    escape(user_answer)

    if player.check_usage(user_answer) == True:
        print('Уже использовано')
        continue

    if user_answer in word.possible and player.check_usage(user_answer) == False:
        player.append_used_word(user_answer)
        stages += 1
        print(stages)

    else:

        print('неверно')
        pass

######################___Итоги___##########################################
print(f'Игра завершена! Вы угадали {stages} слов')
