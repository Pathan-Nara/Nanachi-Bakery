import pygame
from BuildingList import BuildingList

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
SMALL_FONT = pygame.font.SysFont('arial', 20)
FONT = pygame.font.SysFont('arial', 30)


class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 250
        self.buildings_types = BuildingList().get_buildings()
    
    def draw(self, player):
        y_offset = self.y
        for i, Building in enumerate(self.buildings_types):
            color = GREEN if player.can_afford(Building.cost) else GRAY
            
            rect = pygame.Rect(self.x, y_offset, self.width, 60)
            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 2)
            
            text = SMALL_FONT.render(Building.get_info(), True, BLACK)
            SCREEN.blit(text, (self.x + 10, y_offset + 20))
            
            y_offset += 70
    
    def handle_click(self, pos, player):
        y_offset = self.y
        for Building in self.buildings_types:
            rect = pygame.Rect(self.x, y_offset, self.width, 60)
            if rect.collidepoint(pos):
                return player.buy_building(Building)
            y_offset += 70
        return False