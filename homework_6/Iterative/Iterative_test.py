def run_all_tests():
    print("ТЕСТЫ КОРРЕКТНОСТИ ИТЕРАТИВНЫХ АЛГОРИТМОВ")
    print("=" * 50)
    
    test_count = 0
    passed_count = 0
    

    test_count += 1
    arr = []
    expected = []
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Пустой массив")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Пустой массив")
    

    test_count += 1
    arr = [5]
    expected = [5]
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Массив из одного элемента")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Массив из одного элемента")
    

    test_count += 1
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Уже отсортированный массив")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Уже отсортированный массив")
    

    test_count += 1
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Обратно отсортированный массив")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Обратно отсортированный массив")


    test_count += 1
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = sorted(arr)
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Массив с дубликатами")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Массив с дубликатами")
    

    test_count += 1
    arr = [5, -2, 0, -8, 3, 1]
    expected = sorted(arr)
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Отрицательные числа")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Отрицательные числа")
    

    test_count += 1
    arr = [7, 7, 7, 7, 7, 7]
    expected = [7, 7, 7, 7, 7, 7]
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Все элементы одинаковые")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Все элементы одинаковые")
    

    test_count += 1
    arr = generate_random_array(500)
    expected = sorted(arr)
    try:
        assert mergesort_iterative(arr) == expected
        assert quicksort_iterative(arr) == expected
        print(f"Тест {test_count} пройден: Большой случайный массив")
        passed_count += 1
    except AssertionError:
        print(f"Тест {test_count} не пройден: Большой случайный массив")
    
    print("=" * 50)
    print(f"Пройдено тестов: {passed_count} из {test_count}")
    print("=" * 50)
    
    return passed_count == test_count

# СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ
def compare_performance():
    print("\nСРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ИТЕРАТИВНЫХ АЛГОРИТМОВ")
    print("=" * 50)
    
    test_cases = {
        "Случайный массив (2000)": generate_random_array(2000),
        "Отсортированный массив (2000)": generate_sorted_array(2000),
        "Обратно отсортированный (2000)": generate_reversed_array(2000),
        "Много дубликатов (2000)": generate_duplicates_array(2000),
        "Все одинаковые (2000)": generate_all_duplicates(2000),
        "Почти отсортированный (2000)": generate_almost_sorted_array(2000),
        "Худший случай QuickSort (2000)": generate_worst_case_quicksort(2000),
    }
    
    algorithms = [
        ("MergeSort итеративный", timed_mergesort_iterative),
        ("QuickSort итеративный", timed_quicksort_iterative),
    ]
    
    for test_name, test_data in test_cases.items():
        print(f"\n{test_name}:")
        
        times = {}
        for algo_name, algo_func in algorithms:
            try:
                result, exec_time = algo_func(test_data.copy())
                expected = sorted(test_data)
                assert result == expected
                times[algo_name] = exec_time
                print(f"  {algo_name}: {exec_time:.6f} сек")
            except Exception as e:
                times[algo_name] = float('inf')
                print(f"  {algo_name}: ошибка - {e}")
        

        valid_times = {k: v for k, v in times.items() if v != float('inf')}
        if valid_times:
            fastest = min(valid_times, key=valid_times.get)
            fastest_time = valid_times[fastest]
            print(f"  Самый быстрый: {fastest} ({fastest_time:.6f} сек)")




all_tests_passed = run_all_tests()
compare_performance()
