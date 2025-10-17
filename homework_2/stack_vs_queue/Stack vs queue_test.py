def test_stack():
    """Тестирование стека"""
    stack = LinkedListStack()
    

    assert stack.is_empty() == True
    assert len(stack) == 0
    

    stack.push(1)
    stack.push(2)
    stack.push(3)
    

    assert stack.is_empty() == False
    assert len(stack) == 3
    assert stack.peek() == 3
    

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    

    assert stack.is_empty() == True
    assert len(stack) == 0
    

    try:
        stack.pop()
        assert False, "Должна быть ошибка при pop из пустого стека"
    except IndexError:
        pass
    
    print("Все тесты стека пройдены")


def test_queue():
    """Тестирование очереди"""
    queue = LinkedListQueue()
    

    assert queue.is_empty() == True
    assert len(queue) == 0
    

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    

    assert queue.is_empty() == False
    assert len(queue) == 3
    assert queue.peek() == 1 
    

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    

    assert queue.is_empty() == True
    assert len(queue) == 0
    

    try:
        queue.dequeue()
        assert False, "Должна быть ошибка при dequeue из пустой очереди"
    except IndexError:
        pass
    
    print("Все тесты очереди пройдены")



test_stack()
test_queue()
