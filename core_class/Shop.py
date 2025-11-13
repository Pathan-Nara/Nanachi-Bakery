import pygame
from components.BuildingList import BuildingList
from components.constants import SCREEN, GREEN, GRAY, BLACK, SMALL_FONT
from components.ShopButton import ShopButton
from components.UpgradeList import UpgradeList
from components.UpgradeButton import UpgradeButton

pygame.init()


class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 250
        self.buildings_types = BuildingList().get_buildings()
        self.upgrades_types = UpgradeList().get_upgrades()
        self.buttons = []


    def get_player_building(self, building_type, player):
        for player_building in player.buildings:
            if player_building.name == building_type.name:
                return player_building
        return building_type
    
    def get_player_upgrade(self, upgrade_type, player):
        for player_upgrade in player.upgrades:
            if player_upgrade.name == upgrade_type.name:
                return player_upgrade
        return upgrade_type



    def calculate_building_item_dimensions(self, items_list, player):
        display_items = [self.get_player_building(item, player) for item in items_list]
        infos = [item.get_info() for item in display_items]
        sizes = [SMALL_FONT.size(txt) for txt in infos]
        max_text_w = max((w for w, h in sizes), default=0)
        item_heights = [h + self.padding_y * 2 for w, h in sizes]
        return display_items, infos, sizes, max_text_w, item_heights
    
    def calculate_upgrade_item_dimensions(self, items_list, player):
        display_items = [self.get_player_upgrade(item, player) for item in items_list]
        infos = [item.get_info() for item in display_items]
        sizes = [SMALL_FONT.size(txt) for txt in infos]
        max_text_w = max((w for w, h in sizes), default=0)
        item_heights = [h + self.padding_y * 2 for w, h in sizes]
        return display_items, infos, sizes, max_text_w, item_heights
    

    def calculate_box_dimensions(self, max_text_w, item_heights, n_items, title_height=30):
        spacing = 10
        box_width = max(self.width, max_text_w + self.padding_x * 2)
        content_height = sum(item_heights) + max(0, (n_items - 1) * spacing)
    
        outer_width = box_width + self.padding_x * 2
        outer_height = title_height + self.padding_x + content_height + self.padding_x
    
        return box_width, outer_width, outer_height, content_height



    def adjust_position_to_screen(self, outer_x, outer_y, outer_width):
        screen_w = SCREEN.get_width()
    
        if outer_x + outer_width > screen_w:
            outer_x = screen_w - outer_width
        if outer_x < 0:
            outer_x = 0
    
        return outer_x, outer_y
    


    def draw_shop_container(self, outer_rect, box_width, title_height):
        pygame.draw.rect(SCREEN, BLACK, outer_rect, 2)
    
        inner_x = outer_rect.x + self.padding_x
        title_text = SMALL_FONT.render(self.title, True, BLACK)
        title_pos_x = inner_x + (box_width - title_text.get_width()) // 2
        title_pos_y = outer_rect.y + self.padding_x
    
        SCREEN.blit(title_text, (title_pos_x, title_pos_y))
        return inner_x
    


    def create_and_draw_shop_buttons(self, display_items, item_heights, inner_x, start_y, box_width, player):
        y_offset = start_y
        spacing = 10
    
        for i, item in enumerate(display_items):
            h = item_heights[i]
            rect = pygame.Rect(inner_x, y_offset, box_width, h)
            btn = ShopButton(item, rect, SMALL_FONT, self.padding_x, self.padding_y)
            btn.draw_shop_button(player)
            self.buttons.append(btn)
            y_offset += h + spacing

    def create_and_draw_upgrade_buttons(self, display_items, item_heights, inner_x, start_y, box_width, player):
        y_offset = start_y
        spacing = 10
    
        for i, item in enumerate(display_items):
            h = item_heights[i]
            rect = pygame.Rect(inner_x, y_offset, box_width, h)
            btn = UpgradeButton(item, rect, SMALL_FONT, self.padding_x, self.padding_y)
            btn.draw_shop_button(player)
            self.buttons.append(btn)
            y_offset += h + spacing
            


    def draw_building_shop(self, player):
        self.padding_x = 10
        self.padding_y = 8
        self.title = "Buildings"
        title_height = 30
        display_items, infos, sizes, max_text_w, item_heights = \
            self.calculate_building_item_dimensions(self.buildings_types, player)
        n = len(self.buildings_types)
        box_width, outer_width, outer_height, content_height = \
            self.calculate_box_dimensions(max_text_w, item_heights, n, title_height)
        outer_x = self.x - self.padding_x
        outer_y = self.y - title_height - self.padding_x
        outer_x, outer_y = self.adjust_position_to_screen(outer_x, outer_y, outer_width)
        outer_rect = pygame.Rect(outer_x, outer_y, outer_width, outer_height)
        inner_x = self.draw_shop_container(outer_rect, box_width, title_height)
        self.create_and_draw_shop_buttons(display_items, item_heights, inner_x, self.y, box_width, player)
        buildings_shop_height = outer_height
        self.draw_upgrade_shop(player, buildings_shop_height)



    def draw_upgrade_shop(self, player, offset_y):
        self.padding_x = 10
        self.padding_y = 8
        self.title = "Upgrades"
        title_height = 30
        spacing_between_shops = 15
        display_items, infos, sizes, max_text_w, item_heights = \
            self.calculate_upgrade_item_dimensions(self.upgrades_types, player)
        n = len(self.upgrades_types)
        box_width, outer_width, outer_height, content_height = \
            self.calculate_box_dimensions(max_text_w, item_heights, n, title_height)
        outer_x = self.x - self.padding_x
        outer_y = self.y - title_height - self.padding_x + offset_y + spacing_between_shops
        outer_x, outer_y = self.adjust_position_to_screen(outer_x, outer_y, outer_width)
        outer_rect = pygame.Rect(outer_x, outer_y, outer_width, outer_height)
        inner_x = self.draw_shop_container(outer_rect, box_width, title_height)
        start_y = outer_y + title_height + self.padding_x
        self.create_and_draw_upgrade_buttons(display_items, item_heights, inner_x, start_y, box_width, player)

    def draw(self, player):
        self.draw_building_shop(player)

    def handle_click(self, pos, player):
        for btn in self.buttons:
            if btn.is_hovered(pos):
                return btn.buy(player)
        return False