from pin import check_pin

print('Введите ваш Пинкод')

user_input = input()

if check_pin(user_input) == True:
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")
