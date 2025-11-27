class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def __len__(self):
        return len(self.heap)

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if parent >= 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)

    def _sift_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest)

def find_kth_largest_custom(nums, k):
    min_heap = MinHeap()
    
    for num in nums:
        min_heap.push(num)
        if len(min_heap) > k:
            min_heap.pop()
            
    return min_heap.peek()


import heapq

def find_kth_largest_heapq(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return min_heap[0] 