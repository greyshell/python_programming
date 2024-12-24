import unittest

from k_largest_elements_immutable_max_heap import (
    get_k_largest_elements_immutable_max_heap
)


from libozone import Heap, HeapType


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_get_k_largest_elements_immutable_max_heap(self):
        # expected, actual
        test_params = [
            ([17, 16, 15, 14], {"immutable_max_heap": Heap([7, 17, 16, 2, 3, 15, 14], heap_type=HeapType.MAX), "k": 4}),

        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertCountEqual(expected, get_k_largest_elements_immutable_max_heap(**kwargs))


if __name__ == '__main__':
    unittest.main()
