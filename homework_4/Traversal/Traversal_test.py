def test_bst_traversals():
    

    bst = BST()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)
    
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    
    assert bst.pre_order() == [4, 2, 1, 3, 6, 5, 7]
    assert bst.post_order() == [1, 3, 2, 5, 7, 6, 4]
    assert bst.in_order() == [1, 2, 3, 4, 5, 6, 7]
    assert bst.reverse_pre_order() == [4, 6, 7, 5, 2, 3, 1]
    assert bst.reverse_post_order() == [7, 5, 6, 3, 1, 2, 4]
    assert bst.reverse_in_order() == [7, 6, 5, 4, 3, 2, 1]
    print("Тест 1 пройден")
    

    bst = BST()
    bst.insert(10)
    
    assert bst.pre_order() == [10]
    assert bst.post_order() == [10]
    assert bst.in_order() == [10]
    assert bst.reverse_pre_order() == [10]
    assert bst.reverse_post_order() == [10]
    assert bst.reverse_in_order() == [10]
    print("Тест 2 пройден")
    


    bst = BST()
    values = [1, 2, 3, 4, 5]
    for value in values:
        bst.insert(value)
    
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    
    assert bst.pre_order() == [1, 2, 3, 4, 5]
    assert bst.post_order() == [5, 4, 3, 2, 1]
    assert bst.in_order() == [1, 2, 3, 4, 5]
    assert bst.reverse_pre_order() == [1, 2, 3, 4, 5]
    assert bst.reverse_post_order() == [5, 4, 3, 2, 1]
    assert bst.reverse_in_order() == [5, 4, 3, 2, 1]
    print("Тест 3 пройден")
    


    bst = BST()
    values = [0, -2, 2, -3, -1, 1, 3]
    for value in values:
        bst.insert(value)
    
    #       0
    #      / \
    #    -2   2
    #    / \ / \
    #  -3 -1 1  3
    
    assert bst.pre_order() == [0, -2, -3, -1, 2, 1, 3]
    assert bst.post_order() == [-3, -1, -2, 1, 3, 2, 0]
    assert bst.in_order() == [-3, -2, -1, 0, 1, 2, 3]
    assert bst.reverse_pre_order() == [0, 2, 3, 1, -2, -1, -3]
    assert bst.reverse_post_order() == [3, 1, 2, -1, -3, -2, 0]
    assert bst.reverse_in_order() == [3, 2, 1, 0, -1, -2, -3]
    print("Тест 4 пройден")
    


    bst = BST()
    values = [5, 3, 8, 2, 4, 7, 9, 1, 6]
    for value in values:
        bst.insert(value)
    
    #         5
    #       /   \
    #      3     8
    #     / \   / \
    #    2   4 7   9
    #   /     /
    #  1     6
    
    assert bst.pre_order() == [5, 3, 2, 1, 4, 8, 7, 6, 9]
    assert bst.post_order() == [1, 2, 4, 3, 6, 7, 9, 8, 5]
    assert bst.in_order() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bst.reverse_pre_order() == [5, 8, 9, 7, 6, 3, 4, 2, 1]
    assert bst.reverse_post_order() == [9, 6, 7, 8, 4, 1, 2, 3, 5]
    assert bst.reverse_in_order() == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Тест 5 пройден")
    

test_bst_traversals()
