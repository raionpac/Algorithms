import os
import unittest
from binary_search import binary_search

# Clear the terminal before running tests
os.system('cls' if os.name == 'nt' else 'clear')


class TestBinarySearch(unittest.TestCase):

    def test_element_present(self):
        # Test to verify that binary_search correctly finds an element in the list
        # In this case, it checks if the search for '3' in the list [1, 2, 3, 4, 5] returns the correct index (2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_element_not_present(self):
        # Test to verify that binary_search returns -1 for an element not in the list
        # Here, it's checking that searching for '6' in [1, 2, 3, 4, 5] correctly returns -1
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        # Test to verify that binary_search returns -1 when the list is empty
        # This is important for ensuring the function handles edge cases properly
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_list_target_present(self):
        # Test to check the function's behavior with a single-element list where the element is the target
        # This tests the function's capability to handle the smallest non-empty list
        self.assertEqual(binary_search([1], 1), 0)

    def test_single_element_list_target_not_present(self):
        # Test to check the function's behavior with a single-element list where the element is not the target
        # It's another edge case important for completeness
        self.assertEqual(binary_search([1], 2), -1)

    def test_target_at_start_of_list(self):
        # Test to verify if the function correctly identifies an element at the start of the list
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end_of_list(self):
        # Test to verify if the function correctly identifies an element at the end of the list
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)


# This block checks if the script is run as the main module and runs the tests
if __name__ == '__main__':
    unittest.main()
