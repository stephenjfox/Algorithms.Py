from unittest import main, TestCase

from binary_search import search
from sorting.utils import generate_numbers

class TestSearch(TestCase):

    def generate_test_datasets(self, count=10):
        for _ in range(count):
            yield sorted(generate_numbers(100)) # yield a list of numbers

    def test_simpleSearch(self):
        values = list(range(10))
        target = values.index(2)
        self.assertEqual(target, search(values, 2), "Should find a value that is in the array")

    def test_searchNotFound(self):
        values = list(range(10))
        target = -1
        self.assertEqual(target, search(values, 20), "Should return -1 in the case of value not in the array")

if __name__ == "__main__":
    main()