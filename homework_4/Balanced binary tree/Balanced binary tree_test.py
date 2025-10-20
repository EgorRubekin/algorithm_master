
def run_all_tests():
    solution = Solution()
    

    assert solution.isBalanced(None) == True
    print("Тест 1: Пройден")
    
    root = TreeNode(1)
    assert solution.isBalanced(root) == True
    print("Тест 2: Пройден")
    
    #     1
    #    / \
    #   2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.isBalanced(root) == True
    print("Тест 3: Пройден")
    
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert solution.isBalanced(root) == True
    print("Тест 4: Пройден")
    
    #     1
    #    /
    #   2
    #  /
    # 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert solution.isBalanced(root) == False
    print("Тест 5: Пройден")
    
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert solution.isBalanced(root) == False
    print("Тест 6: Пройден")
    
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #  /
    # 7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    assert solution.isBalanced(root) == True
    print("Тест 7: Пройден")
    
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #  / \
    # 6   7
    #/
    #8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.left.left.left = TreeNode(8)
    assert solution.isBalanced(root) == False
    print("Тест 8: Пройден")
    
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6 7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.isBalanced(root) == True
    print("Тест 9: Пройден")
    
    #     1
    #    / \
    #   2   3
    #  /   / \
    # 4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    assert solution.isBalanced(root) == True
    print("Тест 10: Пройден")
    
    #     1
    #    / \
    #   2   3
    #    \
    #     4
    #      \
    #       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    assert solution.isBalanced(root) == False
    print("Тест 11: Пройден")
    


    

    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    #  /         \
    # 6           7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    assert solution.isBalanced(root) == False
    print("Тест 12: Пройден")
    

    #       1
    #      / \
    #     2   3
    #    / 
    #   4   
    #  /
    # 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    assert solution.isBalanced(root) == False
    print("Тест 13: Пройден")
    
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    assert solution.isBalanced(root) == False
    print("Тест 14: Пройден")
    

    
run_all_tests()