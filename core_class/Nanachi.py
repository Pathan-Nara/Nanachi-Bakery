import pygame
from components.constants import SCREEN, BROWN
import os
import random
pygame.init()


class Nanachi:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.imgs = os.listdir("images/nanachi_img")
        self.current_img = self.imgs[0]
    
    def draw(self):
        nanachi = pygame.image.load(f"images/nanachi_img/{self.current_img}").convert_alpha()
        nanachi = pygame.transform.scale(nanachi, (self.radius*2, self.radius*2))
        SCREEN.blit(nanachi, (self.x - self.radius, self.y - self.radius))
        
    def randomize_image(self):
        self.current_img = random.choice(self.imgs)

    def randomize_position(self):
        screen_w = SCREEN.get_width()
        screen_h = SCREEN.get_height()
        self.x = random.randint(self.radius, screen_w - self.radius)
        self.y = random.randint(self.radius, screen_h - self.radius)    
    
    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx*dx + dy*dy <= self.radius*self.radius
    

