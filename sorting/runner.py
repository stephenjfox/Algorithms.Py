from utils import generate_numbers
from quicksort import sort


if __name__ == "__main__":
    numbers = generate_numbers(30)
    print("""PROGRAM START
    """)
    print("Before:", numbers)
    sort(numbers)
    print("After:", numbers)
    print("""
PROGRAM END""")