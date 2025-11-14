import pygame
from components.MainMenuButton import MainMenuButton
from components.constants import FONT
import random
import subprocess
import os

class DoNotClick:

    def __init__(self, screen):
        self.screen = screen
        screen_w = screen.get_width()
        screen_h = screen.get_height()
        self.center_x = screen_w // 2
        self.center_y = screen_h // 2
        self.backBtn = MainMenuButton("Back", pygame.Rect(50, 50, 100, 40), FONT, default_color=(200, 0, 0))
        self.possible_texts = [
            "I sai'd DO NOT CLICK!",
            "Do not click again!",
            "It will break your computer!",
            "Seriously, stop clicking!",
        ]
        self.doNotClick_btn = self.randomize_btn()
        self.click_count = 0
        self.running = True


    def draw(self):
        if self.click_count >= 7:
            self.doNotClick_btn = MainMenuButton("Good Luck", pygame.Rect(self.center_x - 150, self.center_y, 300, 50), FONT, default_color=(200, 0, 0))
            self.screen.fill((0, 0, 0))
            self.backBtn.draw_menu_button()
            self.doNotClick_btn.draw_menu_button()
            pygame.display.flip()
        else:
            self.screen.fill((0, 0, 0))
            self.backBtn.draw_menu_button()
            self.doNotClick_btn.draw_menu_button()
            pygame.display.flip()

    def randomize_btn(self):
        random_text = random.choice(self.possible_texts)
        donotclick_btn = MainMenuButton(random_text, pygame.Rect(self.center_x - 150, self.center_y, 300, 50), FONT, default_color=(200, 0, 0))
        return donotclick_btn
    

    def start_py(self):
        pygame.time.delay(2000)
        base = os.path.dirname(os.path.abspath(__file__))  
        target = os.path.join(base, "..", "secrets", "DoNotExecute.py")
        target = os.path.abspath(target)

        subprocess.Popen(["python", target])
        pygame.quit()
        exit()


    def handle_event(self, event):
        if self.click_count >= 7:
            self.start_py()
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.backBtn.is_hovered(event.pos):
                self.running = False
            elif self.doNotClick_btn.is_hovered(event.pos):
                self.click_count += 1
                self.doNotClick_btn = self.randomize_btn()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()
        