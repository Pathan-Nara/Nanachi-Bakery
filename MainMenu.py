import pygame
from Game import Game
from components.constants import FONT
from components.ListSaveMenu import ListSaveMenu
from components.Button import Button

pygame.init()

class MainMenu:

    def __init__(self, screen):
        self.screen = screen
        self.start_btn = Button('Start Game', (400, 100), FONT)
        self.save_btn = Button('Load Save', (400, 250), FONT)
        self.quit_btn = Button('Quit', (400, 350), FONT)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.start_btn.draw(self.screen)
        self.save_btn.draw(self.screen)
        self.quit_btn.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.is_clicked(event.pos):
                game = Game()
                game.run()
            elif self.save_btn.is_clicked(event.pos):
                list_save_menu = ListSaveMenu(self.screen)
                list_save_menu.run()
            elif self.quit_btn.is_clicked(event.pos):
                pygame.quit()
                exit()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
            self.draw()
        pygame.quit()