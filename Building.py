class Building:
    def __init__(self, name, cost, nps):
        self.name = name
        self.cost = cost
        self.nps = nps
        self.level = 0
    
    def get_info(self):
        return f"{self.name} {self.cost}n - {self.nps:.1f} nps"
    

    def update_cost(self):
        self.cost = int(self.cost * (2 ** self.level))

    def update_nps(self):
        self.nps = self.nps * (1.15 ** self.level)

    def upgrade(self):
        self.level += 1
        self.update_cost()
        self.update_nps()