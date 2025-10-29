@tracer
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

@tracer
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@tracer
def sum_digits(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def test_factorial():
    result = factorial(5)
    assert result == 120
    print("Тест 1 пройден")

def test_fibonacci():
    result = fibonacci(4)
    assert result == 3
    print("Тест 2 пройден")

def test_sum_digits():
    result = sum_digits(123)
    assert result == 6
    print("Тест 3 пройден")

def test_edge_cases():
    assert factorial(0) == 1, "Факториал 0"
    assert factorial(1) == 1, "Факториал 1"
    assert fibonacci(0) == 0, "Фибоначчи 0"
    assert fibonacci(1) == 1, "Фибоначчи 1"
    assert sum_digits(0) == 0, "Сумма цифр 0"
    assert sum_digits(5) == 5, "Сумма цифр 5"
    print("Тест 4 пройден")

if __name__ == "__main__":
    test_factorial()
    test_fibonacci()
    test_sum_digits()
    test_edge_cases()
    print("Все тесты пройдены!")