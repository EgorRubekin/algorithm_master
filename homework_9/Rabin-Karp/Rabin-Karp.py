def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    if m == 0: return []

    P = 31  
    M = 10**9 + 9 
    

    p_pow = pow(P, m - 1, M)
    
    result = []
    pattern_hash = 0
    current_window_hash = 0


    for i in range(m):
        pattern_hash = (pattern_hash * P + ord(pattern[i])) % M
        current_window_hash = (current_window_hash * P + ord(text[i])) % M

    for i in range(n - m + 1):
        if pattern_hash == current_window_hash:
            if text[i:i+m] == pattern:
                result.append(i)
        

        if i < n - m:
            current_window_hash = (current_window_hash - ord(text[i]) * p_pow) % M
            current_window_hash = (current_window_hash * P + ord(text[i+m])) % M
            current_window_hash = (current_window_hash + M) % M
            
    return result