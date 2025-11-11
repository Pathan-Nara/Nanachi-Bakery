import pygame
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
BROWN = (150, 75, 0)

class Nanachi:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        pygame.draw.circle(SCREEN, BROWN, (self.x, self.y), self.radius)
    
    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx*dx + dy*dy <= self.radius*self.radius
    

