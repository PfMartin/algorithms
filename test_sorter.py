import unittest
from sorter import Sorter

test_cases = {
    "unsorted_array": {
        "unsorted": [64, 25, 12, 22, 11],
        "sorted": [11, 12, 22, 25, 64],
    },
    "already_sorted_array": {"unsorted": [1, 2, 3, 4, 5], "sorted": [1, 2, 3, 4, 5]},
    "reverse_sorted_array": {"unsorted": [5, 4, 3, 2, 1], "sorted": [1, 2, 3, 4, 5]},
    "duplicates_array": {"unsorted": [3, 3, 2, 1, 2], "sorted": [1, 2, 2, 3, 3]},
    "empty_array": {"unsorted": [], "sorted": []},
    "single_element_array": {"unsorted": [1], "sorted": [1]},
}


class TestSorter(unittest.TestCase):
    def test_selection_sort(self):
        sorter = Sorter()

        for key in test_cases:
            self.assertEqual(
                sorter.selection_sort(test_cases[key]["unsorted"]),
                test_cases[key]["sorted"],
            )

    def test_insertion_sort(self):
        sorter = Sorter()

        for key in test_cases:
            self.assertEqual(
                sorter.insertion_sort(test_cases[key]["unsorted"]),
                test_cases[key]["sorted"],
            )


if __name__ == "__main__":
    unittest.main()
