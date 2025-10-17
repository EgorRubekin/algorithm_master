class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedListStack:
   
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):

        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):

        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Stack([" + ", ".join(reversed(items)) + "])"


class LinkedListQueue:
    
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        item = self.front.data
        self.front = self.front.next
        

        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Пустая очередь")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Queue([" + ", ".join(items) + "])"