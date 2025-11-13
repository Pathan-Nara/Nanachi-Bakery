import pygame
from components.constants import FONT
from components.LoadData import LoadData
from components.LoadSave import LoadSave
from components.Button import Button
pygame.init()

class ListSaveMenu:

    def __init__(self, screen):
        self.screen = screen
        self.saves = []
        self.load_saves()
        self.buttons = []


    def load_saves(self):
        self.saves = LoadData().listSaves()

    def draw(self):
        self.screen.fill((0, 0, 0))
        y_offset = 100
        for save in self.saves:
            save_btn = Button(save, (400, y_offset), FONT)
            save_btn.draw(self.screen)
            self.buttons.append(save_btn)
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
                for btn in self.buttons:
                    if btn.is_hovered(event.pos) and btn.text == save:
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
