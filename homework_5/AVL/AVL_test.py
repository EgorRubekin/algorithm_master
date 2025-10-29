def test_avl():
    avl = AVL()
    

    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    assert avl.search(10) == True
    assert avl.search(20) == True
    assert avl.search(30) == True
    assert avl.search(40) == False
    assert avl.is_balanced() == True
    print("Тест 1 пройден")
    

    avl.delete(20)
    assert avl.search(20) == False
    assert avl.search(10) == True
    assert avl.search(30) == True
    assert avl.is_balanced() == True
    print("Тест 2 пройден")
    

    avl2 = AVL()
    numbers = [50, 30, 70, 20, 40, 60, 80]
    for num in numbers:
        avl2.insert(num)
    
    for num in numbers:
        assert avl2.search(num) == True
    
    inorder_result = avl2.inorder()
    assert inorder_result == sorted(numbers)
    

    avl2.delete(50)
    avl2.delete(20)
    assert avl2.search(50) == False
    assert avl2.search(20) == False
    assert avl2.is_balanced() == True
    print("Тест 3 пройден")
    

    avl3 = AVL()
    avl3.insert(5)
    assert avl3.search(5) == True
    assert avl3.inorder() == [5]
    
    avl3.delete(5)
    assert avl3.search(5) == False
    assert avl3.inorder() == []
    assert avl3.search(1) == False
    print("Тест 4 пройден")
    

    avl4 = AVL()
    for i in range(10, 0, -1):
        avl4.insert(i)
    
    assert avl4.is_balanced() == True
    assert len(avl4.inorder()) == 10
    print("Тест 5 пройден")
    

    avl5 = AVL()
    avl5.insert(5)
    avl5.insert(5)
    assert avl5.inorder() == [5] 
    print("Тест 6 пройден")

test_avl()
