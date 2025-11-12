import pygame
from constants import FONT
from LoadData import LoadData
from LoadSave import LoadSave
pygame.init()

class ListSaveMenu:

    def __init__(self, screen):
        self.screen = screen
        self.saves = []
        self.load_saves()


    def load_saves(self):
        self.saves = LoadData().listSaves()

    def draw(self):
        self.screen.fill((0, 0, 0))
        y_offset = 100
        for save in self.saves:
            save_text = FONT.render(save, True, (255, 255, 255))
            save_rect = save_text.get_rect(center=(400, y_offset))
            self.screen.blit(save_text, save_rect)
            y_offset += 50
        pygame.display.flip()


    def LoadGame(self, save_name):
        data = LoadData().get_data(save_name)
        if data:
            loadSave = LoadSave(data)
            loadSave.load_game()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            y_offset = 100
            for save in self.saves:
                save_rect = pygame.Rect(0, y_offset - 25, 800, 50)
                if save_rect.collidepoint(event.pos):
                    self.LoadGame(save)
                y_offset += 50
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
            self.draw()
        pygame.quit()
