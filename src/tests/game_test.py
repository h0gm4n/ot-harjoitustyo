import unittest
from entities.sudoku_grid import SudokuGrid
from services.functions import Functions
from repository.repository import Repository

e = ""
number_grid_easy_1 = [
            [e, 4, 3, e, e, 5, e, 2, e],
            [e, 7, e, 9, 6, 2, 3, 4, e],
            [e, e, 2, 4, e, 7, e, 9, 1],
            [e, 3, e, e, 5, e, 4, e, e],
            [e, e, 7, e, 9, e, e, e, e],
            [8, e, 5, 7, e, e, 1, 6, e],
            [e, e, 4, e, e, 6, 9, 1, e],
            [5, 1, 9, 3, 2, e, e, e, 7],
            [e, e, 6, e, 7, e, e, e, 4]
        ]

number_grid_easy_1_values = [
            [False, 4, 3, False, False, 5, False, 2, False],
            [False, 7, False, 9, 6, 2, 3, 4, False],
            [False, False, 2, 4, False, 7, False, 9, 1],
            [False, 3, False, False, 5, False, 4, False, False],
            [False, False, 7, False, 9, False, False, False, False],
            [8, False, 5, 7, False, False, 1, 6, False],
            [False, False, 4, False, False, 6, 9, 1, False],
            [5, 1, 9, 3, 2, False, False, False, 7],
            [False, False, 6, False, 7, False, False, False, 4]
        ]

number_grid_normal_1 = [
            [6, 1, 9, e, e, 7, 5, 8, 4],
            [e, e, 4, e, e, e, e, e, 3],
            [e, e, 3, 1, e, 4, e, 7, 9],
            [e, 2, 1, e, 8, e, e, 3, e],
            [9, e, e, e, e, 2, e, e, 6],
            [4, e, 7, e, 9, 1, e, e, e],
            [e, 7, e, 9, e, 8, 2, e, e],
            [8, e, 2, e, e, e, 3, e, e],
            [e, 4, e, e, e, e, 7, e, e]
        ]

number_grid_normal_1_values = [
            [6, 1, 9, False, False, 7, 5, 8, 4],
            [False, False, 4, False, False, False, False, False, 3],
            [False, False, 3, 1, False, 4, False, 7, 9],
            [False, 2, 1, False, 8, False, False, 3, False],
            [9, False, False, False, False, 2, False, False, 6],
            [4, False, 7, False, 9, 1, False, False, False],
            [False, 7, False, 9, False, 8, 2, False, False],
            [8, False, 2, False, False, False, 3, False, False],
            [False, 4, False, False, False, False, 7, False, False]
        ]

grid_easy_complete = [
            [9, 4, 3, 8, 1, 5, 7, 2, 6],
            [1, 7, 8, 9, 6, 2, 3, 4, 5],
            [6, 5, 2, 4, 3, 7, 8, 9, 1],
            [2, 3, 1, 6, 5, 8, 4, 7, 9],
            [4, 6, 7, 2, 9, 1, 5, 3, 8],
            [8, 9, 5, 7, 4, 3, 1, 6, 2],
            [7, 2, 4, 5, 8, 6, 9, 1, 3],
            [5, 1, 9, 3, 2, 4, 6, 8, 7],
            [3, 8, 6, 1, 7, 9, 2, 5, 4]
        ]


class TestGame(unittest.TestCase):

    def setUp(self):
        self.functions = Functions()
        self.grids = SudokuGrid()
        self.repo = Repository()
        self.error = self.functions.error
        self.grid1 = self.grids.number_grid_easy_1
        self.grid1_values = self.grids.number_grid_easy_1_values

    def test_0_returns_none(self):
        self.assertEqual(self.functions.check(0, 2, 0, number_grid_easy_1), None)

    def test_seemingly_correct_number_returns_no_error(self):
        self.grids.number_grid_easy_1[0][0] = 1
        self.assertEqual(self.functions.check(1, 0, 0, self.grids.number_grid_easy_1), None)

    def test_definitely_incorrect_number_returns_error_vertical(self):
        number_grid_easy_1[0][0] = 8
        self.assertEqual(self.functions.check(8, 0, 0, number_grid_easy_1), (0, 0))

    def test_definitely_incorrect_number_returns_error_horizontal(self):
        number_grid_easy_1[5][5] = 8
        self.assertEqual(self.functions.check(8, 5, 5, number_grid_easy_1), (5, 5))

    def test_definitely_incorrect_number_returns_error_square1(self):
        number_grid_easy_1[0][0] = 7
        self.assertEqual(self.functions.check_squares(0, 0, number_grid_easy_1), (0, 0))

    def test_definitely_incorrect_number_returns_error_square2(self):
        number_grid_easy_1[0][3] = 6
        self.assertEqual(self.functions.check_squares(0, 3, number_grid_easy_1), (0, 3))

    def test_definitely_incorrect_number_returns_error_square3(self):
        number_grid_easy_1[0][8] = 9
        self.assertEqual(self.functions.check_squares(0, 8, number_grid_easy_1), (0, 8))

    def test_definitely_incorrect_number_returns_error_square4(self):
        number_grid_easy_1[3][0] = 7
        self.assertEqual(self.functions.check_squares(3, 0, number_grid_easy_1), (3, 0))

    def test_definitely_incorrect_number_returns_error_square5(self):
        number_grid_easy_1[4][3] = 5
        self.assertEqual(self.functions.check_squares(4, 3, number_grid_easy_1), (4, 3))

    def test_definitely_incorrect_number_returns_error_square6(self):
        number_grid_easy_1[4][8] = 6
        self.assertEqual(self.functions.check_squares(4, 8, number_grid_easy_1), (4, 8))

    def test_definitely_incorrect_number_returns_error_square7(self):
        number_grid_easy_1[8][0] = 1
        self.assertEqual(self.functions.check_squares(8, 0, number_grid_easy_1), (8, 0))

    def test_definitely_incorrect_number_returns_error_square8(self):
        number_grid_easy_1[8][3] = 2
        self.assertEqual(self.functions.check_squares(8, 3, number_grid_easy_1), (8, 3))

    def test_definitely_incorrect_number_returns_error_square9(self):
        number_grid_normal_1[8][8] = 2
        self.assertEqual(self.functions.check_squares(8, 8, number_grid_normal_1), (8, 8))

    def test_correct_sudoku_is_chosen_when_easy_is_chosen(self):
        self.assertEqual(self.functions.build_sudoku(0),
                         (self.grids.number_grid_easy_1, self.grids.number_grid_easy_1_values))

    def test_correct_sudoku_is_chosen_when_normal_is_chosen(self):
        self.assertEqual(self.functions.build_sudoku(1),
                         (self.grids.number_grid_normal_1, self.grids.number_grid_normal_1_values))

    def test_correct_sudoku_is_chosen_when_hard_is_chosen(self):
        self.assertEqual(self.functions.build_sudoku(2),
                         (self.grids.number_grid_hard_1, self.grids.number_grid_hard_1_values))

    def test_complete_grid_returns_victory(self):
        self.assertEqual(self.functions.check_if_grid_full(grid_easy_complete), "victory")
