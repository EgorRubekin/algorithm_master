def test_validate_stack_sequences():
    
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 1 пройден")
    
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert validate_stack_sequences(pushed, popped) == False
    print("Тест 2 пройден")
    

    pushed = [1, 2, 3, 4]
    popped = [1, 2, 3, 4]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 3 пройден")
    

    pushed = [1, 2, 3, 4]
    popped = [4, 3, 2, 1]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 4 пройден")
    

    pushed = [1, 2, 3]
    popped = [2, 1, 3]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 5 пройден")
    

    pushed = [1, 2, 3, 4]
    popped = [2, 4, 1, 3]
    assert validate_stack_sequences(pushed, popped) == False
    print("Тест 6 пройден")
    

    pushed = [1]
    popped = [1]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 7 пройден")
    

    pushed = []
    popped = []
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 8 пройден")
    

    pushed = [1, 2, 3]
    popped = [1, 2]
    assert validate_stack_sequences(pushed, popped) == False
    print("Тест 9 пройден")
    

    pushed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    popped = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]
    assert validate_stack_sequences(pushed, popped) == True
    print("Тест 10 пройден")


test_validate_stack_sequences()
    
