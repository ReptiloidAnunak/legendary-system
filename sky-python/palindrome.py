def is_palindrome(word):
    word = word.replace(' ', '').lower()
    word_revesed = word[::-1]
    if word == word_revesed:
        return True
    else:
        return False

# Код вашей функции должен быть выше

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")