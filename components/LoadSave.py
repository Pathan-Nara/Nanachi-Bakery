import os
from Player import Player
from Nanachi import Nanachi
from Shop import Shop
from Game import Game

class LoadSave:

    def __init__(self, data):
        self.data = data
        self.player = Player()
        self.nanachi = Nanachi(200, 300, 80)
        self.shop = Shop(500, 50)

    def load_game(self):
        print(self.data)
        self.player.nanachi = self.data['nanachi']
        self.player.nps = self.data['nps']
        buildings = self.data['buildings']
        name = self.data['name']
        for building in buildings:
            self.player.buildings.append(building)
        game = Game()
        game.player = self.player
        game.player.name = name
        game.nanachi = self.nanachi
        game.shop = self.shop
        game.run()

    def deleteSave(self, filename):
        filepath = os.path.join("saves", filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    
    def LoadSave(self, filename):
        filepath = self.getSavePath(filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = file.read()
                return data
        return None
