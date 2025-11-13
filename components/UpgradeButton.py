import pygame
from components.Button import Button
import random


class UpgradeButton(Button):    
    def __init__(self, upgrade_class, rect, font, padding_x=10, padding_y=8, border_radius=0):
        self.upgrade_class = upgrade_class
        self.rect = rect
        self.font = font
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.border_radius = border_radius
        self.info_text = upgrade_class.get_info()
        self.text_surface = self.font.render(self.info_text, True, (0, 0, 0))
    
    def draw_shop_button(self, player):
        if player.can_afford(self.upgrade_class.cost):
            if self.is_hovered(pygame.mouse.get_pos()):
                self.randomColor()
                self.random_position()
                
            else:
                self.set_color((0, 255, 0))
        else:
            self.set_color((128, 128, 128))
        self.draw(pygame.display.get_surface())
    
    def buy(self, player):
        return player.buy_upgrade(self.upgrade_class)
    
    def randomColor(self):
        self.bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.draw(pygame.display.get_surface())

    def random_position(self):
        self.rect = self.rect.move(random.randint(-20, 20), random.randint(-20, 20))