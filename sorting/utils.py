import random
import time

def next_int() -> int:
    return random.randint(-100, 100)

def generate_numbers(count: int):
    return [next_int() for _ in range(count)]


def timed(func):
    """Timing decorator for func invocations"""
    def timer(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs) # invoke the thing itself

        print("Execution took:", t - time.perf_counter())
        return result
    
    return timer