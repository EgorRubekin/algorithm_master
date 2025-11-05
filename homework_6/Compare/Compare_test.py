print("ЗАПУСК ТЕСТОВ КОРРЕКТНОСТИ")
print("=" * 60)


arr = []
expected = []
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 1: Пустой массив - пройден")


arr = [5]
expected = [5]
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 2: Массив из одного элемента - пройден")


arr = [1, 2, 3, 4, 5]
expected = [1, 2, 3, 4, 5]
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 3: Уже отсортированный массив - пройден")


arr = [5, 4, 3, 2, 1]
expected = [1, 2, 3, 4, 5]
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 4: Обратно отсортированный массив - пройден")


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
expected = sorted(arr)
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 5: Массив с дубликатами - пройден")


arr = generate_random_array(1000)
expected = sorted(arr)
assert mergesort(arr) == expected
assert quicksort(arr) == expected
assert quicksort_optimized(arr) == expected
print("Тест 6: Большой случайный массив - пройден")

print("=" * 60)
print("ВСЕ ТЕСТЫ КОРРЕКТНОСТИ ПРОЙДЕНЫ УСПЕШНО!")
print()


print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ НА РАЗНЫХ ТИПАХ ДАННЫХ")
print("=" * 60)


test_cases = {
    "ХУДШИЙ СЛУЧАЙ QuickSort (отсортированный 5000)": generate_worst_case_quicksort(5000),
    "ЛУЧШИЙ СЛУЧАЙ QuickSort (случайный 5000)": generate_best_case_quicksort(5000),
    "ВСЕ ЭЛЕМЕНТЫ ОДИНАКОВЫЕ (10000)": generate_all_duplicates(10000),
    "СИЛЬНО НЕСБАЛАНСИРОВАННЫЙ (3000)": generate_extreme_imbalanced(3000),
    "БОЛЬШОЙ СЛУЧАЙНЫЙ (10000)": generate_random_array(10000),
    "ОБРАТНО ОТСОРТИРОВАННЫЙ (5000)": generate_reversed_array(5000),
    "МНОГО ДУБЛИКАТОВ (10000)": generate_duplicates_array(10000),
}

results = {}

for test_name, test_data in test_cases.items():
    print(f"\n{test_name}:")
    

    result_merge, merge_time = timed_mergesort(test_data.copy())
    

    result_quick, quick_time = timed_quicksort(test_data.copy())
    

    result_quick_opt, quick_opt_time = timed_quicksort_optimized(test_data.copy())
    

    expected = sorted(test_data)
    assert result_merge == expected, f"MergeSort дал неверный результат для {test_name}"
    assert result_quick == expected, f"QuickSort дал неверный результат для {test_name}"
    assert result_quick_opt == expected, f"QuickSort оптимизированный дал неверный результат для {test_name}"
    
    results[test_name] = {
        'mergesort': merge_time,
        'quicksort': quick_time,
        'quicksort_optimized': quick_opt_time
    }
    

    fastest = min(results[test_name], key=results[test_name].get)
    slowest = max(results[test_name], key=results[test_name].get)
    
    fastest_time = results[test_name][fastest]
    slowest_time = results[test_name][slowest]
    difference = slowest_time - fastest_time
    
    print(f"Самый быстрый: {fastest} ({fastest_time:.6f} сек)")
    print(f"Самый медленный: {slowest} ({slowest_time:.6f} сек)")


print("\n" + "=" * 60)
print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
print("=" * 60)


for test_name in test_cases.keys():
    merge_time = results[test_name]['mergesort']
    quick_time = results[test_name]['quicksort']
    quick_opt_time = results[test_name]['quicksort_optimized']
    
    print(f"\n{test_name}:")
    print(f"  MergeSort: {merge_time:.6f} сек")
    print(f"  QuickSort: {quick_time:.6f} сек")
    print(f"  QuickSort оптимизированный: {quick_opt_time:.6f} сек")


    if quick_time > merge_time * 2:
        print("  → QuickSignificantly медленнее MergeSort")
    elif merge_time > quick_time * 2:
        print("  → MergeSort значительно медленнее QuickSort")
    else:
        print("  → Производительность сопоставима")

print("\n" + "=" * 60)
print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!")