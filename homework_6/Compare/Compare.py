import time
from typing import List, Callable, Any
import random
import sys

sys.setrecursionlimit(100000)


# Декоратор для замера времени
def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.6f} секунд")
        return result, execution_time
    return wrapper

# Рекурсивная версия MergeSort
def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
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

# Рекурсивная версия QuickSort
def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def quicksort_optimized(arr: List[int]) -> List[int]:
    def _quicksort(arr: List[int], low: int, high: int) -> None:
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)
    
    def partition(arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    arr_copy = arr.copy()
    _quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


@timer
def timed_mergesort(arr: List[int]) -> List[int]:
    return mergesort(arr)

@timer
def timed_quicksort(arr: List[int]) -> List[int]:
    return quicksort(arr)

@timer
def timed_quicksort_optimized(arr: List[int]) -> List[int]:
    return quicksort_optimized(arr)


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

def generate_worst_case_quicksort(size: int) -> List[int]:
    """Генерирует худший случай для QuickSort (отсортированный массив)"""
    return list(range(size))

def generate_best_case_quicksort(size: int) -> List[int]:
    """Генерирует лучший случай для QuickSort (сбалансированные разделения)"""
    arr = list(range(size))
    random.shuffle(arr)
    return arr

def generate_all_duplicates(size: int) -> List[int]:
    """Генерирует массив где все элементы одинаковые"""
    return [5] * size

def generate_extreme_imbalanced(size: int) -> List[int]:
    """Генерирует массив, вызывающий максимальную несбалансированность в QuickSort"""
    return [size] + list(range(size-1))