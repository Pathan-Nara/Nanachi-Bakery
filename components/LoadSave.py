import os
import json
from core_class.Player import Player
from core_class.Nanachi import Nanachi
from core_class.Shop import Shop
from menus.GameMenu import Game
from core_class.Building import Building
from core_class.Upgrades import Upgrades
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
        for building_data in buildings_data:
            if isinstance(building_data, dict):
                building = Building(
                    name=building_data['name'],
                    cost=building_data['base_cost'],   
                    nps=building_data['base_nps']
                )
                building.level = building_data.get('level', 0)
                building.update_cost()  
                building.update_nps()   
            
                self.player.buildings.append(building)
            elif isinstance(building_data, Building):
                self.player.buildings.append(building_data)




    def update_player_upgrades(self, upgrades_data):
        for upgrade_data in upgrades_data:
            if isinstance(upgrade_data, dict):
                upgrade = Upgrades(
                    name=upgrade_data['name'],
                    cost=upgrade_data['base_cost'],
                )
                upgrade.level = upgrade_data.get('level', 0)
                upgrade.update_cost()     
            
                self.player.upgrades.append(upgrade)
            elif isinstance(upgrade_data, Upgrades):
                self.player.upgrades.append(upgrade_data)



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