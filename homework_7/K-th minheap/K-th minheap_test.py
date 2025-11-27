def run_tests():

    solutions = [find_kth_largest_custom, find_kth_largest_heapq]
    
    for solve in solutions:
        func_name = solve.__name__
        print(f"Тестим {func_name}...")


        nums1 = [3, 2, 1, 5, 6, 4]
        k1 = 2

        assert solve(nums1, k1) == 5, f"Ошибка в {func_name} Test 1"


        nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k2 = 4

        assert solve(nums2, k2) == 4, f"Ошибка в {func_name} Test 2"


        nums3 = [10, 20, 15]
        k3 = 1
        assert solve(nums3, k3) == 20, f"Ошибка в {func_name} Test 3"


        nums4 = [7, 1, 9]
        k4 = 3
        assert solve(nums4, k4) == 1, f"Ошибка в {func_name} Test 4"
        

        nums5 = [-1, -5, -2, -4, -3]
        k5 = 2

        assert solve(nums5, k5) == -2, f"Ошибка в {func_name} Test 5"

        print(f"Все тесты пройдены для {func_name}\n")


run_tests()