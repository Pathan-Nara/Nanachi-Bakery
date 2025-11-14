import pygame
from components.MainMenuButton import MainMenuButton
import random
class Credits:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.text = [
            "Ce jeu a été développé par :",
            "Meowfel Nyahri",
            "Nyaxime Miaffry",
            "Nyathan Para",
            "Merci à a tout nos contributeurs :",
            "Nanachi la goat",
            "Mizuki Akiyama pour le soutien moral",
            "Maxime Gréjon pour nous avoir financé",
            "Jorys Pephily pour les tests de QI (on a pas reussi)",
            "Victor Havard pour avoir deserter coda",
            "Poulet Whatsapp pour les idées de gameplay",
            "Le chien à Gréjon pour avoir implanté une puce 5G dans notre cerveau",
            "John Limbus pour les astie de bugs",
            "Sinclair pour avoir permis a Jorys de parler a une VRAIE femme",
            "Cécile Basle pour nous avoir deconcentrer en cours",
            "Cyril Vimard pour nous avoir rien appris en cours",
            "Encore Jorys Pephily pour avoir sauver mon chat de la noyade, ",
            "et sauvé ma mère d'une crise cardiaque et risqué sa vie pour aider ",
            "une grand mère qui se faisait agresser dans la rue (merci Jorys)",
            "Trouvez une alternance pour Jorys svp",
            "Encore merci Jorys pour avoir payé mes factures d'électricité pendant 3 mois",
            "Ah j'ai oublié mais merci Jorys d'avoir codé ce jeu à ma place aussi",
            "Ah oui aussi merci Jorys d'avoir fait mes devoirs de maths",
            "Bon allez j'arrête là, mais merci Jorys d'avoir empecher que je me fasse virer de l'école ",
            "Et merci a vous Dany de nous avoir supporter en classe pendant cette semaine de python !",
            "Bon gooning a tous ! Le skibidi Edge Rizz de Jorys lvl 5 Gyatt 67 sigma ohio patrick bateman vous remercie !"
        ]
        
        self.y_offset = self.screen.get_height()
        self.scroll_speed = 0.5

        self.trollBtn = MainMenuButton("X", pygame.Rect(self.screen.get_width() - 150, self.screen.get_height() - 90, 100, 40), self.font, default_color=(255,192,203))
        self.trollBtn2 = MainMenuButton("X", pygame.Rect(self.screen.get_width() - 300, self.screen.get_height() - 90, 100, 40), self.font, default_color=(255,192,203))
        self.trollBtn3 = MainMenuButton("X", pygame.Rect(self.screen.get_width() - 450, self.screen.get_height() - 90, 100, 40), self.font, default_color=(255,192,203))
        self.trollBtn4 = MainMenuButton("X", pygame.Rect(self.screen.get_width() - 600, self.screen.get_height() - 90, 100, 40), self.font, default_color=(255,192,203))
        self.trollBtn5 = MainMenuButton("X", pygame.Rect(self.screen.get_width() - 750, self.screen.get_height() - 90, 100, 40), self.font, default_color=(255,192,203))
        self.backBtn = MainMenuButton("Back", pygame.Rect(50, 50, 100, 40), self.font, default_color=(200, 0, 0))

        tab = [self.trollBtn, self.trollBtn2, self.trollBtn3, self.trollBtn4, self.trollBtn5]

    def draw(self):
        self.screen.fill(self.background_color)
        
        current_y = self.y_offset
        for line in self.text:
            text_surface = self.font.render(line, True, self.font_color)
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, current_y))
            
            if -50 < current_y < self.screen.get_height() + 50:
                self.screen.blit(text_surface, text_rect)
            
            current_y += 60
        
        self.y_offset -= self.scroll_speed
        
        if self.y_offset < -len(self.text) * 60:
            self.y_offset = self.screen.get_height()
            self.font_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.background_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.scroll_speed = random.randint(1, 60)
        
        self.backBtn.draw_menu_button()
        for btn in [self.trollBtn, self.trollBtn2, self.trollBtn3, self.trollBtn4, self.trollBtn5]:
            btn.set_position((random.randint(0, self.screen.get_width() - 100), random.randint(0, self.screen.get_height() - 40)))
            btn.set_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            btn.draw_menu_button()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backBtn.is_hovered(event.pos):
                        running = False
            self.draw()
