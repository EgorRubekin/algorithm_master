def run_all_tests():
    solution = Solution()
    

    assert solution.isValidBST(None) == True
    print("Тест 1: Пройден")
    

    root = TreeNode(5)
    assert solution.isValidBST(root) == True
    print("Тест 2: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    assert solution.isValidBST(root) == True
    print("Тест 3: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    assert solution.isValidBST(root) == False
    print("Тест 4: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    assert solution.isValidBST(root) == False
    print("Тест 5: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    assert solution.isValidBST(root) == False
    print("Тест 6: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    assert solution.isValidBST(root) == False
    print("Тест 7: Пройден")
    

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    assert solution.isValidBST(root) == True
    print("Тест 8: Пройден")
    

    root = TreeNode(0)
    root.left = TreeNode(-2**31)
    root.right = TreeNode(2**31-1)
    assert solution.isValidBST(root) == True
    print("Тест 9: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    assert solution.isValidBST(root) == False
    print("Тест 10: Пройден")
    

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(11)
    root.left.right.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    assert solution.isValidBST(root) == False
    print("Тест 11: Пройден")
    

    root = TreeNode(0)
    root.left = TreeNode(-5)
    root.right = TreeNode(5)
    root.left.left = TreeNode(-10)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(8)
    assert solution.isValidBST(root) == True
    print("Тест 12: Пройден")
    

    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    assert solution.isValidBST(root) == False
    print("Тест 13: Пройден")
    

run_all_tests()