def run_tests():

    assert rabin_karp("hello", "ell") == [1]
    assert rabin_karp("banana", "ana") == [1, 3]
    

    assert rabin_karp("a", "a") == [0]
    assert rabin_karp("abcdef", "abcdef") == [0]
    assert rabin_karp("abc", "abcd") == []
    
    assert rabin_karp("", "a") == []
    assert rabin_karp("abc", "") == []
    
    assert rabin_karp("abcdef", "xyz") == []
    assert rabin_karp("aaaaa", "b") == []
    
    assert rabin_karp("aaaaaaaaaa", "aaa") == [0, 1, 2, 3, 4, 5, 6, 7]
    
    assert rabin_karp("multi word test", "word") == [6]
    assert rabin_karp("123-456-123", "123") == [0, 8]


    assert rabin_karp("Python", "python") == []
    
    long_text = "ab" * 1000 + "target" + "ab" * 1000
    assert rabin_karp(long_text, "target") == [2000]



run_tests()