def test_functions():

    print("Тест 1")
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
    
    heap1_slow = makeheap_n_log_n(arr1)
    heap1_fast = makeheap(arr1)
    
    print(f"Исходный: {arr1}")
    print(f"O(N log N): {heap1_slow}, valid: {is_min_heap(heap1_slow)}")
    print(f"O(N): {heap1_fast}, valid: {is_min_heap(heap1_fast)}")
    print()
    
   
    print("Тест 2 (Отсортированный массив)")
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
    
    heap2_slow = makeheap_n_log_n(arr2)
    heap2_fast = makeheap(arr2)
    
    print(f"O(N log N): {heap2_slow}, valid: {is_min_heap(heap2_slow)}")
    print(f"O(N): {heap2_fast}, valid: {is_min_heap(heap2_fast)}")
    print()
    

    print("Тест 3 (обратно отсортир)")
    arr3 = [8, 7, 6, 5, 4, 3, 2, 1]
    
    heap3_slow = makeheap_n_log_n(arr3)
    heap3_fast = makeheap(arr3)
    
    print(f"O(N log N): {heap3_slow}, valid: {is_min_heap(heap3_slow)}")
    print(f"O(N): {heap3_fast}, valid: {is_min_heap(heap3_fast)}")
    print()

def compare_performance():

    print("Сравнение производительности:")
    print("Размер | O(N log N) время | O(N) время | Ускорение")
    print("-" * 55)
    
    sizes = [100, 1000, 5000, 10000, 20000]
    
    for size in sizes:

        arr = [random.randint(1, 100000) for _ in range(size)]
        

        start = time.time()
        makeheap_n_log_n(arr)
        time_slow = time.time() - start
        

        start = time.time()
        makeheap(arr)
        time_fast = time.time() - start
        
        speedup = time_slow / time_fast if time_fast > 0 else float('inf')
        
        print(f"{size:6} | {time_slow:15.6f} | {time_fast:10.6f} | {speedup:8.2f}x")

def verify_correctness():

    print("\nПроверка корректности:")
    
    test_cases = [
        [1],
        [2, 1],
        [5, 3, 8, 1, 2],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [random.randint(1, 100) for _ in range(50)]
    ]
    
    all_correct = True
    for i, test_arr in enumerate(test_cases):
        heap_slow = makeheap_n_log_n(test_arr)
        heap_fast = makeheap(test_arr)
        
        valid_slow = is_min_heap(heap_slow)
        valid_fast = is_min_heap(heap_fast)
        
        print(f"Тест {i+1}: O(N log N) - {valid_slow}, O(N) - {valid_fast}")
        
        if not (valid_slow and valid_fast):
            all_correct = False
    
    print(f"\nВсе тесты пройдены: {all_correct}")


test_functions()
compare_performance()
verify_correctness()