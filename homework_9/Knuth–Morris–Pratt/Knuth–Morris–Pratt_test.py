def run_tests():

    assert kmp_search("mississippi", "issip") == [4]

    assert kmp_search("mississippi", "issi") == [1, 4]

    assert kmp_search("hello world", "world") == [6]
    assert kmp_search("abracadabra", "abra") == [0, 7]
    
    assert kmp_search("ababa", "aba") == [0, 2]
    
    assert kmp_search("short", "very long pattern") == []
    
    assert kmp_search("abcde", "fgh") == []
    
    assert kmp_search("abc", "") == []
    
    assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]


run_tests()