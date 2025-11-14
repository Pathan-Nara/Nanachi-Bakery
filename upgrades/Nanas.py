import pygame
import os
import random

class Nanas:
    def __init__(self, screen):
        self.screen = screen
        self.speed = 1
        self.imgs = os.listdir("images/mini_nana_img")
        self.height = 30
        self.width = 30
        self.current_img_name = self.imgs[random.randint(0, len(self.imgs) - 1)]
        self.current_img = None 
        self.load_image()
        
        self.x = random.randint(0, screen.get_width() - 30)
        self.y = random.randint(0, screen.get_height() - 30)
        self.dx = random.choice([-1, 1]) * self.speed
        self.dy = random.choice([-1, 1]) * self.speed
    
    def load_image(self):
        mini_nana = pygame.image.load(f"images/mini_nana_img/{self.current_img_name}").convert_alpha()
        self.current_img = pygame.transform.scale(mini_nana, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.current_img, (self.x, self.y))

    def update(self, screen):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > screen.get_width() - 30:
            self.dx *= -1
        if self.y < 0 or self.y > screen.get_height() - 30:
            self.dy *= -1
    
    def randomize_image(self):
        self.current_img_name = random.choice(self.imgs)
        self.load_image()

    def set_height_width(self, height, width):
        self.height = height
        self.width = width
        self.load_image()

    
    def set_speed(self, speed):
        self.speed = speed
        self.dx = (self.dx / abs(self.dx)) * self.speed
        self.dy = (self.dy / abs(self.dy)) * self.speed

    def on_click(self, player):
        point = random.randint(int(-(player.nanachi)), int(player.nanachi))
        self.set_speed(random.randint(1, 50))
        self.set_height_width(random.randint(10, 300), random.randint(10, 300))
        self.randomize_image()
        player.nanachi += point