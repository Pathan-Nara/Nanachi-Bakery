import pygame
from components.constants import SCREEN, BROWN
pygame.init()


class Nanachi:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        nanachi = pygame.image.load("images/nanachi.png").convert_alpha()
        nanachi = pygame.transform.scale(nanachi, (self.radius*2, self.radius*2))
        SCREEN.blit(nanachi, (self.x - self.radius, self.y - self.radius))
        
    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx*dx + dy*dy <= self.radius*self.radius
    

