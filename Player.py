class Player:
    def __init__(self):
        self.nanachi = 0
        self.nps = 0 
        self.buildings = []
    
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