def validate_stack_sequences(pushed, popped):
    if len(pushed) != len(popped):
        return False
    
    stack = []
    push_index = 0
    pop_index = 0
    

    while pop_index < len(popped):
        if stack and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1
        elif push_index < len(pushed):
            stack.append(pushed[push_index])
            push_index += 1
        else:
            return False
    
    return True