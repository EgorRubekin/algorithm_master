def is_palindrome(n):
    if n < 0:
        return False
    if n < 10:
        return True

    original = n
    reversed_num = 0

    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10

    return original == reversed_num


# Тесты
def test_palindrome():

    assert is_palindrome(121) == True, "Ошибка для 121"
    assert is_palindrome(131) == True, "Ошибка для 131"
    assert is_palindrome(7) == True, "Ошибка для 7"
    assert is_palindrome(0) == True, "Ошибка для 0"
    assert is_palindrome(12321) == True, "Ошибка для 12321"


    assert is_palindrome(31) == False, "Ошибка для 31"
    assert is_palindrome(123) == False, "Ошибка для 123"
    assert is_palindrome(1234) == False, "Ошибка для 1234"

    print("Все тесты пройдены успешно!")



test_palindrome()


number = int(input("Введите число для проверки: "))
result = is_palindrome(number)
print(result)
