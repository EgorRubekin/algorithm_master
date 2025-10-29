import functools
from typing import Any, Callable

def tracer(func: Callable) -> Callable:
    depth = 0
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal depth
        
        indent = "  " * depth
        print(f"{indent}-> {func.__name__}({', '.join(map(str, args))})")
        
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        
        print(f"{indent}<- {func.__name__}() = {result}")
        return result
    
    return wrapper