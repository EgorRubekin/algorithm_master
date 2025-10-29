import functools
from typing import List, Any, Callable

def tracer(func: Callable) -> Callable:

    depth = 0
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal depth
        
        indent = "  " * depth
        print(f"{indent}-> {func.__name__}({args[0]})")
        
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        
        print(f"{indent}<- {func.__name__}() = {result}")
        return result
    
    return wrapper

class Solution:
    @tracer
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._backtrack(nums, [], result)
        return result
    
    def _backtrack(self, nums: List[int], path: List[int], result: List[List[int]]):
        if not nums:
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            path.append(nums[i])
            remaining = nums[:i] + nums[i+1:]
            self._backtrack(remaining, path, result)
            path.pop()