import random

def next_int() -> int:
    return random.randint(-100, 100)

def generate_numbers(count: int):
    return [next_int() for _ in range(count)]