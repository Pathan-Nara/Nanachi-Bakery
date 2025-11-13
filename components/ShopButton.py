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
    
    def draw_shop_button(self, player):
        if player.can_afford(self.building_class.cost):
            if self.is_hovered(pygame.mouse.get_pos()):
                self.randomColor()
            else:
                self.set_color((0, 255, 0))
        else:
            self.set_color((128, 128, 128))
        self.draw(pygame.display.get_surface())
    
    def buy(self, player):
        return player.buy_building(self.building_class)
    
    def randomColor(self):
        self.bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.draw(pygame.display.get_surface())
    