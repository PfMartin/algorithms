import unittest
from sorter import Sorter


class TestSorter(unittest.TestCase):
    def test_selection_sort(self):
        sorter = Sorter()

        # Test case 1: Normal case
        self.assertEqual(
            sorter.selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64]
        )

        # Test case 2: Already sorted array
        self.assertEqual(sorter.selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

        # Test case 3: Reverse sorted array
        self.assertEqual(sorter.selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        # Test case 4: Array with duplicates
        self.assertEqual(sorter.selection_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])

        # Test case 5: Empty array
        self.assertEqual(sorter.selection_sort([]), [])

        # Test case 6: Array with one element
        self.assertEqual(sorter.selection_sort([1]), [1])

    def test_insertion_sort(self):
        sorter = Sorter()

        # Test case 1: Normal case
        self.assertEqual(
            sorter.insertion_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64]
        )

        # Test case 2: Already sorted array
        self.assertEqual(sorter.insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

        # Test case 3: Reverse sorted array
        self.assertEqual(sorter.insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

        # Test case 4: Array with duplicates
        self.assertEqual(sorter.insertion_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])

        # Test case 5: Empty array
        self.assertEqual(sorter.insertion_sort([]), [])

        # Test case 6: Array with one element
        self.assertEqual(sorter.insertion_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
