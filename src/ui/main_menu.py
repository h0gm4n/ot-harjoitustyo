from ui.gameplay import Gameplay
from ui.results import Results
from services.functions import Functions
from repository.repository import Repository
import pygame
import sys
import os
from pygame.locals import *
pygame.font.init()

dirname = os.path.dirname(__file__)


class MainMenu:

    def __init__(self):
        pygame.init()
        self.g = Gameplay()
        self.r = Results()
        self.f = Functions()
        self.repo = Repository()
        self.screen = pygame.display.set_mode((600, 600), 0, 32)
        self.mainClock = pygame.time.Clock()
        self.menufont = pygame.font.SysFont("cambria", 100)
        self.menufont2 = pygame.font.SysFont("cambria", 102)
        self.menufont3 = pygame.font.SysFont("cambria", 40)
        self.menufont4 = pygame.font.SysFont("cambria", 15)
        self.to_game = pygame.Rect(200, 300, 200, 50)
        self.to_results = pygame.Rect(200, 400, 200, 50)
        self.erase_results = pygame.Rect(5, 5, 135, 30)
        self.erase_confirmation = pygame.Rect(200, 50, 200, 100)
        self.click = False
        self.mx, self.my = pygame.mouse.get_pos()
        self.easy = pygame.Rect(200, 210, 200, 50)
        self.normal = pygame.Rect(200, 270, 200, 50)
        self.hard = pygame.Rect(200, 330, 200, 50)

    def run_main_menu(self):
        self.click = False
        confirm_box = False
        self.repo.create_or_maintain_result_files()
        while True:
            self.screen.fill((255, 255, 255))

            self.mx, self.my = pygame.mouse.get_pos()

            self.f.draw_text("Tyhjennä tulostaulu", self.menufont4, (0, 0, 0), self.screen, 10, 10)
            self.f.draw_text("Sudoku", self.menufont, (0, 0, 0), self.screen, 135, 150)
            self.f.draw_text('Peliin', self.menufont3, (0, 0, 0), self.screen, 248, 298)
            self.f.draw_text('Tulokset', self.menufont3, (0, 0, 0), self.screen, 225, 400)

            if self.to_game.collidepoint((self.mx, self.my)):
                if self.click:
                    self.difficulty()
            elif self.to_results.collidepoint((self.mx, self.my)):
                if self.click:
                    self.r.show_results()
            elif self.erase_results.collidepoint((self.mx, self.my)):
                if self.click and confirm_box:
                    confirm_box = False
                elif self.click:
                    confirm_box = True

            pygame.draw.rect(self.screen, (0, 0, 0), self.to_game, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.to_results, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.erase_results, 1)

            if confirm_box:
                pygame.draw.rect(self.screen, (0, 0, 0), self.erase_confirmation, 1)
                self.f.draw_text("Haluatko varmasti", self.menufont4, (0, 0, 0), self.screen, 240, 60)
                self.f.draw_text("tyhjentää tulostaulun?", self.menufont4, (0, 0, 0), self.screen, 230, 80)
                self.f.draw_text("ENTER = Tyhjennä", self.menufont4, (255, 0, 0), self.screen, 240, 100)
                self.f.draw_text("ESC = Peruuta", self.menufont4, (255, 0, 0), self.screen, 252, 120)

            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE and not confirm_box:
                        pygame.quit()
                        sys.exit()
                    if confirm_box:
                        if event.key == K_RETURN:
                            self.repo.clear_results()
                            confirm_box = False
                        elif event.key == K_ESCAPE:
                            confirm_box = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def difficulty(self):

        while True:

            self.screen.fill((255, 255, 255))

            self.f.draw_text('Helppo', self.menufont3, (0, 0, 0), self.screen, 236, 208)
            self.f.draw_text('Normaali', self.menufont3, (0, 0, 0), self.screen, 218, 268)
            self.f.draw_text('Vaikea', self.menufont3, (0, 0, 0), self.screen, 240, 328)

            self.mx, self.my = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, (0, 0, 0), self.easy, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.normal, 1)
            pygame.draw.rect(self.screen, (0, 0, 0), self.hard, 1)

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
                if self.easy.collidepoint((self.mx, self.my)):
                    if self.click:
                        self.g.game_loop(0)
                elif self.normal.collidepoint((self.mx, self.my)):
                    if self.click:
                        self.g.game_loop(1)
                elif self.hard.collidepoint((self.mx, self.my)):
                    if self.click:
                        self.g.game_loop(2)

            pygame.display.update()
            self.mainClock.tick(60)
