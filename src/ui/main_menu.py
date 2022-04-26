from ui.gameplay import Gameplay
import pygame, sys, os
from pygame.locals import *
pygame.font.init()

dirname = os.path.dirname(__file__)

class MainMenu:

    def __init__(self):
        pygame.init()
        self.g = Gameplay()
        self.screen = pygame.display.set_mode((600, 600), 0, 32)
        self.mainClock = pygame.time.Clock()
        self.menufont = pygame.font.SysFont("cambria", 100)
        self.menufont2 = pygame.font.SysFont("cambria", 102)
        self.menufont3 = pygame.font.SysFont("cambria", 40)


    def run_main_menu(self):
        self.click = False
        while True:
            self.screen.fill((255, 255, 255))

            self.mx, self.my = pygame.mouse.get_pos()



            self.draw_text("Sudoku", self.menufont, (0, 0, 0), self.screen, 135, 150)
            self.draw_text('Peliin', self.menufont3, (0, 0, 0), self.screen, 248, 298)
            self.draw_text('Tulokset', self.menufont3, (0, 0, 0), self.screen, 225, 400)

            self.peliin = pygame.Rect(200, 300, 200, 50)
            self.tulokset = pygame.Rect(200, 400, 200, 50)


            if self.peliin.collidepoint((self.mx, self.my)):
                if self.click:
                    self.difficulty()

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

    def draw_text(self, text, font, color, surface, x, y):
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        surface.blit(self.textobj, self.textrect)

    def difficulty(self):

        while True:

            self.screen.fill((255, 255, 255))

            self.draw_text('Helppo', self.menufont3, (127, 127, 127), self.screen, 236, 208)
            self.draw_text('Normaali', self.menufont3,(0, 0, 0), self.screen, 218, 268)
            self.draw_text('Vaikea', self.menufont3,(127, 127, 127), self.screen, 240, 328)

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
                        self.run_main_menu()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if self.normaali.collidepoint((self.mx, self.my)):
                    if self.click:
                        self.g.game_loop()

            pygame.display.update()
            self.mainClock.tick(60)

