from utils import timed
from copy import deepcopy

def sort(numbers: list) -> list:
    values_to_merge = deepcopy(numbers)

    timed(mergesort)(values_to_merge)
    for i, v in enumerate(values_to_merge):
        numbers[i] = v

def mergesort(nums) -> list:
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    left, right = mergesort(left), mergesort(right)
    l, r, f = 0, 0, 0

    # write back rather than creating a new array
    for i in range(len(nums)):
        if l == len(left) or r == len(right):
            break
        
        if left[l] < right[r]:
            nums[i] = left[l]
            l += 1
        else:
            nums[i] = right[r]
            r += 1
        f += 1
    
    # cleanup
    while l < len(left):
        nums[f] = left[l]
        f += 1
        l += 1
    
    while r < len(right):
        nums[f] = right[r]
        f += 1
        r += 1

    return nums
