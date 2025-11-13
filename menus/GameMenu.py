import pygame
from core_class.Player import Player
from core_class.Nanachi import Nanachi
from core_class.Shop import Shop
from components.Button import Button
import random
from components.constants import SCREEN, WHITE, BLACK, FONT, SMALL_FONT
pygame.init()




class Game:
    def __init__(self):
        self.player = Player()
        self.nanachi = Nanachi(SCREEN.get_width() // 4, SCREEN.get_height() // 2, 80)
        self.shop = Shop(SCREEN.get_width() - 20, 50)
        self.clock = pygame.time.Clock()
        self.running = True
        self.buttons = []
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.nanachi.is_clicked(event.pos):
                    self.player.add_nanachi(self.player.npc)
                    self.nanachi.randomize_image()
                    self.nanachi.randomize_position()
                for btn in self.buttons:
                    if btn.is_hovered(event.pos) and btn.text == "Save and Quit":
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
        # SCREEN.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SCREEN.fill(WHITE)
        
        nanachi_text = FONT.render(f"Nanachi: {int(self.player.nanachi)}", True, BLACK)
        SCREEN.blit(nanachi_text, (50, 50))

        nps_text = SMALL_FONT.render(f"NPS: {self.player.nps:.1f}", True, BLACK)
        SCREEN.blit(nps_text, (50, 100))

        npc_text = SMALL_FONT.render(f"NPC: {self.player.npc}", True, BLACK)
        SCREEN.blit(npc_text, (50, 130))

        building_text = SMALL_FONT.render(f"Bâtiments: {len(self.player.buildings)}", True, BLACK)
        SCREEN.blit(building_text, (50, 160))

        upgrade_text = SMALL_FONT.render(f"Upgrades: {len(self.player.upgrades)}", True, BLACK)
        SCREEN.blit(upgrade_text, (50, 190))

        self.shop.draw(self.player)

        save_btn = Button("Save and Quit", (SCREEN.get_width() - 100, SCREEN.get_height() - 50), FONT, BLACK)
        save_btn.draw(SCREEN)
        self.buttons.append(save_btn)

        self.nanachi.draw()

        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        
