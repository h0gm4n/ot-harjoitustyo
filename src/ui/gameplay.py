
import pygame, sys, os
from pygame.locals import *
from ui.sudoku_grid import Sudoku_Grid
pygame.font.init()
dirname = os.path.dirname(__file__)

class Gameplay:
        def __init__(self):
                self.screen = pygame.display.set_mode((600, 600))
                self.X = 0
                self.Z = 0
                self.error = False
                self.error_font = pygame.font.SysFont("cambria", 10)
                self.DIFF = 500 / 9
                self.VALUE = 0
                self.grids = Sudoku_Grid()
                self.GRID1 = self.grids.NUMBER_GRID1
                self.number_font = pygame.font.SysFont("cambria", 25)
                self.mainClock = pygame.time.Clock()
                self.RED = (255, 0, 0)
                self.grid1true = False
                self.sq02hl, self.sq05hl, self.sq06hl, self.sq07hl, self.sq08hl = False, False, False, False, False
                self.sq11hl, self.sq12hl, self.sq15hl, self.sq17hl, self.sq18hl = False, False, False, False, False
                self.sq20hl, self.sq21hl, self.sq23hl, self.sq25hl = False, False, False, False
                self.sq32hl, self.sq33hl, self.sq37hl = False, False, False
                self.sq40hl, self.sq42hl, self.sq43hl, self.sq44hl, self.sq45hl, \
                self.sq47hl, self.sq48hl = False, False, False, False, False, False, False
                self.sq54hl, self.sq56hl, self.sq57hl, self.sq58hl = False, False, False, False
                self.sq60hl, self.sq62hl, self.sq63hl, self.sq67hl, self.sq68hl = False, False, False, False, False
                self.sq70hl, self.sq71hl, self.sq73hl, self.sq74hl, self.sq78hl = False, False, False, False, False
                self.sq80hl, self.sq82hl, self.sq85hl, self.sq87hl = False, False, False, False


        def game_loop(self):
                self.running = True
                self.click = False
                self.grid = self.GRID1
                while self.running:
                        # self.draw_text('game', self.menufont, (0, 0, 0), self.screen, 20, 20)
                        #grid = self.GRID1
                        self.grid1true = True

                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                self.running = False
                                        if event.key >= 48 and event.key <= 57:
                                                if self.sq02hl:
                                                        self.grid[0][2] = event.key - 48
                                                        self.check(self.grid[0][2], 0, 2, self.grid)
                                                if self.sq05hl:
                                                        self.grid[0][5] = event.key - 48
                                                        self.check(self.grid[0][5], 0, 5, self.grid)
                                                if self.sq06hl:
                                                        self.grid[0][6] = event.key - 48
                                                        self.check(self.grid[0][6], 0, 6, self.grid)
                                                if self.sq07hl:
                                                        self.grid[0][7] = event.key - 48
                                                        self.check(self.grid[0][7], 0, 7, self.grid)
                                                if self.sq08hl:
                                                        self.grid[0][8] = event.key - 48
                                                        self.check(self.grid[0][8], 0, 8, self.grid)

                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                self.click = True


                        self.mx, self.my = pygame.mouse.get_pos()

                        self.draw_background()
                        self.draw_numbers(self.grid)
                        self.sq02 = pygame.Rect(155, 40, 60, 65)
                        self.sq05 = pygame.Rect(335, 40, 60, 65)
                        self.sq06 = pygame.Rect(395, 40, 60, 65)
                        self.sq07 = pygame.Rect(455, 40, 60, 65)
                        self.sq08 = pygame.Rect(515, 40, 60, 65)

                        if self.sq02.collidepoint((self.mx, self.my)):
                                self.sq02hl = True
                                pygame.draw.rect(self.screen, self.RED, self.sq02, 5)
                        else:
                                self.sq02hl = False

                        if self.sq05.collidepoint((self.mx, self.my)):
                                self.sq05hl = True
                                pygame.draw.rect(self.screen, self.RED, self.sq05, 5)
                        else:
                                self.sq05hl = False

                        if self.sq06.collidepoint((self.mx, self.my)):
                                self.sq06hl = True
                                pygame.draw.rect(self.screen, self.RED, self.sq06, 5)
                        else:
                                self.sq06hl = False

                        if self.sq07.collidepoint((self.mx, self.my)):
                                self.sq07hl = True
                                pygame.draw.rect(self.screen, self.RED, self.sq07, 5)
                        else:
                                self.sq07hl = False

                        if self.sq08.collidepoint((self.mx, self.my)):
                                self.sq08hl = True
                                pygame.draw.rect(self.screen, self.RED, self.sq08, 5)
                        else:
                                self.sq08hl = False

                        if self.error:
                                self.draw_text('Väärin!', self.error_font, (255, 0, 0), self.screen, 5, 5)

                        pygame.display.update()
                        self.mainClock.tick(60)

        def check(self, k, y, x, grid):

                if k == 0:
                        grid[y][x] = ""
                        self.error = False
                        return

                for i in range(9):
                        if i != x and grid[y][i] == k:
                                self.error = True
                                return
                        else:
                                continue

                for i in range(9):
                        if i != y and grid[i][x] == k:
                                self.error = True
                                return
                        else:
                                continue

                if y <= 2 and x <= 2:
                        for i in range(3):
                                for j in range(3):
                                        if (i, j) != (y, x) and grid[i][j] == grid[y][x]:
                                                self.error = True
                                                return
                                        else:
                                                continue
                if y <= 2 and 3 <= x <= 5:
                        for i in range(0, 2):
                                for j in range(3, 5):
                                        if (i, j) != (y, x) and grid[i][j] == grid[y][x]:
                                                self.error = True
                                                return
                                        else:
                                                continue
                if y <= 2 and 6 <= x <= 8:
                        for i in range(0, 2):
                                for j in range(6, 8):
                                        if (i, j) != (y, x) and grid[i][j] == grid[y][x]:
                                                self.error = True
                                                return
                                        else:
                                                continue

                self.error = False


        def draw_background(self):
                self.screen.fill((255, 255, 255))
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 pygame.Rect(35, 40, 540, 540), 5)
                i = 1
                while (i * 60) < 540:
                        line_width = 3 if i % 3 > 0 else 6
                        pygame.draw.line(self.screen, (0, 0, 0), pygame.Vector2(
                                (i * 60) + 35, 40), pygame.Vector2((i * 60) + 35, 575), line_width)
                        pygame.draw.line(self.screen, (0, 0, 0), pygame.Vector2(
                                40, (i * 60) + 45), pygame.Vector2(570, (i * 60) + 45), line_width)
                        i += 1

        def draw_numbers(self, grid):

                row = 0
                offset = 57
                while row < 9:
                        col = 0
                        while col < 9:
                                output = grid[row][col]

                                number_text = self.number_font.render(
                                        str(output), True, (0, 0, 0))
                                self.screen.blit(number_text, pygame.Vector2(
                                        (col * 60) + offset, (row * 60) + offset))
                                col += 1
                        row += 1

        def draw_text(self, text, font, color, surface, x, y):
                self.textobj = font.render(text, 1, color)
                self.textrect = self.textobj.get_rect()
                self.textrect.topleft = (x, y)
                surface.blit(self.textobj, self.textrect)


#g = Gameplay()
#g.game_loop()