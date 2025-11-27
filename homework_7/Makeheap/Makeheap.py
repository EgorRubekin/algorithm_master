import time
import random
import math

def makeheap_n_log_n(arr):
    """
    Преобразует массив в min-heap за O(N log N)
    Использует метод последовательной вставки
    """
    heap = []
    
    def heapify_up(idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx] < heap[parent]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
            else:
                break
    

    for element in arr:
        heap.append(element)
        heapify_up(len(heap) - 1)
    
    return heap

def makeheap(arr):
    """
    Преобразует массив в min-heap за O(N)
    Использует алгоритм Флойда (heapify_down)
    """
    heap = arr.copy()
    n = len(heap)
    
    def heapify_down(idx, size):

        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right
            
        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            heapify_down(smallest, size)
    

    for i in range(n // 2 - 1, -1, -1):
        heapify_down(i, n)
    
    return heap

def is_min_heap(heap):
    """Проверяет, является ли массив min-heap"""
    n = len(heap)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and heap[i] > heap[left]:
            return False
        if right < n and heap[i] > heap[right]:
            return False
    return True