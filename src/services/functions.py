import os
import pygame
import pygame.locals
from entities.sudoku_grid import SudokuGrid

pygame.font.init()
dirname = os.path.dirname(__file__)


number_font = pygame.font.SysFont("cambria", 25)

screen = pygame.display.set_mode((600, 600))

class Functions:

    def __init__(self):
        self.textrect = None
        self.textobj = None
        self.error = False
        self.grids = False
        self.grid = False
        self.grid_values = False

    def build_sudoku(self, difficulty):
        """Valitsee pelattavan Sudokun.

        Args:
            difficulty: Valittu vaikeustaso

        Returns:
            self.grid, self.grid_values: Tuple, joka sisältää valitun Sudoku-ruudukon ja sen False-arvot
        """
        self.grids = SudokuGrid()
        if difficulty == 0:
            self.grid = self.grids.number_grid_easy_1
            self.grid_values = self.grids.number_grid_easy_1_values
        elif difficulty == 1:
            self.grid = self.grids.number_grid_normal_1
            self.grid_values = self.grids.number_grid_normal_1_values
        elif difficulty == 2:
            self.grid = self.grids.number_grid_hard_1
            self.grid_values = self.grids.number_grid_hard_1_values

        return self.grid, self.grid_values

    def draw_text(self, text, font, color, surface, x, y):
        """Piirtää parametrissä annetun Pygame-tekstin.
        Args:
            text: Haluttu teksti.
            font: Fontti.
            color: Tekstin väri.
            surface: Ruutu, johon teksti piirretään
            x, y: Tekstin koordinaatit
        """
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        surface.blit(self.textobj, self.textrect)

    def draw_numbers(self, grid, grid_values):
        """Piirtää ruudukkoon numerot.

        Args:
            grid: Valittu ruudukko.
            grid_values: Valitun ruudukon False-arvot
        """
        row = 0
        offset = 57
        while row < 9:
            col = 0
            while col < 9:
                output = grid[row][col]
                if not grid_values[row][col]:
                    number_text = number_font.render(
                        str(output), True, (255, 0, 0))
                else:
                    number_text = number_font.render(
                        str(output), True, (0, 0, 0))

                screen.blit(number_text, pygame.Vector2(
                    (col * 60) + offset, (row * 60) + offset))
                col += 1
            row += 1

    def draw_background(self):
        """Piirtää tyhjän Sudoku-ruudukon.
        """
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0),
                         pygame.Rect(35, 40, 540, 540), 5)
        i = 1
        while (i * 60) < 540:
            line_width = 3 if i % 3 > 0 else 6
            pygame.draw.line(screen, (0, 0, 0), pygame.Vector2(
                (i * 60) + 35, 40), pygame.Vector2((i * 60) + 35, 575), line_width)
            pygame.draw.line(screen, (0, 0, 0), pygame.Vector2(
                40, (i * 60) + 45), pygame.Vector2(570, (i * 60) + 45), line_width)
            i += 1

    def check(self, k, y, x, grid):
        """Tarkistaa, onko ruudukossa virhe (jolloin täyttöä ei voi jatkaa ennen virheen korjaamista),
        onko syötetty numero 0 (jolloin ruutu tyhjenee, mikäli siinä oli jokin numero) ja onko pysty- tai vaakarivissä
        numeroa joka on ristiriidassa syötetyn numeron kanssa.

        Args:
            k: Syötetty numero.
            y, x: Ruudun koordinaatit.
            grid: Täytettävä ruudukko.
        Returns:
            None: Palauttaa arvon None muuttujalle self.error.
            y, x: Tuple joka sisältää sen ruudun, joka on ilmeisen virheellinen.
            self.check_if_grid_full(grid): Palauttaa tiedon siitä, onko ruudukko täynnä.
        """
        if self.error and (y, x) != self.error:
            grid[y][x] = ""
            return

        if k == 0:
            grid[y][x] = ""
            return None

        for i in range(9):
            if i != x and grid[y][i] == k:
                return y, x

        for i in range(9):
            if i != y and grid[i][x] == k:
                return y, x

        return self.check_if_grid_full(grid)

    def check_squares(self, y, x, grid):
        """Tarkistaa, onko ruutuun asetettu numero ristiriidassa samassa 3x3-ruudukossa olevien numeroiden kanssa.

        Args:
            y, x: Ruudun koordinaatit.
            grid: Täytettävä ruudukko.

        Returns:
            y, x: Tuple joka sisältää sen ruudun, joka on ilmeisen virheellinen.
            self.check_if_grid_full(grid): Palauttaa tiedon siitä, onko ruudukko täynnä.
        """

        if y <= 2 and x <= 2:
            for i in range(3):
                for j in range(3):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif y <= 2 and 3 <= x <= 5:
            for i in range(0, 3):
                for j in range(3, 6):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif y <= 2 and 6 <= x <= 8:
            for i in range(0, 3):
                for j in range(6, 9):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 3 <= y <= 5 and x <= 2:
            for i in range(3, 6):
                for j in range(3):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 3 <= y <= 5 and 3 <= x <= 5:
            for i in range(3, 6):
                for j in range(3, 6):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 3 <= y <= 5 and 6 <= x <= 8:
            for i in range(3, 6):
                for j in range(6, 9):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 6 <= y <= 8 and x <= 2:
            for i in range(6, 9):
                for j in range(3):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 6 <= y <= 8 and 3 <= x <= 5:
            for i in range(6, 9):
                for j in range(3, 6):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        elif 6 <= y <= 8 and 6 <= x <= 8:
            for i in range(6, 9):
                for j in range(6, 9):
                    if (i, j) != (y, x) and grid[i][j] == grid[y][x] and grid[i][j] != "":
                        return y, x

        return self.check_if_grid_full(grid)

    def check_if_grid_full(self, grid):
        """Tarkistaa, onko ruudukko täytetty.

        Args:
            grid: Täytettävä ruudukko.

        Returns:
            "victory": Asettaa arvon "victory" muuttujalle self.victory
            None: Asettaa arvon None muuttujalle self.victory
        """
        a = 0
        for i in grid:
            for j in i:
                if j != "":
                    a += 1

        if a == 81:
            return "victory"
        else:
            return None