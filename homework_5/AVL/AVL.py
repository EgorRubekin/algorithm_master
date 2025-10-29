from typing import Optional, List

class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def _get_height(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)
    
    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node 
        
        self._update_height(node)
        balance = self._get_balance(node)
        

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        

        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        

        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        

        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)
    
    def _delete(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if not node:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        
        if not node:
            return node
        
        self._update_height(node)
        balance = self._get_balance(node)
        

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left:
            current = current.left
        return current
    
    def search(self, key: int) -> bool:
        return self._search(self.root, key)
    
    def _search(self, node: Optional[AVLNode], key: int) -> bool:
        if not node:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def inorder(self) -> List[int]:
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List[int]):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
    
    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)
    
    def _is_balanced(self, node: Optional[AVLNode]) -> bool:
        if not node:
            return True
        
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return False
        
        return self._is_balanced(node.left) and self._is_balanced(node.right)