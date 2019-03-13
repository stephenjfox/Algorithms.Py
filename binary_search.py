# TODO: implement generic comparible binary_searching
from typing import List #, TypeVar

# T = TypeVar('T')

def search(l: List[int], find: int) -> int:
    """Perform a binary search for item `find` in list `l`.
    Returns:
        -1 if not found, otherwise the index `i` where the value was found
    """
    assert len(l) # fail on bad input

    lo, hi = 0, len(l) - 1
    mid = (lo + hi) // 2
    # stop iterating when they are equivalent
    while lo < hi:
        val_mid = l[mid]
        if val_mid < find:
            lo = mid + 1
        elif val_mid > find:
            hi = mid
        else:
            return mid
        mid = (lo + hi) // 2
    else:
        return 0 if l[0] is find else -1
    
    return mid