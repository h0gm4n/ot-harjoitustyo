import os
import pygame
import pygame.locals

pygame.font.init()
dirname = os.path.dirname(__file__)

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

number_font = pygame.font.SysFont("cambria", 25)

screen = pygame.display.set_mode((600, 600))

class Functions:

    def __init__(self):
        self.textrect = None
        self.textobj = None
        self.error = False

    def draw_text(self, text, font, color, surface, x, y):
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        surface.blit(self.textobj, self.textrect)

    def draw_numbers(self, grid):

        row = 0
        offset = 57
        while row < 9:
            col = 0
            while col < 9:
                output = grid[row][col]
                if not grid1_values[row][col]:
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

        a = 0
        for i in grid:
            for j in i:
                if j != "":
                    a += 1

        if a == 81:
            return "victory"

        return None
