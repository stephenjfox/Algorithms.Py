from unittest import TestCase, main

from utils import generate_numbers
from quicksort import sort

class TestQuicksort(TestCase):

    def test_sort(self):
        a = generate_numbers(100)
        
        self.assertListEqual(sorted(a), sort(a))

if __name__ == "__main__":
    main()