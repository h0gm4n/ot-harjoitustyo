
import pygame, sys, os
from pygame.locals import *
from entities.sudoku_grid import SudokuGrid
from services.functions import Functions

import time
pygame.font.init()
dirname = os.path.dirname(__file__)

class Gameplay:
        def __init__(self):
                self.screen = pygame.display.set_mode((600, 600))
                self.error = False
                self.error_font = pygame.font.SysFont("cambria", 10)
                self.timer_font = pygame.font.SysFont("cambria", 15)
                self.victory_font = pygame.font.SysFont("cambria", 20)
                self.return_font = pygame.font.SysFont("cambria", 40)
                self.grids = SudokuGrid()
                self.functions = Functions()
                self.number_font = pygame.font.SysFont("cambria", 25)
                self.mainClock = pygame.time.Clock()
                self.RED = (255, 0, 0)
                self.GREY = (128, 128, 128)
                self.full = False
                self.start = False
                self.elapsed_time = False
                self.return_rect = pygame.Rect(200, 270, 200, 50)
                self.timer_rect = pygame.Rect(500, 5, 80, 20)
                self.mx, self.my = pygame.mouse.get_pos()
                self.click = False
                self.session = False
                self.running = False

        def sure(self):
                """Varmistaa, haluaako pelaaja keskeyttää sudokun

                Returns:
                        Palauttaa True, jos painetaan ESC, ja False, jos painetaan Enter
                """
                while self.running:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                return True
                                        elif event.key == K_RETURN:
                                                return False

                        pygame.draw.rect(self.screen, (255, 255, 255), self.return_rect)
                        pygame.draw.rect(self.screen, (0, 0, 0), self.return_rect, 1)
                        self.functions.draw_text('Haluatko varmasti keskeyttää?', self.timer_font, (0, 0, 0),
                                                 self.screen, 205, 272)
                        self.functions.draw_text('ESC = Poistu', self.error_font, self.RED, self.screen, 269, 290)
                        self.functions.draw_text('ENTER = Jatka', self.error_font, self.RED, self.screen, 265, 302)
                        self.end = time.time()
                        pygame.draw.rect(self.screen, (255, 255, 255), self.timer_rect)
                        self.timer(self.start, self.end)
                        pygame.display.update()
                        self.mainClock.tick(60)

        def game_loop(self, difficulty):
                """Sudokun täyttämisen käyttöliittymä. Tarkistaa ensin onko Sudokua ensin rakennettu, sitten käynnistää
                timerin ja täyttää täyttämättömän ruudukon arvoja kuvaavan dictionaryn.

                Args:
                        difficulty: Valittu vaikeustaso.
                """
                if not self.session:
                        self.grid = self.functions.build_sudoku(difficulty)[0]
                        self.grid_values = self.functions.build_sudoku(difficulty)[1]
                        self.session = True

                if not self.start:
                        self.start = time.time()

                self.running = True
                self.click = False
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
                                                if self.sure():
                                                        self.running = False
                                                        self.start = False
                                                        self.end = False
                                                        self.session = False
                                                        self.error = False
                                        if event.key >= 48 and event.key <= 57:
                                                if highlight:
                                                        self.grid[highlight[0]][highlight[1]] = event.key - 48
                                                        self.error = self.functions.check(
                                                                self.grid[highlight[0]][highlight[1]], highlight[0],
                                                                highlight[1], self.grid)
                                                        if not self.error:
                                                                self.error = self.functions.check_squares(highlight[0],
                                                                                                          highlight[1],
                                                                                                          self.grid)
                                                        if self.error == "victory":
                                                                self.victory(self.elapsed_time)

                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                self.click = True


                        self.mx, self.my = pygame.mouse.get_pos()

                        self.functions.draw_background()
                        self.functions.draw_numbers(self.grid, self.grid_values)

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

                        self.end = time.time()
                        self.timer(self.start, self.end)
                        pygame.display.update()
                        self.mainClock.tick(60)

        def timer(self, start, end):
                """Timerin ulkoasu.

                Args:
                        start: Lähtöaika.
                        end: Lopetusaika.
                """
                hours, rem = divmod(end - start, 3600)
                minutes, seconds = divmod(rem, 60)
                self.elapsed_time = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)
                self.functions.draw_text(self.elapsed_time, self.timer_font, (0, 0, 0), self.screen, 500, 5)

        def victory(self, elapsed):
                """Voittoruudun käyttöliittymä.

                Args:
                        elapsed: Ratkaisuun käytetty aika.
                """
                self.running = True
                while self.running:
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                self.running = False
                                                self.session = False
                                                self.start = False
                                                self.end = False
                                                self.error = None
                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                self.click = True

                        self.functions.draw_background()
                        self.functions.draw_text('Hyvää työtä!', self.victory_font, (0, 0, 0), self.screen, 5, 5)
                        self.functions.draw_text('Aika: ' + str(elapsed), self.timer_font, (0, 0, 0), self.screen, 150, 5)
                        pygame.draw.rect(self.screen, (255, 255, 255), self.return_rect)
                        pygame.draw.rect(self.screen, (0, 0, 0), self.return_rect, 1)
                        self.functions.draw_text('Palaa painamalla ESC', self.victory_font, (0, 0, 0), self.screen, 210, 282)


                        pygame.display.update()
                        self.mainClock.tick(60)