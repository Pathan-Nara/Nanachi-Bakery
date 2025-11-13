import pygame
from Player import Player
from Nanachi import Nanachi
from Shop import Shop
from components.constants import SCREEN, WHITE, BLACK, FONT, SMALL_FONT
pygame.init()




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
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.nanachi.is_clicked(event.pos):
                    self.player.add_nanachi(1)
                elif 650 <= event.pos[0] <= 750 and 500 <= event.pos[1] <= 550:
                    self.player.save_game()
                    self.running = False
                    pygame.quit()
                    exit()

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

        save_text = SMALL_FONT.render("Save and Quit", True, BLACK)
        SCREEN.blit(save_text, (650 + 10, 500 + 10))

        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        
