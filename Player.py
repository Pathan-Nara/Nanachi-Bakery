from Save import Save
from random import randint
class Player:
    def __init__(self):
        self.nanachi = 0
        self.nps = 0 
        self.buildings = []
        self.name = randint(0, 9999)
    
    def add_nanachi(self, amount):
        self.nanachi += amount

    
    def can_afford(self, cost):
        return self.nanachi >= cost
    
    def buy_building(self, building):
        if self.can_afford(building.cost):
            self.nanachi -= building.cost
            self.buildings.append(building)
            self.nps += building.nps
            building.upgrade()
            return True
        return False
    
    def update(self, dt):
        self.nanachi += self.nps * dt

    def save_game(self):
        saver = Save(f"save_{self.name}.sav")
        saver.save_game(self, self.buildings)

