def test_all_permutations():
    solution = Solution()
    

    result = solution.permute([1, 2, 3])
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert len(result) == len(expected)
    for perm in expected:
        assert perm in result
    print("Тест 1 пройден\n")
    

    result = solution.permute([0, 1])
    expected = [[0,1],[1,0]]
    assert len(result) == len(expected)
    for perm in expected:
        assert perm in result
    print("Тест 2 пройден\n")
    

    result = solution.permute([1])
    expected = [[1]]
    assert result == expected
    print("Тест 3 пройден\n")
    

    result = solution.permute([])
    expected = [[]]
    assert result == expected
    print("Тест 4 пройден\n")
    

    result = solution.permute([1, 2])
    expected = [[1,2],[2,1]]
    assert len(result) == len(expected)
    for perm in expected:
        assert perm in result
    print("Тест 5 пройден\n")
    

    result = solution.permute([5])
    assert result == [[5]]
    print("Тест 6 пройден")
    

    result = solution.permute([1, 2, 3])
    assert len(result) == 6
    print("Тест 7 пройден")


test_all_permutations()
