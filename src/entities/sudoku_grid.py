

class SudokuGrid:

    def __init__(self):
        #self.gameplay = Gameplay()
        e = ""
        self.number_grid1 = [
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
        self.number_grid1_values = [
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
        self.number_grid2 = [
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
        self.number_grid2_values = [
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


sudoku_grid = SudokuGrid()
