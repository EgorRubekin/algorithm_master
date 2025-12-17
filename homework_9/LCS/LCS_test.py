def run_tests():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    result = longest_common_subsequence(s1, s2)
    assert result == "GTAB", f"Expected 'GTAB', but got '{result}'"

    assert longest_common_subsequence("abcde", "abcde") == "abcde"

    assert longest_common_subsequence("abc", "xyz") == ""

    assert longest_common_subsequence("", "abc") == ""
    
    assert longest_common_subsequence("abc", "a_b_c_") == "abc"


    res_ambiguous = longest_common_subsequence("ABC", "ACB")
    assert res_ambiguous in ["AB", "AC"], f"Got '{res_ambiguous}'"


run_tests()