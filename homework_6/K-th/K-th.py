import random
from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    def quickselect(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]
        
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        if k_smallest == store_index:
            return nums[store_index]
        elif k_smallest < store_index:
            return quickselect(left, store_index - 1, k_smallest)
        else:
            return quickselect(store_index + 1, right, k_smallest)
    
    n = len(nums)
    return quickselect(0, n - 1, n - k)

def find_kth_largest_iterative(nums: List[int], k: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    k_smallest = n - k
    
    while left <= right:
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        if k_smallest == store_index:
            return nums[store_index]
        elif k_smallest < store_index:
            right = store_index - 1
        else:
            left = store_index + 1
    
    return nums[left]
