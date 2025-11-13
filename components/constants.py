import pygame
pygame.init()

FONT = pygame.font.SysFont('arial', 30)
SMALL_FONT = pygame.font.SysFont('arial', 20)
screen_resolution = pygame.display.Info()
SCREEN = pygame.display.set_mode((screen_resolution.current_w, screen_resolution.current_h))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)