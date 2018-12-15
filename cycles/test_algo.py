import unittest
from algo import check_cycle

class CyclicListSpecification(unittest.TestCase):
    """Specification for the algorithm that will check if a linkedlist
    contains a cycle, or is otherwise self-referential.
    """
    def test_single_node_list_with_null_tail_is_Not_Cyclic(self):
        node = object()
        self.assertEqual(False, check_cycle(node),
                        'A single node, with no tail should not be considered cyclic')

if __name__ == '__main__':
    unittest.main()

# TODO: make an atom template for running the unit tests
# TODO: maybe switch to nuclide?
