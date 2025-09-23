def max_even_sum(numbers):

    if not numbers:
        return 0

    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return total_sum
    
    odd_numbers = [x for x in numbers if x % 2 == 1]

    if not odd_numbers:
        return total_sum - min(numbers) if numbers else 0

    min_odd = min(odd_numbers)
    return total_sum - min_odd


def test_max_even_sum():

    assert max_even_sum([5, 7, 13, 2, 14]) == 36
    assert max_even_sum([3]) == 0


    assert max_even_sum([2, 4, 6, 8]) == 20
    assert max_even_sum([1, 3, 5]) == 8
    assert max_even_sum([1, 2, 3, 4]) == 10
    assert max_even_sum([1, 2, 3, 4, 5]) == 14
    assert max_even_sum([]) == 0
    assert max_even_sum([2]) == 2
    assert max_even_sum([1]) == 0

    print("Все тесты пройдены!")

test_max_even_sum()
numbers = list(map(int, input().split()))
print(max_even_sum(numbers))
