from services.functions import Functions
import pygame
import sys
import os
import csv
import operator
from pygame.locals import *
pygame.font.init()

dirname = os.path.dirname(__file__)

easy_results_repository = (os.path.join(dirname, "..", "data", "easy_results.csv"))
normal_results_repository = (os.path.join(dirname, "..", "data", "normal_results.csv"))
hard_results_repository = (os.path.join(dirname, "..", "data", "hard_results.csv"))


class Results:

    def __init__(self):
        pygame.init()
        self.functions = Functions()
        self.screen = pygame.display.set_mode((600, 600), 0, 32)
        self.mainClock = pygame.time.Clock()
        self.running = False
        self.results_font = pygame.font.SysFont("cambria", 70)
        self.results_font_2 = pygame.font.SysFont("cambria", 20)
        self.results_font_3 = pygame.font.SysFont("cambria", 30)

    def show_results(self):
        self.running = True
        while self.running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            self.functions.draw_text('Tulokset ', self.results_font, (0, 0, 0), self.screen, 160, 30)
            self.functions.draw_text('Helppo ', self.results_font_3, (0, 0, 0), self.screen, 240, 130)
            self.functions.draw_text('Normaali ', self.results_font_3, (0, 0, 0), self.screen, 229, 260)
            self.functions.draw_text('Vaikea ', self.results_font_3, (0, 0, 0), self.screen, 246, 405)

            if os.path.getsize(easy_results_repository) != 0:
                easy_data = csv.reader(open(easy_results_repository), delimiter=",")
                easy_data = sorted(easy_data, key=operator.itemgetter(1))
                self.functions.present_results_easy(easy_data)
            if os.path.getsize(normal_results_repository) != 0:
                normal_data = csv.reader(open(normal_results_repository), delimiter=",")
                normal_data = sorted(normal_data, key=operator.itemgetter(1))
                self.functions.present_results_normal(normal_data)
            if os.path.getsize(hard_results_repository) != 0:
                hard_data = csv.reader(open(hard_results_repository), delimiter=",")
                hard_data = sorted(hard_data, key=operator.itemgetter(1))
                self.functions.present_results_hard(hard_data)
            pygame.display.update()
            self.mainClock.tick(60)
