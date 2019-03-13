from utils import timed

@timed
def sort(array: list) -> list:
    upper_limit = len(array) - 1
    quicksort(array, 0, upper_limit)
    return array

def quicksort(array, lo:int, hi: int):
    if lo < hi:
        p = partition(array, lo, hi)
        quicksort(array, lo, p - 1)
        quicksort(array, p + 1, hi)

def partition(array, lo:int, hi: int) -> int:
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[hi], array[i] = array[i], array[hi]
    return i