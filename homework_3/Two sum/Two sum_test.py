
def test_two_sum():


    print("=" * 60)
    print("ТЕСТИРОВАНИЕ TWO SUM")
    print("=" * 60)


    print("\nТест 1: Базовый случай из условия")
    arr1 = [1, 3, 4, 10]
    k1 = 7
    result1 = two_sum(arr1, k1)
    expected1 = "1, 2"
    print(f"Вход: arr = {arr1}, k = {k1}")
    print(f"Ожидается: {expected1}")
    print(f"Результат: {result1}")
    assert result1 == expected1, f"Ожидалось '{expected1}', получено '{result1}'"



    print("\nТест 2: Второй случай из условия")
    arr2 = [5, 5, 1, 4]
    k2 = 10
    result2 = two_sum(arr2, k2)
    expected2 = "0, 1"
    print(f"Вход: arr = {arr2}, k = {k2}")
    print(f"Ожидается: {expected2}")
    print(f"Результат: {result2}")
    assert result2 == expected2, f"Ожидалось '{expected2}', получено '{result2}'"



    print("\nТест 3: Отрицательные числа")
    arr3 = [-3, 4, 3, 90]
    k3 = 0
    result3 = two_sum(arr3, k3)
    expected3 = "0, 2"
    print(f"Вход: arr = {arr3}, k = {k3}")
    print(f"Ожидается: {expected3}")
    print(f"Результат: {result3}")
    assert result3 == expected3, f"Ожидалось '{expected3}', получено '{result3}'"



    print("\nТест 4: Большие числа")
    arr4 = [1000000, 500000, 1500000]
    k4 = 2000000
    result4 = two_sum(arr4, k4)
    expected4 = "1, 2"
    print(f"Вход: arr = {arr4}, k = {k4}")
    print(f"Ожидается: {expected4}")
    print(f"Результат: {result4}")
    assert result4 == expected4, f"Ожидалось '{expected4}', получено '{result4}'"



    print("\nТест 5: Минимальная длина массива")
    arr5 = [2, 7]
    k5 = 9
    result5 = two_sum(arr5, k5)
    expected5 = "0, 1"
    print(f"Вход: arr = {arr5}, k = {k5}")
    print(f"Ожидается: {expected5}")
    print(f"Результат: {result5}")
    assert result5 == expected5, f"Ожидалось '{expected5}', получено '{result5}'"



    print("\nТест 6: Ноль в сумме")
    arr6 = [0, 4, 3, 0]
    k6 = 0
    result6 = two_sum(arr6, k6)
    expected6 = "0, 3"
    print(f"Вход: arr = {arr6}, k = {k6}")
    print(f"Ожидается: {expected6}")
    print(f"Результат: {result6}")
    assert result6 == expected6, f"Ожидалось '{expected6}', получено '{result6}'"



    print("\nТест 7: Сумма в конце массива")
    arr7 = [1, 2, 3, 4, 5, 6]
    k7 = 11
    result7 = two_sum(arr7, k7)
    expected7 = "4, 5"
    print(f"Вход: arr = {arr7}, k = {k7}")
    print(f"Ожидается: {expected7}")
    print(f"Результат: {result7}")
    assert result7 == expected7, f"Ожидалось '{expected7}', получено '{result7}'"



    print("\nТест 8: Сумма в начале массива")
    arr8 = [8, 2, 1, 7, 3]
    k8 = 10
    result8 = two_sum(arr8, k8)
    expected8 = "0, 1"
    print(f"Вход: arr = {arr8}, k = {k8}")
    print(f"Ожидается: {expected8}")
    print(f"Результат: {result8}")
    assert result8 == expected8, f"Ожидалось '{expected8}', получено '{result8}'"



    print("\nТест 9: Смешанные положительные и отрицательные")
    arr9 = [-1, -2, -3, -4, -5]
    k9 = -8
    result9 = two_sum(arr9, k9)
    expected9 = "2, 4"
    print(f"Вход: arr = {arr9}, k = {k9}")
    print(f"Ожидается: {expected9}")
    print(f"Результат: {result9}")
    assert result9 == expected9, f"Ожидалось '{expected9}', получено '{result9}'"



    print("\nТест 10: Повторяющиеся числа (не пара)")
    arr10 = [3, 3, 2, 4]
    k10 = 6
    result10 = two_sum(arr10, k10)
    expected10 = "0, 1"
    print(f"Вход: arr = {arr10}, k = {k10}")
    print(f"Ожидается: {expected10}")
    print(f"Результат: {result10}")
    assert result10 == expected10, f"Ожидалось '{expected10}', получено '{result10}'"



    print("\nТест 11: Последовательные индексы")
    arr11 = [1, 2, 3, 4]
    k11 = 5
    result11 = two_sum(arr11, k11)
    expected11 = "1, 2"
    print(f"Вход: arr = {arr11}, k = {k11}")
    print(f"Ожидается: {expected11}")
    print(f"Результат: {result11}")
    assert result11 == expected11, f"Ожидалось '{expected11}', получено '{result11}'"




test_two_sum()