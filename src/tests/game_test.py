import unittest
from entities.sudoku_grid import SudokuGrid
from services.functions import Functions

e = ""
grid1 = [
    [e, e, e, e, e, 2, 1, e, e],
            [e, e, e, e, 8, e, 6, 7, e],
            [e, e, 9, e, 1, e, 4, 8, e],
            [e, 2, e, e, e, e, e, e, e],
            [6, 9, 8, e, 7, e, e, e, 4],
            [e, 4, 7, 1, 5, 6, 9, e, e],
            [e, 7, e, e, 6, 1, 2, e, e],
            [e, e, e, e, e, e, 8, 4, 6],
            [2, e, 5, e, 4, e, e, 9, 1]
]

grid1_values = [
            [False, False, False, False, False, 2, 1, False, False],
            [False, False, False, False, 8, False, 6, 7, False],
            [False, False, 9, False, 1, False, 4, 8, False],
            [False, 2, False, False, False, False, False, False, False],
            [6, 9, 8, False, 7, False, False, False, 4],
            [False, 4, 7, 1, 5, 6, 9, False, False],
            [False, 7, False, False, 6, 1, 2, False, False],
            [False, False, False, False, False, False, 8, 4, 6],
            [2, False, 5, False, 4, False, False, 9, 1]
]


class TestGame(unittest.TestCase):
    def setUp(self):
        self.functions = Functions()
        self.entities = SudokuGrid()
        self.error = self.functions.error
        self.grid1 = self.entities.number_grid1
        self.grid1_values = self.entities.number_grid1_values

    def test_0_returns_none(self):
        self.assertEqual(self.functions.check(0, 2, 0, grid1), None)

    def test_seemingly_correct_number_returns_no_error(self):
        grid1[0][0] = 4
        self.assertEqual(self.functions.check(4, 0, 0, grid1), None)

    def test_definitely_incorrect_number_returns_error_square_1(self):
        grid1[0][0] = 9
        self.assertEqual(self.functions.check(9, 0, 0, grid1), (0, 0))

    def test_definitely_incorrect_number_returns_error_square_2(self):
        grid1[3][0] = 9
        self.assertEqual(self.functions.check(8, 3, 0, grid1), (3, 0))



