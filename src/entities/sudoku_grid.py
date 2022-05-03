

class SudokuGrid:

    def __init__(self):
        e = ""
        self.number_grid_easy_1 = [
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
        self.number_grid_easy_1_values = [
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




        self.number_grid_normal_1 = [
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
        self.number_grid_normal_1_values = [
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
        self.number_grid_hard_1 = [
            [e, 6, e, e, e, 3, e, e, 2],
            [e, e, e, e, 5, e, e, 6, 8],
            [e, e, e, e, 8, e, e, e, e],
            [e, 2, e, 3, e, e, e, e, e],
            [e, 7, e, e, 9, e, 6, e, 5],
            [8, e, 1, e, e, 6, 9, e, 4],
            [6, e, e, 4, e, e, 2, e, e],
            [e, 3, 4, 1, e, e, 8, 5, e],
            [e, e, e, 5, 3, 8, 4, e, e]
        ]
        self.number_grid_hard_1_values = [
            [False, 6, False, False, False, 3, False, False, 2],
            [False, False, False, False, 5, False, False, 6, 8],
            [False, False, False, False, 8, False, False, False, False],
            [False, 2, False, 3, False, False, False, False, False],
            [False, 7, False, False, 9, False, 6, False, 5],
            [8, False, 1, False, False, 6, 9, False, 4],
            [6, False, False, 4, False, False, 2, False, False],
            [False, 3, 4, 1, False, False, 8, 5, False],
            [False, False, False, 5, 3, 8, 4, False, False]
        ]





sudoku_grid = SudokuGrid()
