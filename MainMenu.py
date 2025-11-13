import pygame
from Game import Game
from components.constants import FONT
from components.ListSaveMenu import ListSaveMenu
pygame.init()
class MainMenu:

    def __init__(self, screen):
        self.screen = screen
        self.start_text = FONT.render('Start Game', True, (255, 255, 255))
        self.save_text = FONT.render('Load Save', True, (255, 255, 255))
        self.quit_text = FONT.render('Quit', True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(400, 100))
        self.save_rect = self.save_text.get_rect(center=(400, 250))
        self.quit_rect = self.quit_text.get_rect(center=(400, 350))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.start_text, self.start_rect)
        self.screen.blit(self.save_text, self.save_rect)
        self.screen.blit(self.quit_text, self.quit_rect)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_rect.collidepoint(event.pos):
                game = Game()
                game.run()
            elif self.save_rect.collidepoint(event.pos):
                list_save_menu = ListSaveMenu(self.screen)
                list_save_menu.run()


            elif self.quit_rect.collidepoint(event.pos):
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
    