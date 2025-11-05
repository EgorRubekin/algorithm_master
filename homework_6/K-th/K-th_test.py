def run_tests():
    print("ТЕСТЫ АЛГОРИТМА QUICKSELECT")
    print("=" * 50)
    
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([5, 5, 5, 5], 2, 5),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 3, 3),
        ([5, 4, 3, 2, 1], 2, 4),
        ([10, 20, 30, 40, 50], 5, 10),
        ([7, 10, 4, 3, 20, 15], 3, 10),
        ([7, 10, 4, 3, 20, 15], 4, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5, 6),
    ]
    
    algorithms = [
        ("Рекурсивный", find_kth_largest),
        ("Итеративный", find_kth_largest_iterative),
    ]
    
    all_passed = True
    test_count = 0
    
    for nums, k, expected in test_cases:
        test_count += 1
        print(f"Тест {test_count}: массив {nums}, k={k}, ожидаем {expected}")
        
        for algo_name, algo_func in algorithms:
            test_nums = nums.copy()
            result = algo_func(test_nums, k)
            if result == expected:
                print(f"  {algo_name}: пройден")
            else:
                print(f"  {algo_name}: НЕ ПРОЙДЕН - получено {result}")
                all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ")
    else:
        print("НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")
    print("=" * 50)


def test_large_arrays():
    print("\nТЕСТЫ НА БОЛЬШИХ МАССИВАХ")
    print("=" * 50)
    
    large_array = [random.randint(1, 100000) for _ in range(10000)]
    k = 500
    
    algorithms = [
        ("Рекурсивный", find_kth_largest),
        ("Итеративный", find_kth_largest_iterative),
    ]
    
    for algo_name, algo_func in algorithms:
        test_nums = large_array.copy()
        result = algo_func(test_nums, k)
        
        sorted_array = sorted(large_array)
        expected = sorted_array[-k]
        
        if result == expected:
            print(f"{algo_name}: пройден - результат {result}")
        else:
            print(f"{algo_name}: НЕ ПРОЙДЕН - получено {result}, ожидалось {expected}")

run_tests()
test_large_arrays()