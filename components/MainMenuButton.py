import pygame
from components.Button import Button
import random

class MainMenuButton(Button):
    def __init__(self, text, rect, font, padding_x=10, padding_y=8, border_radius=100, default_color=(255, 255, 255)):
        self.rect = rect
        self.font = font
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.border_radius = border_radius
        self.default_color = default_color
        self.text_surface = self.font.render(text, True, (255, 255, 255))

    def draw_menu_button(self):
        if self.is_hovered(pygame.mouse.get_pos()):
            self.set_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        else:
            self.set_color(self.default_color)
        self.draw(pygame.display.get_surface())
    
