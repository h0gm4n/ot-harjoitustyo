import pygame
import sys
import os
from pygame.locals import *
from entities.sudoku_grid import SudokuGrid
from services.functions import Functions

import time

pygame.font.init()
dirname = os.path.dirname(__file__)


class Gameplay:
    """Luokka pääosin pelisession käyttöliittymälle.
    """
    def __init__(self):
        """Konstruktori
        """
        self.screen = pygame.display.set_mode((600, 600))
        self.error = False
        self.error_font = pygame.font.SysFont("cambria", 10)
        self.timer_font = pygame.font.SysFont("cambria", 15)
        self.victory_font = pygame.font.SysFont("cambria", 20)
        self.return_font = pygame.font.SysFont("cambria", 40)
        self.number_font = pygame.font.SysFont("cambria", 25)
        self.grids = SudokuGrid()
        self.functions = Functions()
        self.mainClock = pygame.time.Clock()
        self.RED = (255, 0, 0)
        self.start = False
        self.end = False
        self.elapsed_time = False
        self.return_rect = pygame.Rect(200, 180, 200, 50)
        self.esc_rect = pygame.Rect(200, 270, 200, 50)
        self.timer_rect = pygame.Rect(500, 5, 80, 20)
        self.mx, self.my = pygame.mouse.get_pos()
        self.click = False
        self.session = False
        self.running = False
        self.input_box = pygame.Rect(105, 250, 400, 200)
        self.difficulty = None

    def sure(self):
        """Varmistaa, haluaako pelaaja keskeyttää sudokun

        Returns:
                Palauttaa True, jos painetaan ESC, ja False, jos painetaan Enter.
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

            pygame.draw.rect(self.screen, (255, 255, 255), self.esc_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.esc_rect, 1)
            self.functions.draw_text('Haluatko varmasti keskeyttää?', self.timer_font, (0, 0, 0),
                                     self.screen, 205, 272)
            self.functions.draw_text('ESC = Poistu', self.error_font, self.RED, self.screen, 269, 290)
            self.functions.draw_text('ENTER = Jatka', self.error_font, self.RED, self.screen, 265, 302)
            self.end = time.time()
            pygame.draw.rect(self.screen, (255, 255, 255), self.timer_rect)
            self.timer(self.start, self.end)
            pygame.display.update()
            self.mainClock.tick(60)

    def shut_down(self):
        """Asettaa useita muuttujia False-tilaan.
        """
        self.running = False
        self.start = False
        self.end = False
        self.session = False
        self.error = None

    def game_loop(self, difficulty):
        """Sudokun täyttämisen käyttöliittymä. Tarkistaa ensin onko Sudokua ensin rakennettu, sitten käynnistää
        timerin ja täyttää täyttämättömän ruudukon arvoja kuvaavan dictionaryn.

        Args:
                difficulty: Valittu vaikeustaso.
        """

        self.difficulty = difficulty

        if not self.session:
            self.grid = self.functions.build_sudoku(difficulty)[0]
            self.grid_values = self.functions.build_sudoku(difficulty)[1]
            self.session = True

        if not self.start:
            self.start = time.time()

        difficulty_text = ""

        if self.difficulty == 0:
            difficulty_text = "Helppo"
        elif self.difficulty == 1:
            difficulty_text = "Normaali"
        elif self.difficulty == 2:
            difficulty_text = "Vaikea"

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
                            self.shut_down()
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
                        square = pygame.Rect(40 + (i * x_factor), 48 + (j * y_factor), 50, 50)
                        square_values = (j, i)
                        if square.collidepoint((self.mx, self.my)):
                            if not self.error:
                                pygame.draw.rect(self.screen, self.RED, square, 2)
                                highlight = square_values
                            elif square_values == self.error and self.error:
                                pygame.draw.rect(self.screen, self.RED, square, 2)

            if highlight:
                second_square = pygame.Rect(40 + (highlight[1] * x_factor), 48 + (highlight[0] * y_factor), 50, 50)
                pygame.draw.rect(self.screen, self.RED, second_square, 2)
            if self.error:
                self.functions.draw_text('Väärin! - Pyyhi painamalla 0', self.error_font, (255, 0, 0), self.screen, 5,
                                         5)

            self.functions.draw_text(difficulty_text, self.victory_font, (0, 0, 0), self.screen, 270, 5)

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
        self.session = False
        arrow_blink = time.time()
        player_name = ""
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.shut_down()
                    elif event.key == K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif 122 >= int(event.key) >= 97 and len(player_name) <= 9:
                        player_name += event.unicode
                    elif event.key == K_RETURN and player_name != "":
                        self.functions.write_time(player_name, str(elapsed), self.difficulty)
                        self.shut_down()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            self.functions.draw_background()
            pygame.draw.rect(self.screen, (255, 255, 255), self.return_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.return_rect, 1)
            pygame.draw.rect(self.screen, (255, 255, 255), self.input_box)
            pygame.draw.rect(self.screen, (0, 0, 0), self.input_box, 1)
            self.functions.draw_text('Palaa painamalla ESC', self.victory_font, (0, 0, 0), self.screen, 210,
                                     193)
            self.functions.draw_text('Hyvää työtä!', self.victory_font, (0, 0, 0), self.screen, 243, 260)
            self.functions.draw_text('Aika: ' + str(elapsed), self.timer_font, (0, 0, 0), self.screen, 252,
                                     290)
            self.functions.draw_text('Lisää tulos tulostauluun syöttämällä ', self.victory_font, (0, 0, 0),
                                     self.screen, 150, 320)
            self.functions.draw_text('nimi ja painamalla Enter ', self.victory_font, (0, 0, 0),
                                     self.screen, 197, 347)
            self.functions.draw_text(player_name, self.victory_font, (0, 0, 0),
                                     self.screen, 238, 381)

            arrow_blink_end = time.time()
            arrow_time = arrow_blink_end - arrow_blink
            if str(arrow_time)[1] == ".":
                if int(str(arrow_time)[0]) % 2 == 0:
                    self.functions.draw_text('>',
                                             self.victory_font, (0, 0, 0), self.screen, 220, 380)
            else:
                if int(str(arrow_time)[0:2]) % 2 == 0:
                    self.functions.draw_text('>',
                                             self.victory_font, (0, 0, 0), self.screen, 220, 380)

            pygame.display.update()
            self.mainClock.tick(60)
