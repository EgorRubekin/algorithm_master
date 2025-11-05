import time
from typing import List, Callable, Any
import random
from collections import deque


def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper


def mergesort_iterative(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()
    
    queue = deque([ [x] for x in arr ])
    
    while len(queue) > 1:
        left = queue.popleft()
        right = queue.popleft()
        merged = merge_iterative(left, right)
        queue.append(merged)
    
    return queue[0]

def merge_iterative(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort_iterative(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()
    
    arr_copy = arr.copy()
    stack = [(0, len(arr_copy) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pi = partition_iterative(arr_copy, low, high)
            
            if (pi - low) > (high - pi):
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
            else:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))
    
    return arr_copy

def partition_iterative(arr: List[int], low: int, high: int) -> int:
    mid = (low + high) // 2
    
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    pivot = arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


@timer
def timed_mergesort_iterative(arr: List[int]) -> List[int]:
    return mergesort_iterative(arr)

@timer
def timed_quicksort_iterative(arr: List[int]) -> List[int]:
    return quicksort_iterative(arr)


def generate_sorted_array(size: int) -> List[int]:
    return list(range(size))

def generate_reversed_array(size: int) -> List[int]:
    return list(range(size, 0, -1))

def generate_random_array(size: int) -> List[int]:
    return [random.randint(0, 10000) for _ in range(size)]

def generate_duplicates_array(size: int) -> List[int]:
    return [random.randint(0, 10) for _ in range(size)]

def generate_almost_sorted_array(size: int) -> List[int]:
    arr = list(range(size))
    for i in range(size // 100):
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def generate_all_duplicates(size: int) -> List[int]:
    return [5] * size

def generate_worst_case_quicksort(size: int) -> List[int]:
    return list(range(size))
