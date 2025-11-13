import pygame
from Game import Game
from components.constants import FONT
from components.ListSaveMenu import ListSaveMenu
from components.Button import Button

pygame.init()

class MainMenu:

    def __init__(self, screen):
        self.screen = screen
        screen_w = screen.get_width()
        screen_h = screen.get_height()
        center_x = screen_w // 2
        self.start_btn = Button('Start Game', (center_x, screen_h // 4), FONT)
        self.save_btn = Button('Load Save', (center_x, screen_h // 2), FONT)
        self.quit_btn = Button('Quit', (center_x, 3 * screen_h // 4), FONT)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.start_btn.draw(self.screen)
        self.save_btn.draw(self.screen)
        self.quit_btn.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.is_hovered(event.pos):
                game = Game()
                game.run()
            elif self.save_btn.is_hovered(event.pos):
                list_save_menu = ListSaveMenu(self.screen)
                list_save_menu.run()
            elif self.quit_btn.is_hovered(event.pos):
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