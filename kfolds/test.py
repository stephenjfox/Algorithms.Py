import unittest
from random import randint
from impl import *

def rando_data(count=20):
    return [randint(1, 30) for _ in range(count)]


class TestK_Fold(unittest.TestCase):
    """docstring for TestK_Fold."""

    def test_chunk(self):
        data = rando_data()

        folded = k_folds(data, 10)
        self.assertEqual(len(folded), 10)

        folded = k_folds(data, 5)
        self.assertEqual(len(folded), 5)

    def test_uneven_chunk(self):
        data = rando_data(5)

        expected = [data[-1]]
        actual = k_folds(data, 2)[2] # should be the last data, in a box

        self.assertEqual(len(expected), len(actual))
        self.assertEqual(1, len(actual))
        self.assertEqual(expected[0], actual[0])

    def test_data_existence(self):
        data = rando_data(50)
        folded = k_folds(data)
        train, validation = k_sample(folded, 1)

        self.assertEqual(folded[1], validation,
                        'The validation set should be folded[i]')
        self.assertEqual(len(folded) - 1, len(train),
                        'Folded and prep data should have a length delta of 1')

    def test_sample_with_multiple_indicies(self):
        folded = k_folds(rando_data(25), 5)
        train, validation = k_sample(folded, [1, 2])

        self.assertEqual(2, len(validation),
                        'The validation set should preserve the designated indices')

        self.assertEqual([folded[1], folded[2]], validation,
                        'Sampling should have returned the data at the target indices')

if __name__ == '__main__':
    unittest.main()
