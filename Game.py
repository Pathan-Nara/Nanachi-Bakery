import pygame
from Player import Player
from Nanachi import Nanachi
from Shop import Shop
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('arial', 30)
SMALL_FONT = pygame.font.SysFont('arial', 20)
SCREEN = pygame.display.set_mode((800, 600))    



class Game:
    def __init__(self):
        self.player = Player()
        self.nanachi = Nanachi(200, 300, 80)
        self.shop = Shop(500, 50)
        self.clock = pygame.time.Clock()
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.nanachi.is_clicked(event.pos):
                    self.player.add_nanachi(1)
                else:
                    self.shop.handle_click(event.pos, self.player)
    
    def update(self):
        dt = self.clock.tick(60) / 1000.0
        self.player.update(dt)
    
    def draw(self):
        SCREEN.fill(WHITE)

        self.nanachi.draw()

        nanachi_text = FONT.render(f"Nanachi: {int(self.player.nanachi)}", True, BLACK)
        SCREEN.blit(nanachi_text, (50, 50))

        nps_text = SMALL_FONT.render(f"NPS: {self.player.nps:.1f}", True, BLACK)
        SCREEN.blit(nps_text, (50, 100))

        owned_text = SMALL_FONT.render(f"Bâtiments: {len(self.player.buildings)}", True, BLACK)
        SCREEN.blit(owned_text, (50, 130))
        self.shop.draw(self.player)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        
