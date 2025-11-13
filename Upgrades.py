class Upgrades:
    def __init__(self, name,cost, level=1):
        self.name = name
        self.cost = cost
        self.level = level

    def get_info(self):
        return f"{self.name} Upgrade - Level {self.level}"

    def upgrade(self):
        self.level += 1

    def update_cost(self):
        self.cost = int(self.cost * 1.5)