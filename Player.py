from Save import Save
import datetime
class Player:
    def __init__(self):
        self.nanachi = 0
        self.nps = 0
        self.npc = 1
        self.buildings = []
        self.upgrades = []
        self.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    def add_nanachi(self, amount):
        self.nanachi += amount

    
    def can_afford(self, cost):
        return self.nanachi >= cost
    
    def buy_building(self, building):
        if self.can_afford(building.cost):
            self.nanachi -= building.cost
            if building not in self.buildings:
                self.buildings.append(building)
            self.nps += building.nps
            building.upgrade()
            return True
        return False
    
    def buy_upgrade(self, upgrade):
        if self.can_afford(upgrade.cost):
            self.nanachi -= upgrade.cost
            if upgrade not in self.upgrades:
                self.upgrades.append(upgrade)
            upgrade.upgrade(self)
            return True
        return False
    
    def update(self, dt):
        self.nanachi += self.nps * dt

    def save_game(self):
        saver = Save(f"save_{self.name}.sav")
        saver.save_game(self, self.buildings, self.upgrades)

