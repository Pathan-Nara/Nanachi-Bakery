import pygame
from components.Button import Button
import random


class ShopButton(Button):    
    def __init__(self, building_class, rect, font, padding_x=10, padding_y=8):
        self.building_class = building_class
        self.rect = rect
        self.font = font
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.info_text = building_class.get_info()
        self.text_surface = self.font.render(self.info_text, True, (0, 0, 0))
    
    def draw(self, screen, player, green_color, gray_color, black_color):
        color = green_color if player.can_afford(self.building_class.cost) else gray_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, black_color, self.rect, 2)
        screen.blit(self.text_surface, (self.rect.x + self.padding_x, self.rect.y + self.padding_y))
    
    def buy(self, player):
        return player.buy_building(self.building_class)
    