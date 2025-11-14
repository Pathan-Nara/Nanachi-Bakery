import os
import json
from core_class.Player import Player
from core_class.Nanachi import Nanachi
from core_class.Shop import Shop
from menus.GameMenu import Game
from components.BuildingList import BuildingList
from components.UpgradeList import UpgradeList
from components.constants import SCREEN

class LoadSave:

    def __init__(self, data):
        self.data = data
        self.player = Player()
        self.nanachi = Nanachi(SCREEN.get_width() // 4, SCREEN.get_height() // 2, 80)
        self.shop = Shop(SCREEN.get_width() - 20, 50)
        

    def load_game(self):
        self.player.nanachi = self.data['nanachi']
        self.player.nps = self.data['nps']
        self.player.npc = self.data['npc']
        buildings_data = self.data['buildings']
        upgrades_data = self.data['upgrades']
        self.update_player_buildings(buildings_data)
        self.update_player_upgrades(upgrades_data)
        name = self.data['name']
        game = Game()
        game.player = self.player
        game.player.name = name
        game.nanachi = self.nanachi
        game.shop = self.shop
        game.run()


    def update_player_buildings(self, buildings_data):
        available_buildings = BuildingList().get_buildings()
    
        for building_data in buildings_data:
            if isinstance(building_data, dict):
                for available_building in available_buildings:
                    if available_building.name == building_data['name']:
                        available_building.level = building_data.get('level', 0)
                        available_building.base_cost = building_data['base_cost']
                        available_building.base_nps = building_data['base_nps']
                        available_building.update_cost()
                        available_building.update_nps()
                        self.player.buildings.append(available_building)
                        break




    def update_player_upgrades(self, upgrades_data):
        available_upgrades = UpgradeList().get_upgrades()
        for upgrade_data in upgrades_data:
            if isinstance(upgrade_data, dict):
                for available_upgrade in available_upgrades:
                    if available_upgrade.name == upgrade_data['name']:
                        available_upgrade.level = upgrade_data.get('level', 0)
                        available_upgrade.base_cost = upgrade_data['base_cost']
                        available_upgrade.update_cost()
                        if available_upgrade.name == "Mini Nana":
                            for _ in range(upgrade_data.get('level', 0)):
                                available_upgrade.apply_effect(self.player)
                        self.player.upgrades.append(available_upgrade)
                        break

    def deleteSave(self, filename):
        filepath = os.path.join("saves", filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def LoadSave(self, filename):
        filepath = self.getSavePath(filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = json.load(file) 
                return data
        return None
    
    def getSavePath(self, filename):
        return os.path.join("saves", filename)