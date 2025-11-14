from core_class.Upgrades import Upgrades
import pygame
import os
import random
from components.constants import SCREEN
from upgrades.Nanas import Nanas

class MiniNana(Upgrades):
    def __init__(self):
        super().__init__("Mini Nana", 1)
        self.nana_list = []
        self.screen = SCREEN
    
    def apply_effect(self, player):
        self.nana_list.append(Nanas(self.screen))

    
    def update_nanas(self):
        for nana in self.nana_list:
            nana.update(self.screen)

    def draw_nanas(self, screen):
        for nana in self.nana_list:
            nana.draw(screen)
    
    def handle_click(self, pos, player):
        for nana in self.nana_list:
            nana_rect = pygame.Rect(nana.x, nana.y, nana.width, nana.height)
            if nana_rect.collidepoint(pos):
                nana.on_click(player)
                return True
        return False