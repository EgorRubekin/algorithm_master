def count_primes(n):
    if n <= 2:
        return 0


    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    # Решето Эратосфена
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)


def test_count_primes():

    assert count_primes(10) == 4
    assert count_primes(1) == 0

    assert count_primes(0) == 0
    assert count_primes(2) == 0
    assert count_primes(3) == 1
    assert count_primes(4) == 2
    assert count_primes(20) == 8
    assert count_primes(30) == 10
    assert count_primes(100) == 25
    assert count_primes(-5) == 0

    print("Все тесты пройдены!")

test_count_primes()
n = int(input().strip())
print(count_primes(n))
