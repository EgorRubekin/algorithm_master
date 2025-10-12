def test_group_anagrams():


    print("=" * 60)
    print("ТЕСТИРОВАНИЕ")
    print("=" * 60)


    print("\nТест 1: Базовый случай из условия")
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = group_anagrams(strs1)
    result1_sorted = sorted([sorted(group) for group in result1])
    expected1 = sorted([sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
    print(f"Input: {strs1}")
    print(f"Output: {result1}")
    print(f"Expected: {[['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]}")
    assert result1_sorted == expected1, f"Ожидалось {expected1}, получено {result1_sorted}"



    print("\nТест 2: Пустой список")
    strs2 = []
    result2 = group_anagrams(strs2)
    expected2 = []
    print(f"Input: {strs2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    assert result2 == expected2, f"Ожидалось {expected2}, получено {result2}"



    print("\nТест 3: Одно слово")
    strs3 = ["hello"]
    result3 = group_anagrams(strs3)
    expected3 = [["hello"]]
    print(f"Input: {strs3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    assert sorted([sorted(group) for group in result3]) == sorted([sorted(group) for group in expected3])



    print("\nТест 4: Все слова - анаграммы")
    strs4 = ["abc", "bca", "cab", "acb", "cba", "bac"]
    result4 = group_anagrams(strs4)
    result4_sorted = sorted([sorted(group) for group in result4])
    expected4 = sorted([sorted(group) for group in [["abc", "bca", "cab", "acb", "cba", "bac"]]])
    print(f"Input: {strs4}")
    print(f"Output: {result4}")
    print(f"Expected: {[['abc', 'bca', 'cab', 'acb', 'cba', 'bac']]}")
    assert result4_sorted == expected4, f"Ожидалось {expected4}, получено {result4_sorted}"



    print("\nТест 5: Нет анаграмм")
    strs5 = ["cat", "dog", "bird", "fish"]
    result5 = group_anagrams(strs5)
    result5_sorted = sorted([sorted(group) for group in result5])
    expected5 = sorted([sorted(group) for group in [["cat"], ["dog"], ["bird"], ["fish"]]])
    print(f"Input: {strs5}")
    print(f"Output: {result5}")
    print(f"Expected: {[['cat'], ['dog'], ['bird'], ['fish']]}")
    assert result5_sorted == expected5, f"Ожидалось {expected5}, получено {result5_sorted}"



    print("\nТест 6: Слова разной длины")
    strs6 = ["a", "ab", "ba", "abc", "bca", "abcd"]
    result6 = group_anagrams(strs6)
    result6_sorted = sorted([sorted(group) for group in result6])
    expected6 = sorted([sorted(group) for group in [["a"], ["ab", "ba"], ["abc", "bca"], ["abcd"]]])
    print(f"Input: {strs6}")
    print(f"Output: {result6}")
    print(f"Expected: {[['a'], ['ab', 'ba'], ['abc', 'bca'], ['abcd']]}")
    assert result6_sorted == expected6, f"Ожидалось {expected6}, получено {result6_sorted}"



    print("\nТест 7: Слова с повторяющимися буквами")
    strs7 = ["aabb", "abab", "bbaa", "abba", "abc", "bac"]
    result7 = group_anagrams(strs7)
    result7_sorted = sorted([sorted(group) for group in result7])
    expected7 = sorted([sorted(group) for group in [["aabb", "abab", "bbaa", "abba"], ["abc", "bac"]]])
    print(f"Input: {strs7}")
    print(f"Output: {result7}")
    print(f"Expected: {[['aabb', 'abab', 'bbaa', 'abba'], ['abc', 'bac']]}")
    assert result7_sorted == expected7, f"Ожидалось {expected7}, получено {result7_sorted}"


    print("\nТест 8: Пустые строки")
    strs8 = ["", "", "a", "b", ""]
    result8 = group_anagrams(strs8)
    result8_sorted = sorted([sorted(group) for group in result8])
    expected8 = sorted([sorted(group) for group in [["", "", ""], ["a"], ["b"]]])
    print(f"Input: {strs8}")
    print(f"Output: {result8}")
    print(f"Expected: {[['', '', ''], ['a'], ['b']]}")
    assert result8_sorted == expected8, f"Ожидалось {expected8}, получено {result8_sorted}"



test_group_anagrams()