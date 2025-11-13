import pygame
from components.BuildingList import BuildingList
from components.constants import SCREEN, GREEN, GRAY, BLACK, SMALL_FONT
pygame.init()


class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 250
        self.buildings_types = BuildingList().get_buildings()
        self.item_rects = []

    def draw(self, player):
        n = len(self.buildings_types)
        padding_x = 10
        padding_y = 8
        spacing = 10
        title_height = 30

        infos = [b.get_info() for b in self.buildings_types]
        sizes = [SMALL_FONT.size(txt) for txt in infos]
        max_text_w = max((w for w, h in sizes), default=0)
        item_heights = [h + padding_y * 2 for w, h in sizes]

        box_width = max(self.width, max_text_w + padding_x * 2)
        content_height = sum(item_heights) + max(0, (n - 1) * spacing)

        outer_x = self.x - padding_x
        outer_y = self.y - title_height - padding_x
        outer_width = box_width + padding_x * 2
        outer_height = title_height + padding_x + content_height + padding_x
        screen_w = SCREEN.get_width()
        if outer_x + outer_width > screen_w:
            outer_x = screen_w - outer_width
        if outer_x < 0:
            outer_x = 0

        outer_rect = pygame.Rect(outer_x, outer_y, outer_width, outer_height)
        pygame.draw.rect(SCREEN, BLACK, outer_rect, 2)
        inner_x = outer_x + padding_x

        title_text = SMALL_FONT.render("Shop", True, BLACK)
        title_pos_x = inner_x + (box_width - title_text.get_width()) // 2
        title_pos_y = outer_y + padding_x
        SCREEN.blit(title_text, (title_pos_x, title_pos_y))
        y_offset = self.y
        self.item_rects = []
        for i, Building in enumerate(self.buildings_types):
            h = item_heights[i]
            color = GREEN if player.can_afford(Building.cost) else GRAY

            rect = pygame.Rect(inner_x, y_offset, box_width, h)
            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 2)

            text_surface = SMALL_FONT.render(infos[i], True, BLACK)
            SCREEN.blit(text_surface, (inner_x + padding_x - padding_x +10, y_offset + padding_y))

            self.item_rects.append((rect, Building))
            y_offset += h + spacing

    def handle_click(self, pos, player):
        for rect, Building in self.item_rects:
            if rect.collidepoint(pos):
                return player.buy_building(Building)
        return False