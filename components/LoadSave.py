import os
import json
from Player import Player
from Nanachi import Nanachi
from Shop import Shop
from Game import Game
from Building import Building

class LoadSave:

    def __init__(self, data):
        self.data = data
        self.player = Player()
        self.nanachi = Nanachi(200, 300, 80)
        self.shop = Shop(500, 50)

    def load_game(self):
        self.player.nanachi = self.data['nanachi']
        self.player.nps = self.data['nps']
        buildings_data = self.data['buildings']
        self.update_player_buildings(buildings_data)
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
                level = building_data.get('count', 0)
                
                if 'cost' in building_data and 'nps' in building_data:
                    building = Building(
                        name=building_data['name'],
                        cost=building_data['cost'],
                        nps=building_data['nps']
                    )
                    building.level = level
                    building.cost = building_data['cost']
                    building.nps = building_data['nps']
                else:
                    current_cost = building_data['cost']
                    current_nps = building_data['nps']
                    base_cost = int(current_cost / (2 ** level)) if level > 0 else current_cost
                    base_nps = current_nps / (1.15 ** level) if level > 0 else current_nps
                    
                    building = Building(
                        name=building_data['name'],
                        cost=base_cost,
                        nps=base_nps
                    )
                    building.level = level
                    building.cost = current_cost
                    building.nps = current_nps
                    
                self.player.buildings.append(building)
            elif isinstance(building_data, Building):
                self.player.buildings.append(building_data)

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