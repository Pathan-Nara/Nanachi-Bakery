import pygame

class Button:
    def __init__(self, text, pos, font, text_color=(255, 255, 255), bg_color=None):
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.text_surface = self.font.render(text, True, text_color)
        self.rect = self.text_surface.get_rect(center=pos)
        
    def draw(self, screen):
        if self.bg_color:
            padding = 10
            bg_rect = self.rect.inflate(padding * 2, padding * 2)
            pygame.draw.rect(screen, self.bg_color, bg_rect)
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, 2)
        screen.blit(self.text_surface, self.rect)

    def set_color(self, color):
        self.bg_color = color

    def set_position(self, pos):
        self.rect.center = pos

    def get_color(self):
        return self.bg_color
    
    def font_color(self, color):
        self.text_color = color
        self.text_surface = self.font.render(self.text, True, color)
    
    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)
    
    def update_text(self, new_text):
        center = self.rect.center
        self.text = new_text
        self.text_surface = self.font.render(new_text, True, self.text_color)
        self.rect = self.text_surface.get_rect(center=center)