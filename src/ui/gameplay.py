
import pygame, sys, os
from pygame.locals import *
from entities.sudoku_grid import SudokuGrid
from services.functions import Functions
pygame.font.init()
dirname = os.path.dirname(__file__)

class Gameplay:
        def __init__(self):
                self.screen = pygame.display.set_mode((600, 600))
                self.error = False
                self.error_font = pygame.font.SysFont("cambria", 10)
                self.victory_font = pygame.font.SysFont("cambria", 20)
                self.grids = SudokuGrid()
                self.functions = Functions()
                self.grid1 = self.grids.number_grid1
                self.grid1_values = self.grids.number_grid1_values
                self.number_font = pygame.font.SysFont("cambria", 25)
                self.mainClock = pygame.time.Clock()
                self.RED = (255, 0, 0)
                self.GREY = (128, 128, 128)
                self.grid1true = False
                self.full = False



        def game_loop(self):
                self.running = True
                self.click = False
                self.grid = self.grid1
                self.grid_values = self.grid1_values
                x_factor = 60
                y_factor = 60
                grid_value_dict = {}
                highlight = None
                for i in range(0, 9):
                        for j in range(0, 9):
                                string = f"{str(i)}{str(j)}"
                                grid_value_dict[string] = self.grid_values[i][j]

                while self.running:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                self.running = False
                                        if event.key >= 48 and event.key <= 57:
                                                if highlight:
                                                        self.grid[highlight[0]][highlight[1]] = event.key - 48
                                                        self.error = self.functions.check(self.grid[highlight[0]][highlight[1]], highlight[0],
                                                                   highlight[1], self.grid)
                                                        if self.error == "victory":
                                                                self.victory()

                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                self.click = True


                        self.mx, self.my = pygame.mouse.get_pos()

                        self.functions.draw_background()
                        self.functions.draw_numbers(self.grid)

                        for i in range(9):
                                for j in range(9):
                                        square = f"{str(j)}{str(i)}"
                                        if not grid_value_dict[square]:
                                                square = pygame.Rect(40+(i*x_factor), 48+(j*y_factor), 50, 50)
                                                square_values = (j, i)
                                                if square.collidepoint((self.mx, self.my)):
                                                        if not self.error:
                                                                pygame.draw.rect(self.screen, self.RED, square, 2)
                                                                highlight = square_values
                                                        elif square_values == self.error and self.error:
                                                                pygame.draw.rect(self.screen, self.RED, square, 2)

                        if highlight:
                                second_square = pygame.Rect(40+(highlight[1]*x_factor), 48+(highlight[0]*y_factor), 50, 50)
                                pygame.draw.rect(self.screen, self.RED, second_square, 2)
                        if self.error:
                                self.functions.draw_text('Väärin!', self.error_font, (255, 0, 0), self.screen, 5, 5)

                        pygame.display.update()
                        self.mainClock.tick(60)

        def victory(self):
                self.running = True

                while self.running:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                self.running = False

                        self.functions.draw_background()
                        self.functions.draw_text('Hyvää työtä!', self.victory_font, (0, 0, 0), self.screen, 5, 5)

                        pygame.display.update()
                        self.mainClock.tick(60)