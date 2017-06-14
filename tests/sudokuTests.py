import unittest

from printGrid import printable_grid
from solver import is_row_valid, is_grid_valid


class TestSudoku(unittest.TestCase):
    def test_print_grid(self):
        grid = [
            [None, None, 7, None, None, None, None, 6, None],
            [2, 3, None, None, 5, 6, None, 9, None],
            [9, None, 1, 8, None, None, 3, None, 5],
            [1, 4, None, None, None, None, None, None, None],
            [8, 9, None, 1, 2, 4, None, 5, 6],
            [None, None, None, None, None, None, None, 8, 1],
            [3, None, 8, None, None, 5, 6, None, 9],
            [None, 5, None, 9, 1, None, None, 2, 7],
            [None, 1, None, None, None, None, 5, None, None]
        ]
        expected_output = '. . 7 . . . . 6 .\n' \
                          '2 3 . . 5 6 . 9 .\n' \
                          '9 . 1 8 . . 3 . 5\n' \
                          '1 4 . . . . . . .\n' \
                          '8 9 . 1 2 4 . 5 6\n' \
                          '. . . . . . . 8 1\n' \
                          '3 . 8 . . 5 6 . 9\n' \
                          '. 5 . 9 1 . . 2 7\n' \
                          '. 1 . . . . 5 . .\n'
        output = printable_grid(grid)
        self.assertEqual(expected_output, output)

    def test_is_row_valid_false(self):
        row = [None, None, 7, None, None, None, None, 6, 6]
        output = is_row_valid(row)
        self.assertFalse(output)

    def test_is_row_valid_true(self):
        row = [None, None, 7, None, None, None, None, 6, 9]
        output = is_row_valid(row)
        self.assertTrue(output)

    def test_is_grid_valid_true(self):
        grid = [
            [None, None, 7, None, None, None, None, 6, None],
            [2, 3, None, None, 5, 6, None, 9, None],
            [9, None, 1, 8, None, None, 3, None, 5],
            [1, 4, None, None, None, None, None, None, None],
            [8, 9, None, 1, 2, 4, None, 5, 6],
            [None, None, None, None, None, None, None, 8, 1],
            [3, None, 8, None, None, 5, 6, None, 9],
            [None, 5, None, 9, 1, None, None, 2, 7],
            [None, 1, None, None, None, None, 5, None, None]
        ]
        output = is_grid_valid(grid)
        self.assertTrue(output)

    def test_is_grid_valid_false1(self):
        grid = [
            [None, None, 7, None, None, None, None, 6, 6],
            [2, 3, None, None, 5, 6, None, 9, None],
            [9, None, 1, 8, None, None, 3, None, 5],
            [1, 4, None, None, None, None, None, None, None],
            [8, 9, None, 1, 2, 4, None, 5, 6],
            [None, None, None, None, None, None, None, 8, 1],
            [3, None, 8, None, None, 5, 6, None, 9],
            [None, 5, None, 9, 1, None, None, 2, 7],
            [None, 1, None, None, None, None, 5, None, None]
        ]
        output = is_grid_valid(grid)
        self.assertFalse(output)

    def test_is_grid_valid_false2(self):
        grid = [
            [None, None, 7, None, None, None, None, 6, 9],
            [2, 3, None, None, 5, 6, None, 9, None],
            [9, None, 1, 8, None, None, 3, None, 5],
            [1, 4, None, None, None, None, None, None, None],
            [8, 9, None, 1, 2, 4, None, 5, 6],
            [None, None, None, None, None, None, None, 8, 1],
            [3, None, 8, None, None, 5, 6, None, 9],
            [None, 5, None, 9, 1, None, None, 2, 7],
            [None, 1, None, None, None, None, 5, None, None]
        ]
        output = is_grid_valid(grid)
        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
