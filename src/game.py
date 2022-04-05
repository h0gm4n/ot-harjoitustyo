import pygame, sys
import os
from pygame.locals import *

dirname = os.path.dirname(__file__)

class Game:
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        pygame.display.set_caption('Sudoku')
        self.screen = pygame.display.set_mode((600, 600), 0, 32)

        self.PUNAINEN = (255, 0, 0)

        self.menufont = pygame.font.SysFont("cambria", 100)
        self.menufont2 = pygame.font.SysFont("cambria", 102)
        self.menufont3 = pygame.font.SysFont("cambria", 40)

        e = ""
        self.number_grid = [
            [7, 3, e, 9, 5, e, e, e, e],
            [2, e, e, 6, 7, e, 5, 8, e],
            [e, e, 5, e, 1, e, 4, 8, 9],
            [1, 9, e, e, 6, 3, 2, e, 5],
            [e, 4, e, e, e, e, 6, e, e],
            [5, 6, 8, 2, e, 7, e, e, e],
            [e, 2, e, e, 8, 1, 3, e, e],
            [e, e, 1, e, e, 9, 7, 6, e],
            [e, 7, e, 5, 2, e, 8, e, 9]
        ]

        self.number_font = pygame.font.SysFont("cambria", 25)

    def main_menu(self):
        self.click = False
        while True:
            self.screen.fill((255, 255, 255))
            self.draw_text('Sudoku', self.menufont2, (0, 0, 0), self.screen, 139, 149)
            self.draw_text('Peliin', self.menufont3, (0, 0, 0), self.screen, 248, 298)
            self.draw_text('Tulokset', self.menufont3, (0, 0, 0), self.screen, 225, 400)

            self.mx, self.my = pygame.mouse.get_pos()

            self.peliin = pygame.Rect(200, 300, 200, 50)
            self.tulokset = pygame.Rect(200, 400, 200, 50)

            if self.peliin.collidepoint((self.mx, self.my)):
                if self.click:
                    self.vaikeustaso()
            if self.tulokset.collidepoint((self.mx, self.my)):
                if self.click:
                    self.options()
            pygame.draw.rect(self.screen, (0, 0, 0), self.peliin, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.tulokset, 1)

            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def draw_numbers(self, grid):

        row = 0
        offset = 57
        while row < 9:
            col = 0
            while col < 9:
                output = self.number_grid[row][col]

                number_text = self.number_font.render(str(output), True, (0, 0, 0))
                self.screen.blit(number_text, pygame.Vector2((col * 60) + offset, (row * 60) + offset))
                col += 1
            row += 1


    def draw_text(self, text, font, color, surface, x, y):
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        surface.blit(self.textobj, self.textrect)

    def draw_background(self):
        a=1

    click = False

    def vaikeustaso(self):
        while True:

            self.screen.fill((255, 255, 255))

            self.draw_text('Helppo', self.menufont3, (0, 0, 0), self.screen, 236, 208)
            self.draw_text('Normaali', self.menufont3, (0, 0, 0), self.screen, 218, 268)
            self.draw_text('Vaikea', self.menufont3, (0, 0, 0), self.screen, 240, 328)

            self.mx, self.my = pygame.mouse.get_pos()

            self.helppo = pygame.Rect(200, 210, 200, 50)
            self.normaali = pygame.Rect(200, 270, 200, 50)
            self.vaikea = pygame.Rect(200, 330, 200, 50)

            pygame.draw.rect(self.screen, (0, 0, 0), self.helppo, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.normaali, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.vaikea, 1)

            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.main_menu()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if self.normaali.collidepoint((self.mx, self.my)):
                    if self.click:
                        self.game()

            pygame.display.update()
            self.mainClock.tick(60)

    def draw_background(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(35, 40, 540, 540), 5)
        i = 1
        while (i * 60) < 540:
            line_width = 3 if i % 3 > 0 else 6
            pygame.draw.line(self.screen, (0, 0, 0), pygame.Vector2((i * 60) + 35, 40), pygame.Vector2((i * 60) + 35, 575), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), pygame.Vector2(40, (i * 60) + 45), pygame.Vector2(570, (i * 60) + 45), line_width)
            i += 1

    def game(self):
        self.running = True
        self.click = False
        while self.running:
            #self.draw_text('game', self.menufont, (0, 0, 0), self.screen, 20, 20)

            grid = self.number_grid

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            self.mx, self.my = pygame.mouse.get_pos()

            self.draw_background()
            self.draw_numbers(grid)
            self.sq11 = pygame.Rect(35, 40, 60, 65)


            if self.sq11.collidepoint((self.mx, self.my)):
                pygame.draw.rect(self.screen, self.PUNAINEN, self.sq11, 5)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_1:
                        grid[0][0]=int(event.key[2])

            pygame.display.update()
            self.mainClock.tick(60)