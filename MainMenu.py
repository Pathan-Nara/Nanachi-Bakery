import pygame
from Game import Game
from components.constants import FONT
from components.ListSaveMenu import ListSaveMenu
from components.MainMenuButton import MainMenuButton
from components.Credits import Credits

pygame.init()

class MainMenu:

    def __init__(self, screen):
        self.screen = screen
        screen_w = screen.get_width()
        screen_h = screen.get_height()
        center_x = screen_w // 2
        center_y = screen_h // 2
        
        self.start_btn = MainMenuButton("Start Game", pygame.Rect(center_x - 100, center_y - 80, 200, 50), FONT, default_color=(0, 0, 255))
        self.save_btn = MainMenuButton("Load Game", pygame.Rect(center_x - 100, center_y, 200, 50), FONT, default_color=(0, 100, 255))
        self.credit_btn = MainMenuButton("Credits", pygame.Rect(center_x - 100, center_y + 80, 200, 50), FONT, default_color=(255, 165, 0))
        self.quit_btn = MainMenuButton("Quit", pygame.Rect(center_x - 100, center_y + 160, 200, 50), FONT, default_color=(255, 0, 0))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.start_btn.draw_menu_button()
        self.save_btn.draw_menu_button()
        self.credit_btn.draw_menu_button()
        self.quit_btn.draw_menu_button()
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

            elif self.credit_btn.is_hovered(event.pos):
                credits = Credits(self.screen)
                credits.run()
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